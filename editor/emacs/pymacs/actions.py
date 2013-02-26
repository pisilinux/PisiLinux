#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

#WorkDir="pinard-Pymacs-5989046"

def install():
    pythonmodules.install()
    pisitools.insinto("/usr/share/emacs/site-lisp", "pymacs.el.in", "pymacs.el")

    pisitools.dodoc("THANKS", "README", "TODO")
