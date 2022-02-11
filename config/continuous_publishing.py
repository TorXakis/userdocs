
# ----------------------------------------------------------------------------
#   Configuration for Continuous Publishing 
# ----------------------------------------------------------------------------


# -- manual configuration  -----------------------------------------------------

github_user_or_organisation='torxakis'
github_repo_name="userdocs"

# when publishing documentation as file assets on github use following filename:
document_name_format="TorXakis-{TOOLVERSION}_Userguide-{DOCVERSION}"
# notes: 
#  - TOOLVERSION and DOCVERSION are template parameters which are filled in later.
#  - TOOLVERSION is set in separate file TOOLVERSION.txt so we only need to change that file as part of the
#    documentation source. This general configuration once set doesn't need changing then. 
#  - DOCVERSION is automatically derived from git from this repository

prefix_for_git_sha1_version="git-sha1-"



# -- website icon -------------------------------------------------

## to add a special icon for the website
## add source/favicon.ico then uncomment next line
#html_favicon = 'favicon.ico'


# -- extra css and javascript  -------------------------------------------

# Add .css files to _static/css/  and .js files to _static/js/ and they will automatically added to html output.
#  -> eg. convenient for defining css styles for custom rst roles

# -- extra latex PREAMBLE --------------------------------------------------------

# Add .tex files to _static/_latex_preamble/ and they will automatically added to the PREAMBLE of your latex output.
#  -> eg. convenient for defining macros in latex for custom rst roles

extra_latex_packages=""
# extra_latex_packages=r"""
# \usepackage{xcolor}
# """

# -- extra rst epilog  --------------------------------------------------------

# Add .rst files to _static/_rst_epilog and they will automatically added to the rst_epilog variable
# which content will be added to every rst file in your source folder.
#  ->  convenient for defining things globally for the project which normally in rst hold only for the rst file
#     eg. for defining reference names with an hyperlink which then can be used globally in the project

# ----------------------------------------------------------------------------
#   DON'T EDIT BELOW
# ----------------------------------------------------------------------------

# -- setup tools folders for easy extending sphinx ----------------

# structure from python docs @ https://github.com/python/cpython/tree/main/Doc
#
#   tools/
#      extensions/   : python code for extensions   # added with : sys.path.append(os.path.abspath('../tools/extensions'))
#      static/       : javascript/css               #              templates_path = ['../tools/templates']
#      templates/    : html templates               #              html_static_path = ['../tools/static']
#
# instead we use paths with stick more to defaults
#
# python
#     CONFIGDIR/_extensions   for extensions
# html
#     CONFIGDIR/_static       for static files such as .css  and .js      (set by default by conf.py)
#     CONFIGDIR/_templates    for html template files                     (set by default by conf.py)
# tex
#     CONFIGDIR/_tex          for latex preamble files whose content is include in the generated latex preamble
#
#  note: CONFIGDIR is by default the source/ dir, but we change the configdir by either
#    - setting environment variable SPHINXOPTS or
#    - setting variable SPHINXOPTS in Makefile



extensions_path='_extensions'

templates_dir = templates_path[0]  # override templates in sphinx theme

static_dir = html_static_path[0]  # gets copied to build/html/_static/
css_dir = static_dir + "/css"
js_dir = static_dir + "/js"

tex_dir =  "_latex_preamble" # start with underscore to be compatible with other resource folders starting with underscore
                  # note: resource folders start with underscore to distinguish them from rst source folders
                  #       when configdir is "source/"

rst_dir = "_rst_epilog"


# add extensions dir to python path
import sys,os
sys.path.append(os.path.abspath(extensions_path))  # by default relative to config dir



# create extra dirs for the different kind of source files for extending current sphinx installation
create_dirs = [ extensions_path, templates_dir, css_dir, js_dir, tex_dir, rst_dir ]
from os import listdir
from os.path import isfile, join
for directory in create_dirs:
    if not os.path.exists(directory):
        os.makedirs(directory)


# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_css_files
# note: paths relative to the html_static_path
#
# html_css_files = [
#     'css/custom.css',
# ]

css_files = [join("css", f) for f in listdir(css_dir) if isfile(join(css_dir, f))]

try: html_css_files
except NameError:
    html_css_files=[]

for css_file in css_files:
    html_css_files.append( css_file)



# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_js_files
# note: paths relative to the html_static_path
#
# html_js_files = [
#     'js/custom.js',
# ]

js_files = [join("js", f) for f in listdir(js_dir) if isfile(join(js_dir, f))]

try: html_js_files
except NameError:
    html_js_files=[]

for js_file in js_files:
    html_js_files.append(js_file)



# https://www.sphinx-doc.org/en/master/latex.html#the-latex-elements-configuration-setting
#
# 'preamble'
#
#     Additional preamble content. One may move all needed macros into some file mystyle.tex.txt of the project
#     source repertory, and get LaTeX to import it at run time:
#
#         'preamble': r'\input{mystyle.tex.txt}',                => IMPORTANT: must have .txt extension otherwise the file included itself will be compiled as tex file!
#
#
#     It is then needed to set appropriately latex_additional_files, for example:
#
#         latex_additional_files = ["mystyle.tex.txt"]

# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-latex_additional_files
# note: paths relative to the configuration directory  (current working directory of this script)
#
# latex_additional_files
#
#     A list of file names, relative to the configuration directory, to copy to the build directory when building
#     LaTeX output. This is useful to copy files that Sphinx doesn’t copy automatically, e.g. if they are referenced
#     in custom LaTeX added in latex_elements. Image files that are referenced in source files (e.g. via .. image::)
#     are copied automatically.
#
#     You have to make sure yourself that the filenames don’t collide with those of any automatically copied files.


tex_directory_with_txt_extension=join("..","build","tex_with_txt_extension")
if not os.path.exists(tex_directory_with_txt_extension):
    os.makedirs(tex_directory_with_txt_extension)

tex_files = [f for f in listdir(tex_dir) if isfile(join(tex_dir, f))]


try: latex_additional_files
except NameError:
    latex_additional_files=[]

from shutil import copyfile
latex_preamble=[]
for tex_file in tex_files:
    txt_file = join(tex_file + ".txt")
    latex_additional_files.append(txt_file)
    include_file=join("..", "tex_with_txt_extension" , txt_file)
    latex_preamble.append('\input{' +  include_file + '}')
    src=join(tex_dir, tex_file)
    dst=join(tex_directory_with_txt_extension,txt_file)
    copyfile(src,dst)

latex_preamble = "\n".join(latex_preamble)


# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-rst_epilog
#
# rst_epilog
#     A string of reStructuredText that will be included at the end of every source file that is read.
#     This is a possible place to add substitutions that should be available in every file (another being rst_prolog).
#     An example:
#
#         rst_epilog = """
#         .. |psf| replace:: Python Software Foundation
#         """

# OLD method:
# rst_epilog="""
# .. include:: /epilog.rst
# """

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

rst_files = [join(rst_dir, f) for f in listdir(rst_dir) if isfile(join(rst_dir, f))]

try: rst_epilog
except NameError:
    rst_epilog=""

for rst_file in rst_files:
    with open(rst_file) as f:
        contents = f.read()
        rst_epilog += contents


# example usage rst_epilog :
#
#     internal linking  :ref:linkname
#     using :ref: we can use sphinx cross referencing in a sphinx document (between possible different rst files in sphinx project)
#     however :ref: is only used for internal linking,
#
#     external linking   linkname_
#     for external linking you must use the standard restructured text
#     syntax using a role with an ending _ character. You can even separate the link and the target definition.
#     However the  target definition from standard restructured text only holds for the current rst file.
#                                                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     The trick to have target definitions hold for all rst files in the sphinx project is to include in each
#     rst file the target definitions using the sphinx rst_epilog config variable.
#
#     We do this by adding an hyperlinks.rst file in the _rst_epilog/  folder where we can include all
#     target definitions which should be available globally in the document.




# -- only explicit highlighting  ---------------------------------------------

highlight_language = 'none'
# no implicit highlighting, it must be explicitly set!!
# => use literal blocks only for none-highlighted text, and  'code-block' for explicitly highlighted text    ( never use  '.. highlight: LANGUAGE" directive)


# --  automatically number  figures, tables and code-block if they have a caption ------------------------------

# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-numfig
#   If true, figures, tables and code-blocks are automatically numbered if they have a caption.
#   The numref role is enabled. Obeyed so far only by HTML and LaTeX builders. Default is False.
numfig = True



# -- Automatic configuration of tool/doc version and  document name/url ------

# NOTE: DOCUMENT_NAME is exported to be used in github actions workflow

# This adds 'toolversion' as variable to sphinx documentation.
# Use in .rst file as |toolversion|
# eg. Documentation for TorXakis version: |toolversion|
with open('../source/TOOLVERSION.txt') as f:
    toolversion = f.readline()
toolversion=toolversion.strip()    

import os,sys
import subprocess
tag=subprocess.check_output(["git","tag", "--points-at","HEAD"],encoding="utf-8").strip()
print("tag="+tag)
if tag:
   print("tag taken")
   release_name=tag
   todo_include_todos=False
   display_edit_on_github=False
   docversion=tag
   html_docversion="stable docs: " + docversion
   pdf_docversion="Document version " + docversion   
else:   
   print("tag not taken")
   release_name="develop"
   todo_include_todos=True
   display_edit_on_github=True
   docversion=subprocess.check_output(["git","rev-parse","--short","HEAD"],encoding="utf-8").strip()
   docversion=prefix_for_git_sha1_version + docversion
   
   ret=subprocess.call(["git","diff","--quiet"])
   if ret == 1:
       docversion=docversion+"+"

   html_docversion="latest docs: " + docversion 
   pdf_docversion="Document version " + docversion   

print("html_docversion="+html_docversion)

