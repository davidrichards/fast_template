=============
fast_tutorial
=============

This project is a training project, where I want to learn how I develop FastAPI projects. I have been taking other classes, reading PEPs, trying some things out for myself. There were too many questions, and I was taking too long to finish basic tasks because this didn't exist in one place.

What you can expect from this project:

* Training on structuring a project so that new features require linear effort. even when the project gets large.
* Examples of test-driven practices that work well with Docker and the various levels of the system.
* Discussion around the supporting systems, like tox, Docker, Sphinx, diagrams, and automation scripts.
* Links to the PEPs involved, why they are important, and how to maintain a consistent system.
* Demonstration of architectural integrity, or how to develop in layers so that the system remains testable.
* Ideas about developing in cycles, being kind to your mind as you take these things on.

At some point, I'll wrap these lessons into a Feed and provide an interactive tutorial based on what I'm learning here. 


.. note::

    This is the main page of your project's `Sphinx`_ documentation.
    It is formatted in `reStructuredText`_. Add additional pages
    by creating rst-files in ``docs`` and adding them to the `toctree`_ below.
    Use then `references`_ in order to link them from this page, e.g.
    :ref:`authors` and :ref:`changes`.

    It is also possible to refer to the documentation of other Python packages
    with the `Python domain syntax`_. By default you can reference the
    documentation of `Sphinx`_, `Python`_, `NumPy`_, `SciPy`_, `matplotlib`_,
    `Pandas`_, `Scikit-Learn`_. You can add more by extending the
    ``intersphinx_mapping`` in your Sphinx's ``conf.py``.

    The pretty useful extension `autodoc`_ is activated by default and lets
    you include documentation from docstrings. Docstrings can be written in
    `Google style`_ (recommended!), `NumPy style`_ and `classical style`_.


Contents
========

.. toctree::
   :maxdepth: 2

   Overview <readme>
   Contributions & Help <contributing>
   License <license>
   Authors <authors>
   Changelog <changelog>
   Module Reference <api/modules>
   Questions <questions>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _toctree: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html
.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _references: https://www.sphinx-doc.org/en/stable/markup/inline.html
.. _Python domain syntax: https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-python-domain
.. _Sphinx: https://www.sphinx-doc.org/
.. _Python: https://docs.python.org/
.. _Numpy: https://numpy.org/doc/stable
.. _SciPy: https://docs.scipy.org/doc/scipy/reference/
.. _matplotlib: https://matplotlib.org/contents.html#
.. _Pandas: https://pandas.pydata.org/pandas-docs/stable
.. _Scikit-Learn: https://scikit-learn.org/stable
.. _autodoc: https://www.sphinx-doc.org/en/master/ext/autodoc.html
.. _Google style: https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
.. _NumPy style: https://numpydoc.readthedocs.io/en/latest/format.html
.. _classical style: https://www.sphinx-doc.org/en/master/domains.html#info-field-lists
