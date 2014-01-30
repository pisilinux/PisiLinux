#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import os

def removeCruft():
    for root, dirs, files in os.walk(get.installDIR()):
        for name in files:
            if name.endswith(".el.gz"):
                shelltools.unlink(os.path.join(root, name))

def setup():
    #autotools.autoreconf("-fvi")
    autotools.configure("--with-x-toolkit=gtk \
                         --with-xft \
                         ac_cv_lib_gif_EGifPutExtensionLast=yes")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove versioned copy
    #pisitools.remove("/usr/bin/emacs-*")
    #removeCruft()

    pisitools.dodoc("ChangeLog", "BUGS", "README", "COPYING")
