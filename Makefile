BASE_PYTHON ?= $(shell which python)
VENV := $(PWD)/.virtualenv

PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
PEP8 := $(VENV)/bin/pep8
NOSE := $(VENV)/bin/nosetests

dev-install: init
	$(PYTHON) setup.py develop

init: $(VENV)

$(VENV):
	virtualenv --no-site-packages --python=$(BASE_PYTHON) $(VENV)

tests: dev-install
	$(NOSE) ./tests/

pyc:
	find . -name "*.pyc" ! -path "./.virtualenv/*" -delete

clean: pyc
	-rm -rf ./.virtualenv
	-rm -rf *.egg-info

.PHONY: clean pyc tests

