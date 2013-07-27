Symfind
=======

``symfind`` lists undefined symbols in shared libraries and executables, and
tracks down which linked library defines each. It's a thin wrapper around
existing gnu tools.

Installation
------------
::

  python setup.py sdist
  pip install dist/symfind-*.tar.gz

Usage
-----

::

  symfind <file>
