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
- **Datasets**: All datasets are stored in the `datasets` directory. Each dataset file should be named descriptively, e.g., `dataset_name.csv`.
- **Scripts**: All scripts are stored in the `scripts` directory. Each script should be named according to its function, e.g., `data_analysis.py`, `data_visualization.py`.

- Short Code for each Dataset: Save cleaned datasets/changed/merged using these codes

    Description of the content
    Project number
    Name of creator
    Name of research team/department associated with the data
    Date of creation; Publication date
    Version number
- **Documentation**: All documentation files are stored in the `docs` directory. Each documentation file should be named according to its content, e.g., `README.md`, `data_description.md`.
- **Images**: All images used in the project are stored in the `images` directory. Each image file should be named descriptively, e.g., `data_visualization.png`.
- **Results**: All results of the analysis are stored in the `results` directory. Each result file should be named according to its content, e.g., `analysis_results.csv`, `visualization_results.png`.
- 



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
