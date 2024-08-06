# Predicting Electric Vehicle Count w/ IRS Data

## Overview
1) Pre-Processing File (Quarto): /code/processing-code/pre_process_tax_data.qmd

2) Exploratory Data Analysis (Quarto):
  - /code/eda-code/eda-ev-dataset.qnd
  - /code/eda-code/eda-ev-tax.qmd

3) Main code file (Quarto): /code/analysis-code/statistical_analysis.qmd done with Python/Quarto/Github. 

4) References present in code/analysis-code/references.bib file.

5) Report file: /products/manuscript/Manuscript.qmd done with Python/Quarto/Github.
Knit this file to obtain Manuscript.docx which is the final report.

6) Supplemental file: /products/manuscript/supplement/Supplement.qmd done with Python/Quarto/Github.
knit this file to obtain Supplement.docx which is the final report.

## Pre-requisites
- **Python Version 3.11.9**
### Execute these commands in your terminal
- **Install Homebrew:** `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
- **Install 'ffmpeg' via Homebrew:** `brew install libomp`
- **Create local virtual env:** `python3 -m venv .venv`
- **Activate local virtual env:** `source .venv/bin/activate`
- **Install Python dependencies:** `pip3 install -r requirements.txt`


Once you got the repository, you can check out the examples by executing them in order. First run the processing code, which will produce the processed data. Then run the analysis scripts, which will take the processed data and produce some results.