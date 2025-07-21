# MoSD

This Repository contains the source code of my data management project for the final exam in the Management of Scientific Data course at the University of Jena.

## TODO

Update this README

create metadata eg dublin core generator: https://nsteffel.github.io/dublin_core_generator/generator_nq.html

create naming convention

credit datasets correctly (see readme etc)

END: 
Update requirements.txt
conda list --export > requirements.txt


Create JSON metadata

Get conda environment file - add jupyter notebook to environment!



## Contents- [MoSD](#mosd)
  - [Contents](#contents)
  - [Project description](#project-description)
  - [Getting started](#getting-started)
    - [Create your project](#create-your-project)
    - [Add your files](#add-your-files)
    - [Integrate with your tools](#integrate-with-your-tools)
    - [Collaborate with your team](#collaborate-with-your-team)
    - [Test and Deploy](#test-and-deploy)

## Datasets

I chose to use the xx and the yy datasets for my project. The xx dataset contains information about the xx, while the yy dataset contains information about the yy. Both datasets are available in the [data](data) directory of this repository.

https://www.gapminder.org/data/
https://ourworldindata.org/grapher/womens-educational-attainment-vs-fertility

## Research question

How does female eduacation and participation in the labor market change societal structures and economic development in different countries?

## Project description

This project aims to demonstrate the management of scientific data using the xx and yy datasets. The goal is to showcase how to effectively handle, analyze, and visualize data in a scientific context.

## Naming Convention

This project follows a specific naming convention for files and directories to ensure clarity and consistency. The naming convention is as follows:

<type>_<id>[_state]_<descriptive name>[_version]_<timestamp>.<file_extension>

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

- **Project Root**: The root directory contains the main README file, a requirements file, and a conda environment file.
- **Requirements**: The `requirements.txt` file lists all the Python packages required for this project. It can be generated using the command `conda list --export > requirements.txt`.
- **Conda Environment**: The `environment.yml` file contains the conda environment configuration for this project. It can be created using the command `conda env export > environment.yml`.
- **Project Metadata**: The `project_metadata.json` file contains metadata about the project, including the project title, description, author, and date of creation. This file should be updated with relevant information about the project.
-  **Data**: The `data` directory contains all datasets used in the project. It is organized into subdirectories based on the data state and source.
- **Scripts**: The `scripts` directory contains all Python scripts used in the project, including analysis, and visualization scripts.
- **Notebooks**: The `notebooks` directory contains Jupyter notebooks used for data exploration, cleaning and analysis.
- **Visualizations**: The `visualizations` directory contains all visualizations generated from the datasets.


## Metadata

Metadata is collected for all (raw and filtered) datasets in the `data` directory.
For the visualizations, metadata is collected in the `visualizations` directory.
For the scripts metadata is collected implicitly through comments and docstrings within the scripts themselves. For a larger project, it might be useful to create a separate metadata file for the scripts as well.

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/topics/git/add_files/#add-files-to-a-git-repository) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://git.uni-jena.de/sonjaweitzing/mosd.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://git.uni-jena.de/sonjaweitzing/mosd/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Set auto-merge](https://docs.gitlab.com/user/project/merge_requests/auto_merge/)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing (SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thanks to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README

Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
