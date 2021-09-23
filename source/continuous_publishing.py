
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


# ----------------------------------------------------------------------------
#   DON'T EDIT BELOW
# ----------------------------------------------------------------------------

# -- Automatic configuration of tool/doc version and  document name/url ------

# NOTE: DOCUMENT_NAME is exported to be used in github actions workflow

# This adds 'toolversion' as variable to sphinx documentation.
# Use in .rst file as |toolversion|
# eg. Documentation for TorXakis version: |toolversion|
with open('TOOLVERSION.txt') as f:
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
try: rst_epilog
except NameError:
  rst_epilog=""
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

#html_show_sourcelink = True

# for adding color roles in html
# -------------------------------
#
# src: https://stackoverflow.com/questions/32033158/create-a-role-font-color-in-sphinx-that-works-with-make-latexpdf#answer-32038624
#    https://www.sphinx-doc.org/en/master/man/sphinx-quickstart.html#cmdoption-sphinx-quickstart-dot
#     Inside the root directory, two more directories will be created; “_templates” for custom HTML templates and “_static” for custom stylesheets and other static files.
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# # Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']
#
# # Add any paths that contain custom static files (such as style sheets) here,
# # relative to this directory. They are copied after the builtin static files,
# # so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# https://stackoverflow.com/questions/32033158/create-a-role-font-color-in-sphinx-that-works-with-make-latexpdf#answer-32038624
#

css_filepath="_static/custom.css"
css_template="""   
@import url("default.css");

.black {
  color: black;
}

.blue {
  color: blue;
}

.brown {
  color: brown;
}

.cyan {
  color: cyan;
}

.darkgray {
  color: darkgray;
}

.gray {
  color: gray;
}

.green {
  color: green;
}

.lightgray {
  color: lightgray;
}

.lime {
  color: lime;
}

.magenta {
  color: magenta;
}

.olive {
  color: olive;
}

.orange {
  color: orange;
}

.pink {
  color: pink;
}

.purple {
  color: purple;
}

.red {
  color: red;
}

.teal {
  color: teal;
}

.violet {
  color: violet;
}

.white {
  color: white;
}

.yellow {
  color: yellow;
}
"""

#  black, blue, brown, cyan, darkgray, gray, green, lightgray, lime, magenta, olive, orange, pink, purple, red, teal, violet, white, yellow

# black blue brown cyan darkgray gray green lightgray lime magenta olive orange pink purple red teal violet white yellow

html_filepath='_templates/layout.html'
html_template="""   
{% extends "!layout.html" %}

{% block extrahead %}
<link rel="stylesheet" type="text/css"
     href="{{ pathto('_static/custom.css', 1) }}" />

{% endblock %}
"""


# script running at PWD=source/
print(os.getcwd())
#for directory in ["source/_static","source/_templates"]:
for directory in ["_static","_templates"]:
    if not os.path.exists(directory):
        os.makedirs(directory)


with open(html_filepath,"w") as f:
   f.write(html_template)

with open(css_filepath,"w") as f:
   f.write(css_template)




# -- Configuration for Latex/PDF output -------------------------------------------------


# higher toc depth in latex bookmarks
#  see: https://www.sphinx-doc.org/en/master/latex.html#latex-elements-confval
latex_elements = {
 'papersize': 'a4paper',
 'preamble': r'''

%% use tocdepth to increase depth of bookmarks in pdf, see: https://github.com/sphinx-doc/sphinx/issues/2547
\setcounter{tocdepth}{9}

%% src: https://en.wikibooks.org/wiki/LaTeX/Hyperlinks
%% option for hyperref package to number bookmarks in pdf:
\hypersetup{bookmarksnumbered}


%% for adding color roles in html 
%% -------------------------------

%%https://en.wikibooks.org/wiki/LaTeX/Colors
\usepackage{xcolor}
%% https://docutils.sourceforge.io/docs/user/latex.html#custom-interpreted-text-roles
%% https://en.wikibooks.org/wiki/LaTeX/Colors#Predefined_colors
%%      black, blue, brown, cyan, darkgray, gray, green, lightgray, lime, magenta, olive, orange, pink, purple, red, teal, violet, white, yellow
\newcommand{\DUroleblack}{\textcolor{black}}
\newcommand{\DUroleblue}{\textcolor{blue}}
\newcommand{\DUrolebrown}{\textcolor{brown}}
\newcommand{\DUrolecyan}{\textcolor{cyan}}
\newcommand{\DUroledarkgray}{\textcolor{darkgray}}
\newcommand{\DUrolegray}{\textcolor{gray}}
\newcommand{\DUrolegreen}{\textcolor{green}}
\newcommand{\DUrolelightgray}{\textcolor{lightgray}}
\newcommand{\DUrolelime}{\textcolor{lime}}
\newcommand{\DUrolemagenta}{\textcolor{magenta}}
\newcommand{\DUroleolive}{\textcolor{olive}}
\newcommand{\DUroleorange}{\textcolor{orange}}
\newcommand{\DUrolepink}{\textcolor{pink}}
\newcommand{\DUrolepurple}{\textcolor{purple}}
\newcommand{\DUrolered}{\textcolor{red}}
\newcommand{\DUroleteal}{\textcolor{teal}}
\newcommand{\DUroleviolet}{\textcolor{violet}}
\newcommand{\DUrolewhite}{\textcolor{white}}
\newcommand{\DUroleyellow}{\textcolor{yellow}}

'''
}





