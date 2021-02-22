pywraps
#######

.. .. |PyPI-Status| |Downloads| |PyPI-Versions| |Build-Status| |Codecov| |Codefactor| |LICENCE|

Some useful wrapping approaches for Python classes and objects.


.. code-block:: python

  from pywraps import NullWrapper

.. contents::

.. section-numbering::


Installation
============

.. code-block:: bash

  pip install pywraps

Contributing
============

Package author and current maintainer is `Shay Palachy <http://www.shaypalachy.com/>`_ (shay.palachy@gmail.com); You are more than welcome to approach him for help. Contributions are very welcomed.

Installing for development
----------------------------

Clone:

.. code-block:: bash

  git clone git@github.com:shaypal5/pywraps.git


Install in development mode, including test dependencies:

.. code-block:: bash

  cd pywraps
  pip install -e '.[test]'


Running the tests
-----------------

To run the tests use:

.. code-block:: bash

  cd pywraps
  pytest


Adding documentation
--------------------

The project is documented using the `numpy docstring conventions`_, which were chosen as they are perhaps the most widely-spread conventions that are both supported by common tools such as Sphinx and result in human-readable docstrings. When documenting code you add to this project, follow `these conventions`_.

.. _`numpy docstring conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
.. _`these conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt

Additionally, if you update this ``README.rst`` file,  use ``python setup.py checkdocs`` to validate it compiles.


.. |PyPI-Status| image:: https://img.shields.io/pypi/v/pywraps.svg
  :target: https://pypi.python.org/pypi/pywraps

.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/pywraps.svg
   :target: https://pypi.python.org/pypi/pywraps

.. |Build-Status| image:: https://travis-ci.org/shaypal5/pywraps.svg?branch=master
   :target: https://travis-ci.org/shaypal5/pywraps

.. |LICENCE| image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://github.com/shaypal5/pywraps/blob/master/LICENSE

.. |Codecov| image:: https://codecov.io/github/shaypal5/pywraps/coverage.svg?branch=master
   :target: https://codecov.io/github/shaypal5/pywraps?branch=master

.. |Codacy| image:: https://api.codacy.com/project/badge/Grade/99e79faee7454a13a0e60219c32015ae
   :alt: Codacy Badge
   :target: https://app.codacy.com/app/shaypal5/pywraps?utm_source=github.com&utm_medium=referral&utm_content=shaypal5/pywraps&utm_campaign=Badge_Grade_Dashboard

.. |Requirements| image:: https://requires.io/github/shaypal5/pywraps/requirements.svg?branch=master
   :target: https://requires.io/github/shaypal5/pywraps/requirements/?branch=master
   :alt: Requirements Status

.. |Codefactor| image:: https://www.codefactor.io/repository/github/shaypal5/pywraps/badge?style=plastic
   :target: https://www.codefactor.io/repository/github/shaypal5/pywraps
   :alt: Codefactor code quality

.. |Downloads| image:: https://pepy.tech/badge/pywraps
   :target: https://pepy.tech/project/pywraps
   :alt: PePy stats

.. .. test pypi
