# SmartPetDoor

## Common

For backend and frontend developing I'd suggest to use Linux because it is much faster and easier to install and use the tools we will use, for example [pre-commit](https://pre-commit.com/).
Before starting developing please run `make init` which will install all of the useful tools that we will use.

## Backend

For Backend developing we are using a docker compose environment which contains all of the dependencies. To start developing please start the dev environment with `make up`.
After the environment started the backend will be available at `http://localhost:8000`, documentation is available at `http://localhost:8000/docs`.

For some reason sometime backend starts faster than DB - even I set up dependency for these services - in this case backend crashes. Run `make up` again and it will work.

If you add a new dependencie to **requirements.txt** run `make up-build` to install them inside containers.

### Live edit

To make life easier a Live Codeing environment is created, which means when you edit the source code after a save it will be automatically reloaded within the container. So you do not need to install any dependencies on your computer, everything is running within containers.

### Pre-commit

Pretty please install pre-commit before you start developing with `make init` to have a well linted, formatted codebase.

### Branching

#### main branch

The meeting point between HW and SW code changes.

#### dev/backend branch

The meeting point for features. When features are done this is where you should target the PR.
When a group of features are ready target the main branch with a PR.

#### feature/<short-feature-description> branch

These branches are created from `dev/backend` branch. In these branches smaller features are developed.
When feature is ready target the `dev/backend` branch with a PR.
