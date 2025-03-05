
# The Cosmic Evolution of Fast Radio Bursts Inferred from CHIME/FRB Baseband Catalog 1

This repository contains data products and visualization tools associated with the paper: [Gupta, Beniamini, Kumar & Finkelstein (2025)](https://arxiv.org/abs/2501.09810)

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

- [Visualize CHIME Observation Function](./vis_obsfunc.ipynb): Visualize and analyze the observation function derived from CHIME injections (see the [CHIME injections system paper](https://arxiv.org/abs/2206.14079)). This is a data product generated in the [CHIME/FRB Catalog 1 paper](https://arxiv.org/abs/2106.04352), provided by its corresponding author Kiyoshi Masui (used and copy provided here with his permission.)

### Visualize and Analyze Baseband data
- [Compare Baseband and Intensity Catalogs](./baseband_compare.ipynb)
- [Analyze Baseband Observables](./dm_flu_snr_analysis.ipynb)
- [Sample Selection](./sample_selection.ipynb)

### Estimate the cosmic star formation rate density (SFRD)


## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Contact

For any questions or inquiries, please contact [Om](mailto:om@example.com).
