from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.fileutil import copy_asset
from os import path

# used ideas from /usr/local/lib/python3.9/site-packages/sphinx/ext/graphviz.py

css_filename='textcolor_styles.css'
package_dir=path.dirname(__file__)
colors = [ "black",  "blue", "brown",  "cyan",  "darkgray", "gray",  "green", "lightgray",  "lime",  "magenta", "olive",  "orange", "pink", "purple", "red", "teal", "violet", "white", "yellow" ]

def on_config_inited(app: Sphinx,config)-> None:
    # https://www.sphinx-doc.org/en/master/latex.html#latex-elements-confval
    # add tex commands from file to latex preamble
    latex_elements=config['latex_elements']
    latex_elements['preamble'] += "\n" + r'\input{textcolor_commands.tex.txt}' + "\n"

    # add latex package (adding it in on_build_inited it too late)
    app.add_latex_package('xcolor')

    # # configure html to include css file
    # app.add_css_file(css_filename)

def on_build_inited(app: Sphinx)-> None:

    if app.builder.format == 'html':
        # configure html to include css file
        app.add_css_file(css_filename)

    if app.builder.format == 'latex':
        # add latex file to builder folder
        src = path.join(package_dir, 'resources', 'textcolor_commands.tex.txt')
        dst = app.outdir
        copy_asset(src,dst)

def on_build_finished(app: Sphinx, exc: Exception) -> None:
    # for html : add css file to _static subdir in html builder dir
    # for latex : add DUroles in preamble + add xcolor package (to extrapackages config)
    if exc is None:
        if app.builder.format == 'html':
            # add css file to builder output
            src = path.join(package_dir, 'resources', css_filename)
            dst = path.join(app.outdir, '_static')
            copy_asset(src, dst)


#https://protips.readthedocs.io/link-roles.html
def role_textcolor(color):
    def role(name, rawtext, text, lineno, inliner, options={}, content=[]):
        node = nodes.inline(text=text, classes=[color])
        return [node], []
    return role



def setup(app: Sphinx):
    for color in colors:
        app.add_role(color,role_textcolor(color))

    # https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx-core-events
    app.connect('config-inited',  on_config_inited)
    app.connect('builder-inited', on_build_inited)
    app.connect('build-finished', on_build_finished)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }