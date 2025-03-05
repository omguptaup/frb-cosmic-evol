import numpy as np
from scipy.interpolate import griddata, SmoothBivariateSpline
from importlib_resources import files

def observation_function(x_param, fname="observation_function.npz"):
    # Import CHIME observation function file
    # Courtesy: Kiyoshi Masui
    obsfunc = np.load(files('files').joinpath(fname))
    of_snr = obsfunc['snr_edges']
    of_flu = obsfunc['flu_edges']
    of_dm = obsfunc['dm_edges']
    of = obsfunc['observation_function']
    of_det = np.zeros((of_flu.shape[0]-1, of_dm.shape[0]-2))
    for i in range(1,of_snr.shape[0]-1):
        of_det[:,:] += of[i,:,1:]*(of_snr[i+1] - of_snr[i])  
    of_det = np.log10(of_det[7:-7,:])

    # Define array for DM and F array binning
    logF_of = (np.log10(of_flu[7:-8]) + np.log10(of_flu[8:-7]))/2 + 3
    logdm_of = (np.log10(of_dm[1:-1]) + np.log10(of_dm[2:]))/2

    # Interpolate the missing points
    inter_det = np.ma.masked_invalid(of_det)
    xx, yy = np.meshgrid(logF_of, logdm_of, indexing='ij')
    F_mask = xx[~inter_det.mask]
    dm_mask = yy[~inter_det.mask]
    inter_det = inter_det[~inter_det.mask]

    interp2d = griddata((F_mask, dm_mask), inter_det.T, (xx, yy), method='nearest')

    # Smooth and the extrapolate the of_smooth data over the full range of DM and F on a regularly spaced log-grid
    inter_det = np.ma.masked_invalid(interp2d)
    xx, yy = np.meshgrid(logF_of, logdm_of, indexing='ij')
    F_mask = xx[~inter_det.mask]
    dm_mask = yy[~inter_det.mask]
    inter_det = inter_det[~inter_det.mask]

    sbs = SmoothBivariateSpline(F_mask, dm_mask, inter_det, kx=5, ky=5)

    xgrid, ygrid = np.meshgrid(np.log10(x_param[2]), np.log10(x_param[1]), indexing='ij')
    logF = np.log10(x_param[2][:-1]) + np.diff(np.log10(x_param[2]))/2
    logdm = np.log10(x_param[1][0:-1]) + np.diff(np.log10(x_param[1]))/2
    xmidgrid, ymidgrid = np.meshgrid(logF, logdm, indexing='ij')

    of_smooth = sbs(xmidgrid.ravel(), ymidgrid.ravel(), grid=False)

    of_smooth = 10**of_smooth.reshape(logF.shape[0], logdm.shape[0])

    return sbs, of_smooth

def match_cats(cat1, cat2):
    cat1_idx = []
    cat2_idx = []
    for i in range(cat2.shape[0]):
        flag = np.where(cat1['tns_name'] == cat2['tns_name'][i])[0]
        if len(flag) != 0 and cat2['fluence'][i] > 0:
            cat1_idx.append(flag[0])
            cat2_idx.append(i)
    return cat1_idx, cat2_idx