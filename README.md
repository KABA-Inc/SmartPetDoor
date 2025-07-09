# SmartPetDoor

## Common

For backend and frontend developing I'd suggest to use Linux because it is much faster and easier to install and use the tools we will use, for example [pre-commit](https://pre-commit.com/).
Before starting developing please run `make init` which will install all of the useful tools that we will use.

## Backend

[FastAPI](https://fastapi.tiangolo.com/) supports **Python 3.13**, so please make sure to install that.

- Windows: https://www.python.org/downloads/
- Linux: https://ubuntuhandbook.org/index.php/2024/02/install-python-3-13-ubuntu/

After you have installed **Python 3.13** do the following bootstrap steps:

1. Create a virtual environment: `make venv`
2. Activate virtual environemt: `source backend/.venv/bin/activate`
3. Install all basic tools: `make init`
