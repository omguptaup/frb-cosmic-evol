
# The Cosmic Evolution of Fast Radio Bursts Inferred from CHIME/FRB Baseband Catalog 1

This repository contains data products and visualization tools associated with the paper: [Gupta, Beniamini, Kumar & Finkelstein (2025)](https://arxiv.org/abs/2501.09810). Please cite in your work, if using data products, visualization, or code from here.

## Installation

To run the notebooks, you need to have Python and Jupyter Notebook installed. Download or clone or fork the repository, and navigate to the root directory. You can install the required packages using:

a conda environment file
```bash
conda env create -f environment.yml
```

or

```bash
pip install -r requirements.txt
```

Most files are interactive Jupyter Notebooks, so you need to have Jupyter Notebook/Lab or VSCode installed.

## Notebooks

- [Visualize CHIME Observation Function](./vis_obsfunc.ipynb): Visualize and analyze the observation function derived from CHIME injections (see the [CHIME injections system paper](https://arxiv.org/abs/2206.14079)). This is a data product generated in the [CHIME/FRB Catalog 1 paper](https://arxiv.org/abs/2106.04352), provided by its corresponding author Kiyoshi Masui (used and copy provided here with his permission. Kindly cite these works if using the observation function.)

### Visualize and Analyze Baseband data
- [Compare Baseband and Intensity Catalogs](./baseband_compare.ipynb)
- [Analyze Baseband Observables](./dm_flu_snr_analysis.ipynb)
- [Sample Selection](./sample_selection.ipynb)

### Estimate the cosmic star formation rate density (SFRD)
- [High-redshift UV luminosity function](./uvlf_dpl.ipynb)
- [Cosmic SFRD z=0-14](./sfrd_compute.ipynb)

### DM distributions and underlying code
- [Visualize changes to FRB package](./calibrate_macigm.ipynb): This project uses the [FRBs/FRB package](https://github.com/FRBs/FRB), making changes primarily to the implemented SFRD and stellar mass density evolution.
- [DM-IGM and DM-host distributions](./dm_distn.ipynb)

### Parameter posteriors
- [SFR-SMD Hybrid Model](./DMnF_mcmc_agEf.ipynb)
- [Constant Delay time model](./DMnF_mcmc_agEt.ipynb)
- [Delayed-tau model](./DMnF_nestsamp_dtau.ipynb)
- [Rayleigh-distribution tau model](./DMnF_nestsamp_raytau.ipynb)
- [SSH+CDT posteriors from Zhang+21](./DMnF_zhang_mcmc.ipynb)

### Redshift, Energy, DM and FLuence distributions
- [Generate calibrated distributions](./DMnF_compare_zevol.ipynb)

## License

This project is licensed under the BSD-3 License. See the [LICENSE](./LICENSE) file for details.

## Contact

For any questions or inquiries, please contact [Om](mailto:omgupta@utexas.edu).