# show in left top corner in html build
version="version: " + toolversion + "<br/>" + html_docversion
# show on first page in pdf build
release= toolversion + ", " + pdf_docversion


document_name = document_name_format.format(TOOLVERSION=toolversion,DOCVERSION=docversion)

githubenv=os.environ.get('GITHUB_ENV')
if githubenv:
    print("using GITHUB_ENV\n")
    handle = open(githubenv, 'a') 
else:
    print("NOT using GITHUB_ENV\n")
    handle = sys.stdout

handle.write("DOCUMENT_NAME=" + document_name + "\n")

pdfdocumenturl="https://github.com/{0}/{1}/releases/download/{2}/{3}.pdf".format(github_user_or_organisation,
                github_repo_name,release_name,document_name)


import os
if os.environ.get('GITHUB_ACTIONS'):
   # build on github actions
   # add link to pdf in html theme below version
   version = version + r'<br/><a style="color:white" href="' + pdfdocumenturl + '">pdf</a>'
else:
   # local build    
   pdfdocumenturl="https://for.local.build.no.pdf.is.uploaded"

#document_overview_url="https://{0}.github.io/{1}/".format(github_user_or_organisation,github_repo_name)
document_overview_url="https://github.com/{0}/{1}/releases/".format(github_user_or_organisation,github_repo_name)

print("docversion: " +docversion)        
print("toolversion: " +toolversion)        
print("pdfdocumenturl: " +pdfdocumenturl)        
print("document_overview_url: " +document_overview_url)        

url_and_versions =  '''
.. |TOOLVERSION| replace:: {toolversion}
.. |DOCVERSION| replace:: {docversion}
.. _PDFDOCUMENTURL: {pdfdocumenturl}
.. _DOCUMENT_OVERVIEW_URL: {document_overview_url}
'''.format(toolversion=toolversion,pdfdocumenturl=pdfdocumenturl,docversion=docversion,document_overview_url=document_overview_url)
# see for the hyperref syntax: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#embedded-uris-and-aliases

rst_epilog = rst_epilog + url_and_versions

# -- get the filename of the build pdf (SPHINX_BUILD_PDF) ----------

# NOTE: SPHINX_BUILD_PDF is exported to be used in github actions workflow


def slugify(value, allow_unicode=False):
    """
    Convert to ASCII if 'allow_unicode' is False. Convert spaces to hyphens.
    Remove characters that aren't alphanumerics, underscores, or hyphens.
    Convert to lowercase. Also strip leading and trailing whitespace.
    """
    import unicodedata
    import re
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower()).strip()
    return re.sub(r'[\s]+', '', value)


output_pdf="build/latex/" + slugify(project) + ".pdf"
handle.write("SPHINX_BUILD_PDF=" + output_pdf + "\n")
if githubenv: handle.close() 




# -- Configuration for HTML output -------------------------------------------------

# use sphinx readthedocs theme 
import sphinx_rtd_theme


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

html_theme = "sphinx_rtd_theme"

# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html

html_theme_options = {
#    'canonical_url': '',
#    'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    'logo_only': False,
    'display_version': True,
#    'prev_next_buttons_location': 'bottom',
    'prev_next_buttons_location': 'both',
    'style_external_links': False,
    #'vcs_pageview_mode': 'blob',  => notexisting option
#    'style_nav_header_background': 'blue',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': -1,
    'includehidden': True,
    'titles_only': False
}


# html_context: A dictionary of values to pass into the template engine’s context for all pages.
#  see https://www.sphinx-doc.org/en/master/usage/configuration.html?highlight=html_context#confval-html_context  
#
# edit on github -> set "display_github": True 
#  see: https://github.com/readthedocs/sphinx_rtd_theme/issues/314#issuecomment-244646642-permalink
html_context = {
    # which fields there are see /usr/local/lib/python3.7/site-packages/sphinx_rtd_theme/breadcrumbs.html
    "show_source": False,
    "display_github": display_edit_on_github,
    "github_host": "github.com",
    "github_user": github_user_or_organisation,
    "github_repo": github_repo_name,
    "github_version": "main",
    "conf_py_path": "/source/",
    "source_suffix": '.rst',
}




# -- Configuration for Latex/PDF output -------------------------------------------------



# higher toc depth in latex bookmarks
#  see: https://www.sphinx-doc.org/en/master/latex.html#latex-elements-confval
latex_elements = {
 'papersize': 'a4paper',
 'sphinxsetup': 'verbatimwithframe=true, VerbatimColor={rgb}{0.992,0.964,0.890}',
 'extrapackages' : extra_latex_packages,  # Default: ''
 'preamble': r'''

%% use tocdepth to increase depth of bookmarks in pdf, see: https://github.com/sphinx-doc/sphinx/issues/2547
\setcounter{tocdepth}{9}

%% src: https://en.wikibooks.org/wiki/LaTeX/Hyperlinks
%% option for hyperref package to number bookmarks in pdf:
\hypersetup{bookmarksnumbered}

''' + latex_preamble
}





