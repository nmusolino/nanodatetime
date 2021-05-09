========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        | |coveralls| |codecov|
        | |scrutinizer| |codacy|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/nanodatetime/badge/?style=flat
    :target: https://nanodatetime.readthedocs.io/
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.com/nmusolino/nanodatetime.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/nmusolino/nanodatetime

.. |coveralls| image:: https://coveralls.io/repos/nmusolino/nanodatetime/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/nmusolino/nanodatetime

.. |codecov| image:: https://codecov.io/gh/nmusolino/nanodatetime/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/nmusolino/nanodatetime

.. |codacy| image:: https://img.shields.io/codacy/grade/[Get ID from https://app.codacy.com/gh/nmusolino/nanodatetime/settings].svg
    :target: https://www.codacy.com/app/nmusolino/nanodatetime
    :alt: Codacy Code Quality Status

.. |version| image:: https://img.shields.io/pypi/v/nanodatetime.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/nanodatetime

.. |wheel| image:: https://img.shields.io/pypi/wheel/nanodatetime.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/nanodatetime

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/nanodatetime.svg
    :alt: Supported versions
    :target: https://pypi.org/project/nanodatetime

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/nanodatetime.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/nanodatetime

.. |commits-since| image:: https://img.shields.io/github/commits-since/nmusolino/nanodatetime/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/nmusolino/nanodatetime/compare/v0.0.0...master


.. |scrutinizer| image:: https://img.shields.io/scrutinizer/quality/g/nmusolino/nanodatetime/master.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/nmusolino/nanodatetime/


.. end-badges

Datetime library with nanosecond resolution

* Free software: GNU Lesser General Public License v3 (LGPLv3)

Installation
============

::

    pip install nanodatetime

You can also install the in-development version with::

    pip install https://github.com/nmusolino/nanodatetime/archive/master.zip


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
