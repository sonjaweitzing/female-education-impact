# MoSD

This Repository contains the source code of my data management project for the final exam in the Management of Scientific Data course at the University of Jena.


## Contents- [MoSD](#mosd)
- [Datasets](#datasets)
- [Research question](#research-question)
- [Project description](#project-description)
- [Naming Convention](#naming-convention)
- [File Structure](#file-structure)
- [Metadata](#metadata)
- [Installation](#installation)
- [License](#license)

## Datasets

This project uses two datasets from Gapminder and Our World in Data:
https://www.gapminder.org/data/
https://ourworldindata.org/grapher/womens-educational-attainment-vs-fertility

## Research question

How does female education impact society in different countries?

## Project description

This project aims to demonstrate the management of scientific data using the xx and yy datasets. The goal is to showcase how to effectively handle, analyze, and visualize data in a scientific context.

## Naming Convention

This project follows a specific naming convention for files and directories to ensure clarity and consistency. The naming convention is as follows:

\`<type>\_<id>\[_state]\_<descriptive name>\[_version]\_<timestamp>.<file\_extension>\`
    - type: The type of the file, two letter abbreviation, e.g., `ds` for datasets, "md" for metadata, `vi` for visualizations, `dc` for data cleaning scripts, `az` for analysis scripts, `am` for animations.
    - id: A unique identifier for the project/analysis/task the file is associated with, e.g., `1`.
    - state: The state of the file, important for data and visualizations, not so much for scripts, e.g., `raw`, `cleaned`, `filtered`, `merged`.
    - descriptive name: A short, descriptive name for the dataset content, e.g., `gdp_pcap`, `population_growth`.
    - version: Optional version number, e.g., `v1`, `v2.3`.
    - timestamp: The date of creation or last modification in ISO format, for scripts including time, e.g., '2025-07-19', `2025-07-19T12:00:00`.
    - file extension: The file type, e.g., `.csv`, `.png`, `.py`.

ID index:
| ID | Description |
|----|-------------|
| 1  | Fertility rate over  womans educational attainment combined with population and world region |
| 2  | Fertility rate over gender ratio mean years in school combined with population and GDP per capita |

## File Structure

- **Project Root**: The root directory contains the main README file, a requirements file, and a conda environment file and a LICENSE file.
- **Requirements**: The `requirements.txt` file lists all the Python packages required for this project.
- **Conda Environment**: The `environment.yml` file contains the conda environment configuration for this project.
-  **Data**: The `data` directory contains all datasets used in the project. It is organized into subdirectories based on the data state and source.
- **Scripts**: The `scripts` directory contains all Python scripts used in the project, including analysis, and visualization scripts.
- **Notebooks**: The `notebooks` directory contains Jupyter notebooks used for data exploration, cleaning and analysis.
- **Visualizations**: The `visualizations` directory contains all visualizations generated from the datasets.

## Metadata

Metadata is collected for all (raw and filtered) datasets in the `data` directory.
For the visualizations, metadata is collected in the `visualizations` directory.
For the scripts metadata is collected implicitly through comments and docstrings within the scripts themselves. For a larger project, it might be useful to create a separate metadata file for the scripts as well.

## Installation
To get started with this project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://git.uni-jena.de/sonjaweitzing/mosd.git
   ```
   cd mosd
   ```

2. **Create a new virtual environment and install dependencies:**
   - Using **conda**:
     ```bash
     conda create --name mosd_env --file requirements.txt
     conda activate mosd_env
     ```
   - Using **pip**:
     ```bash
     python3 -m venv mosd_env
     source mosd_env/bin/activate
     pip install -r requirements.txt
     ```

3. **Run the scripts:**
   ```bash
   python scripts/vi_1_bubbles-ds-1_2025-07-21.py
   ```
4. **Open Jupyter Notebook:**
   ```bash
    jupyter notebook
    ```

## License
This Project is licensed under the CC-BY-4.0 license. See the [LICENSE](LICENSE) file for details.
Analysis and Visualization is based on free material from GAPMINDER.ORG, CC-BY LICENSE and UN, World Population Prospects (2024) – processed by Our World in Data. “Fertility rate, total – UN WPP” [dataset]. United Nations, “World Population Prospects” [original data].

