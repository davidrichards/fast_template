==========
PyScaffold
==========

Using PyScaffold to create a new Python project is as easy as running::

    putup my_project

However, there are quite a few things you'll want to configure after your project is setup. Generally:

* README.rst for the project overview
* setuptools configuration in setup.py
* version control with git and Github
* tox.ini for testing
* CONTRIBUTING.rst, AUTORS.rst and LICENSE.rst for community
* docs for the coder first, the user later

Additionally, you may want to add:

* requirements.txt and a dependency on it in tox.ini
* Makefile, in case you want to use make

Let's take these one at a time.

----------
README.rst
----------

At the top of the generated file are a some badges. If you want to leave them commented out, but update the `<USER>` placeholder, they'll be ready for use.

You're going to want to write a short description. What I like to do is write this, then change the Github project description to match. It's one less thing to bug me later if I forget. Notice how the short description is indented. That's for formatting reasons.

