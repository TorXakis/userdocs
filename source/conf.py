# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'TorXakis'
copyright = '2020, TorXakis'
author = 'TorXakis'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# using :ref: we can use sphinx cross referencing in a sphinx document (between possible different rst files in sphinx project)
# however :ref: is only used for internal linking, for external linking you must use the standard restructured text
# syntax using a role with an ending _ character. You can even separate the link and the target definition.
# However the  target definition from standard restructured text only holds for the current rst file.
# The trick to have target definitions hold for all rst files in the sphinx project is to include to each
# rst file the target definitions. We do this by adding an include directive for including hyperlinks.rst
# to the rst_epilog, so that hyperlinks.rst is then automatically include to rst file.
rst_epilog="""
.. include:: hyperlinks.rst
"""


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Load Continuous publishing configuration ---------------------------------------------------

includefile='continuous_publishing.py'
exec(compile(source=open(includefile).read(), filename=includefile, mode='exec'))
