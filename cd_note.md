# Workflow for all

## Initial Setup

1. Read the [Install.md](https://github.com/alshedivat/al-folio/blob/master/INSTALL.md) file.
2. Follow the [Recommended Approach](https://github.com/alshedivat/al-folio/blob/master/INSTALL.md#recommended-approach) to set up the *al-folio* template.

## Local Setup

0. **Before starting the local setup**, ensure the following applications are installed in WSL (for Windows users):
    - Git
    - [docker](https://docs.docker.com/get-started/get-docker/)
    - [docker-compose](https://docs.docker.com/compose/install/)
    > The Jekyll and Ruby dependencies can be installed by using Docker. No need to install manually.
1. After completing the initial setup, use the **WSL Linux (Ubuntu) terminal** to clone the repository:
    ```shell
    git clone https://github.com/ChenDdon/chenddon.github.io.git
    ```
2. Open the `_config.yml` file with VS Code. The editor will prompt you to install the necessary extensions and automatically configure everything required. (This is the way that **Local Setup with Development Containers**.)
3. Check the `PORTS` window at the bottom of VS Code. In the `PORTS` panel, port 8080 should be available to preview the website. You can view the website at `http://localhost:8080/`.

## Updating and Deployment

0. Ensure the **Initial Setup** is completed successfully.
1. Work on the `master` or `main` branch. (There is no need to update the `gh-pages` branch.) Push your changes as usual:
    ```shell
    git add .
    git commit -m 'your_change_note'
    git push origin master or main
    ```