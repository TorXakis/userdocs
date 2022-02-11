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
exclude_patterns = []

pygments_style = "solarized-light"
#pygments_style = "solarized-dark"
#pygments_style = "colorful"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']







# -- ADDED ---------------------------------------------------


# -- Setup code size in pdf output--------------------------------------------

# https://stackoverflow.com/questions/9899283/how-do-you-change-the-code-example-font-size-in-latex-pdf-output-with-sphinx
# => choose size from: https://en.wikibooks.org/wiki/LaTeX/Fonts#Built-in_sizes
from sphinx.highlighting import PygmentsBridge
from pygments.formatters.latex import LatexFormatter

class CustomLatexFormatter(LatexFormatter):
    def __init__(self, **options):
        super(CustomLatexFormatter, self).__init__(**options)
        self.verboptions = r"formatcom=\scriptsize"

PygmentsBridge.latex_formatter = CustomLatexFormatter



# note: do NOT use 'sphinx.ext.autosectionlabel' because makes it difficult to change section labels because
#       when you change the label you also have to relabel all references referring that section.
#       Instead explicitly define a target for a section we want to refer to. Has the following advantages:
#        - can change section label independent of references
#        - can quickly see whether a section is referenced by the definition of a target.

extensions = [ 'sphinxcontrib.textcolor', 'sphinxcontrib.igrammar']

#extensions = [ 'sphinx.ext.autosectionlabel' , 'helloworld', 'todo', 'recipe', 'sphinxcontrib.textcolor', 'sphinxcontrib.igrammar']
               # 'sphinx.ext.coverage', 'sphinx.ext.doctest',
               # 'pyspecific', 'c_annotations', 'escape4chm']

todo_include_todos = True







# -- Load Continuous publishing configuration ---------------------------------------------------

includefile='continuous_publishing.py'
exec(compile(source=open(includefile).read(), filename=includefile, mode='exec'))


