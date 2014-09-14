#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("PTHREAD_LIBS", "-lpthread")
    shelltools.system("./autogen.sh")
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()
    shelltools.cd("python")
    pythonmodules.compile()
    shelltools.cd("..")

def install():
    autotools.install()
    shelltools.cd("python")
    pythonmodules.install()
    shelltools.cd("..")

    pisitools.insinto("/usr/share/vim/vimfiles/syntax/", "editors/proto.vim")
    pisitools.insinto("/usr/share/emacs/site-lisp/", "editors/protobuf-mode.el")

    pisitools.dodoc("CHANGES.txt", "CONTRIBUTORS.txt", "COPYING.txt", "README.txt")
