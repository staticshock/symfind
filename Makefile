SHELL := /bin/bash

all:
	python setup.py sdist

install:
	pip install --upgrade dist/symfind-*.tar.gz

clean:
	rm -rf ./dist ./index MANIFEST symfind.pyc
