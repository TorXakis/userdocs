# Minimal makefile for Sphinx documentation
#

# https://www.sphinx-doc.org/en/master/man/sphinx-build.html
#
#   -M buildername
#
#           Alternative to -b. Uses the Sphinx make_mode module, which provides the same build functionality as a
#           default Makefile or Make.bat.
#
#           Important
#           		Sphinx only recognizes the -M option if it is placed first.
#                     => REASON why SPHINXOPTS placed at end of command in below make rules
#                        which contradicts manpage who says that the SPHINXOPTS should be directly behind SPHINXBUILD

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?= -c config/
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD)  -M help  "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean:
	@$(SPHINXBUILD)  -M clean  "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


.PHONY: help clean Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	#NOT NEEDED: python3 -mpip install dist/pygments_torxakis-0.0.1-py3-none-any.whl
	#   github action  https://github.com/ammaraskar/sphinx-action
	#   installs all packages in requirements.txt
	#   (does do: python3 -mpip install -r requirements.txt)
	$(SPHINXBUILD)  -M $@  "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
