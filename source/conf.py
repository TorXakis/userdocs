# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

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
# extensions = [
#     'sphinx.ext.autosectionlabel'
# ]

import sys,os
sys.path.append(os.path.abspath('tools/extensions'))

extensions = [ 'sphinx.ext.autosectionlabel' ]
               # 'sphinx.ext.coverage', 'sphinx.ext.doctest',
               # 'pyspecific', 'c_annotations', 'escape4chm']

# By default  (for literal block (::) AND '.. code-block::'  AND  '.. literalinclude:: FILE'  (latter has :language: option to set specific language )
# - highlight as Python 3.
#highlight_language = 'python3'
# - no highlighting
highlight_language = 'none'
# no implicit highlighting, it must be explicitly set!!
# => use literal blocks only for none-highlighted text, and  'code-block' for explicitly highlighted text    ( never use  '.. highlight: LANGUAGE" directive)

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# internal linking  :ref:linkname
# using :ref: we can use sphinx cross referencing in a sphinx document (between possible different rst files in sphinx project)
# however :ref: is only used for internal linking,
#
# external linking   linkname_
# for external linking you must use the standard restructured text
# syntax using a role with an ending _ character. You can even separate the link and the target definition.
# However the  target definition from standard restructured text only holds for the current rst file.
#                                                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# The trick to have target definitions hold for all rst files in the sphinx project is to include to each
# rst file the target definitions. We do this by adding an include directive for including hyperlinks.rst
# to the rst_epilog, so that hyperlinks.rst is then automatically include to rst file.
#
rst_epilog="""
.. include:: /epilog.rst
"""
# note: officially include directive only supports a relative file argument
#      https://docutils.sourceforge.io/docs/ref/rst/directives.html#including-an-external-document-fragment
#        The "include" directive reads a text file. The directive argument is the path to the file to be included,
#        relative to the document containing the directive.Unless the options literal, code, or parser are given,
#        the file is parsed in the current document's context at the point of the directive.
# however https://stackoverflow.com/questions/44563794/how-to-correctly-include-other-rest-files-in-a-sphinx-project
#      said an absolute path ( root is source/ dir) works also and I verified it!


# rst_prolog="""
# .. include:: /prolog.rst
# """

numfig = True

# -- Options for HTML output -------------------------------------------------

html_favicon = 'favicon.ico'

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
