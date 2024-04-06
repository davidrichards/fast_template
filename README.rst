.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/davidrichards/fast_tutorial.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/davidrichards/fast_tutorial
    .. image:: https://readthedocs.org/projects/fast_tutorial/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://fast_tutorial.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/davidrichards/fast_tutorial/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/davidrichards/fast_tutorial
    .. image:: https://img.shields.io/pypi/v/fast_tutorial.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/fast_tutorial/
    .. image:: https://img.shields.io/conda/vn/conda-forge/fast_tutorial.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/fast_tutorial
    .. image:: https://pepy.tech/badge/fast_tutorial/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/fast_tutorial
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/fast_tutorial

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

=============
fast_tutorial
=============


    Build a FastAPI application using conventional Python and layered architecture.


There are a lot of resources I've used to get my projects running:

* Docker containers: start with deployment in mind.
* Tests: always a good idea to test-drive anything.
* Sphinx: for documentation.
* Tox: for testing, building, deploying, and more.
* Makefile and local scripts: for running common tasks.
* Layered architecture: for keeping the code testable and maintainable.

If I can remember what the standard way to use these are, that would be wonderful. Since I can't, I wrote a tutorial to learn the material more deeply and leave a reference for later.

Project Setup
-------------

To get started, you'll need to clone the respository:

.. code-block:: bash

    git clone git@github.com:davidrichards/fast_template.git

Then, you'll need to install the dependencies. I like to do this in a conda environment, because I work with an M1 Mac.

.. code-block:: bash

    conda create -n fast_tutorial python=3.9
    conda activate fast_tutorial
    pip install -r requirements.txt 

At this point, you should be able to run the tests:

.. code-block:: bash

    tox

If the tests pass, you're ready to start the server:

.. code-block:: bash

    make run

In our case, we have two containers running: one for the FastAPI application and one for the database. The FastAPI application is running on port 8000, and the database is running on port 5432.

Because this is a tutorial repository, I will show you how to do this for your own projects.

.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.
