SHELL := /bin/bash

index:
	python setup.py sdist
	makeindex dist/*

clean:
	rm -rf ./dist ./index MANIFEST symfind.pyc

install:
	pip install -i file://$(realpath ./index) --upgrade symfind
