PYVENV ?= $(shell which pyvenv)
VENV := $(PWD)/.env

PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
PEP8 := $(VENV)/bin/pep8
NOSE := $(VENV)/bin/nosetests

all: init

dev-install: init
	$(PYTHON) setup.py develop

init: $(VENV)

$(VENV):
	$(PYVENV) $(VENV)

tests: dev-install
	$(NOSE) ./tests/

pyc:
	find . -name "*.pyc" ! -path "./.virtualenv/*" -delete

clean: pyc
	-rm -rf ./.virtualenv
	-rm -rf *.egg-info

.PHONY: clean pyc tests

