symfind
=======

``symfind`` lists undefined symbols in shared libraries and executables, and
tracks down which linked library defines each. It's a thin wrapper around
existing gnu tools.

Installation
============

It's not in the package index, but the cleanest install is still through pip::

  git clone git://github.com/staticshock/symfind.git
  cd symfind
  python setup.py sdist
  makeindex dist/*  # pip install basketweaver if you don't have this
  pip install -i file://$(realpath ./index) symfind

Usage
=====

::

  symfind <file>

TODO
====
* --color=auto
* -r, --recursive
