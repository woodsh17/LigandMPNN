# Contributors Guide
Thank you for your interest in contributing to the Rosetta Commons-supported RosettaMPNN repository. 

## Code Contributors

## Documentation Contributors
All files used to create the documentation can be found in the `docs/source` directory. [Sphinx](https://www.sphinx-doc.org/en/master/#) is used to generate the static HTML pages which are then hosted by GitHub pages. Any pull request, push, or woskflow dispatch will trigger the GitHub page to update via GitHub Actions. 

Similar to contributing to the code you can suggest documetnation changes in two ways: 
- Clone the repository and then make changes in your own branch. You can then push your branch to the main repository and create a pull reqest to merge it with the main branch. *This is recommended for those with write access to the repository.*
- Fork the repository, push your changes to your fork, and then create a pull reqest to merge the fork when you are ready. *This is recommended for those who would like to contribute to the project, but do not have direct write access.*
You must be a member of the Rosetta Commons GitHub organization to have write access to Rosetta Commons-supporte repositories. Reach out to [Colin Smith](mailto:colin.smith@wesleyan.edu), the Rosetta Commons Membership Chair, to learn more about becoming a member. 

The files with `.md` extensions are written in [MarkDown](https://www.markdownguide.org/cheat-sheet/) and those with `.rst` extensions are written using [reStructuredText](https://sphinx-tutorial.readthedocs.io/cheatsheet/). 

Any new files should go into the `source` directory, or any relevant subdirectory. Make sure this file gets added to `docs/source/index.rst` so that it shows up in the table of contents and so that Sphinx knows to generate a static HTML page for it. 

To see your documentation updates before you create a pull request: 
1. *(Optional)* It is recommended to create a different conda environment for the docs, in case any of the dependencies interfere with running LigandMPNN:
    ```
    conda create -n ligandmpnn_docs_env
    ```
1. Make sure you have:
    - [Sphinx](https://www.sphinx-doc.org/en/master/usage/installation.html)
    - [MyST](https://myst-parser.readthedocs.io/en/latest/intro.html)
    - the [furo](https://pradyunsg.me/furo/) template (`pip install furo`)

1. `cd RosettaMPNN/docs`
1. `make html`
1. `open build/html/index.html` - this will open the static HTML page in your default browser

Upon the creation of a pull reqest, all files will be reviewd to ensure that their style and content is appropriate. 