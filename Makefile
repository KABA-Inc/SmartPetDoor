.PHONY: help
help: ## Show this help message with available targets and descriptions.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: init
init: ## Installs basic tools in order to make development efficient and uniform.
	pip install pre-commit && \
	pre-commit install && \
	make run-pre-commit-all

.PHONY: run-pre-commit-all
run-pre-commit-all: ## Runs installed hooks on all files.
	pre-commit run --all-files

.PHONY: venv
venv: ## Creates virtual environment for backend.
	python -m venv backend/.venv

.PHONY: backend-packages
backend-packages: ## Installs all python packages that the backend needs.
	pip install -r backend/requirements.txt

.PHONY: backend-run
backend-run: ## Starts the backend as a basic process/code.
	fastapi dev backend/app.py \
		--host 0.0.0.0 \
		--port 8000
