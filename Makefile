.PHONY: setup run clean

VENV_DIR := .venv
PYTHON := $(VENV_DIR)\Scripts\python
UV := $(VENV_DIR)\Scripts\uv

setup:
	@if not exist $(VENV_DIR) (		\
		echo Creating virtual environment...	\
		uv venv $(VENV_DIR)			\
	)
	@echo Installing dependencies from pyproject.toml...
	@$(UV) pip install -e .

run: setup
	@echo Starting the project...
	@$(PYTHON) src\myproject\main.py

clean:
	@if exist $(VENV_DIR) (			\
		echo Removing virtual environment...	\
		rmdir /s /q $(VENV_DIR)		\
	)
