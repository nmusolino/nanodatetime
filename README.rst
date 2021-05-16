========
Overview
========

Datetime library with nanosecond resolution.

* Free software: GNU Lesser General Public License v3 (LGPLv3)

.. image:: https://github.com/nmusolino/nanodatetime/actions/workflows/python-test.yml/badge.svg?event=push
    :target: https://github.com/nmusolino/nanodatetime/actions/workflows/python-test.yml?query=branch%3Amain


Documentation
=============


https://nanodatetime.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
