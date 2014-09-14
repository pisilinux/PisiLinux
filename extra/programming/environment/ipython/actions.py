#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodir("/usr/share/emacs/site-lisp")
    pisitools.insinto("/usr/share/emacs/site-lisp", "docs/emacs/ipython.el")

    #pisitools.dodoc("README.txt")
