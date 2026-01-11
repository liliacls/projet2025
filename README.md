# Project - Gene Expression Count Matrix Analysis
Programming project - M1 BIMS

University of Rouen Normandie - 2025

# Project Objective

This project implements a small analysis pipeline for a gene expression count matrix, including : 
- Loading of .tsv and .tsv.gz files
- Computation of total counts per gene and per tissue/cell
- Identification of minimum and maximum total values
- Visualization of the top 10 genes and tissues/cells (barplots)
- Generation of a synthetic HTML report
- Unit testing and code coverage analysis

# Project Structure

PROJET2025/

├── .pytest_cache/

├── data/

│   └── ARCHS4.tsv

│   └── ARCHS4.tsv.gz

│   └── mini_ARCHS4.tsv

│   └── mini_ARCHS4.tsv.gz

├── src/

│   ├── __init__.py

│   ├── main.py

│   ├── io_utils.py

│   ├── stats_utils.py

│   └── plotting.py

├── tests/

│   ├── __init__.py

│   ├── test_io_utils.py

│   └── test_stats_utils.py

├── .gitignore

├── README.md

└── requirements.txt

# Dependency Installation

pip install -r requirements.txt

# Module Description

- io_utils.py : Loads count matrices in .tsv or .tsv.gz format and filters count rows. 

- stats_utils.py : Statistical utilities --> total counts per gene/tissue, min/max detection  and structured summary.

- plotting.py : Generates bar plots for the top 10 genes and tissues/cells based on total counts.

- main.py : Main pipeline. Loads the matrix, computes statistics, generates plots, and exports an HTML report containing results and visualizations.

# Pipeline Execution 

- The input matrix is passed as a command-line argument :

python src/main.py data/file.tsv

- For the matrix provided in the project :

python src/main.py data/ARCHS4.tsv

# Unit Tests

- Run all tests : 

PYTHONPATH=src pytest -s

- Run a specific test module :

PYTHONPATH=src pytest -s tests/test_stats_utils.py

PYTHONPATH=src pytest -s tests/test_io_utils.py

# Code Coverage 

- Generate an HTML coverage report :

PYTHONPATH=src pytest -s --cov=src --cov-report=html

- Open the report:
  
Linux : xdg-open htmlcov/index.html

macOS : open htmlcov/index.html

Windows : start htmlcov/index.html

