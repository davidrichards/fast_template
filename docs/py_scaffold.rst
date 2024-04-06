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

The longer description tends to be a good moment for humane coding: take some time to think through what you're doing and why. What it's doing is creating an arch in your mind that makes it easier to get ready for coding sessions. Cold starts are rough on the mind and nerves.

I like to add:

* Developer installation instructions
* Testing instructions
* Usage instructions with links to the documentation
* Basic roadmap of the project

-----------
Setup Tools
-----------

You'll want to update the setup.cfg.

* Copy the short description from the README.md into the description field.
* Update the url to point to the Github project.

I tend to update as many of the supporting systems that use Github. I don't tend to set up other systems yet. That may be a laziness that I need to address. I don't tend to update anything after the project_urls.

The setup.py should just work. Note: it uses the git tags for the version. To add a tag:

    git tag -a v0.1 -m "First release"
    git push --tags

Tox uses the setup tools to run the tests. Knowing that these work is a good sign that you'll be comfortable making incremental updates later.

---------------
Version Control
---------------

I use git and Github. I create the project in Github as I create the project locally. I've noticed that the smaller my commitments, the lower my anxiety. I'll commit many times during the setup process.

-------
tox.ini
-------

I tend to add a requirements.txt file and a dependency on it in the tox.ini. This is a good time to add the requirements.txt file.

    pip freeze > requirements.txt

This is often too many requirements. I prune the file to ensure that only the main requirements are in there. This is because I also add a depency on the requirements.txt file in the tox.ini. I add these lines inside of the `[testenv]` section:

.. code-block:: ini

    [testenv]
    deps =
        -r {toxinidir}/requirements.txt

This is a good time to run tox. If it fails, the failing tests should guide you in the the next steps. Once a developer learns to invite failing tests, the anxiety levels around code improvements drop.

The PyScaffold project builds a skeleton CLI file with some fairly good tests. I appreciate the test coverage stats that are configured to work with Tox out of the box. This reminds me of any unfinished work, especially when I work backwards and write code before writing failing tests. (If you've never tried it, give it a shot, notice that the first version of your code tends to be a little simpler and easier to test.)

----------------------------------------------
CONTRIBUTING.rst, AUTHORS.rst, and LICENSE.rst
----------------------------------------------

Spend some time in these files. When I'm not in a rush, I can spend about an hour thinking about how to collaborate with others. Most of the work is in CONTRIBUTING.rst.

------
Sphinx
------

PyScaffold sets up Sphinx in the `docs` directory. You can build the documentation with:

    tox -e docs

This is a good time to write some documentation.

One thing that's difficult for me is to remember all of the ways rst links to other files. Here is a short reminder of the top things you want to know:

* `:ref:` is for references to other files. For example: `:ref:`README.rst` is the README file.`
* `:doc:` is for references to other files
* `:class:` is for references to classes
* `:func:` is for references to functions
* `:mod:` is for references to modules
* `:attr:` is for references to attributes

To read the documents:

    open docs/_build/html/index.html

Sphinx can also be used to build other types of documentation. See the Sphinx documentation for more information.

https://sphinx-tutorial.readthedocs.io/cheatsheet/