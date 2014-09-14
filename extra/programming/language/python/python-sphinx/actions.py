#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Sphinx-%s" % get.srcVERSION()

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    # Generating the Grammar pickle to avoid on the fly generation causing sandbox violations
    pythonmodules.run("-c \"from sphinx.pycode.pgen2.driver import load_grammar ; \
load_grammar('%s/usr/lib/%s/site-packages/sphinx/pycode/Grammar-py2.txt')\"" %(get.installDIR(), get.curPYTHON(), ) )

    # create sphinx documentation using itself
    pythonmodules.run("sphinx-build.py doc doc/_build/html")
    pisitools.dohtml("doc/_build/html/*")

    pisitools.dodoc("CHANGES", "EXAMPLES")

