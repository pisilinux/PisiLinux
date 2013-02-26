#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import os

shelltools.export("HOME", get.workDIR())

def removeCruft():
    for root, dirs, files in os.walk(get.installDIR()):
        for name in files:
            if name.endswith(".el.gz"):
                shelltools.unlink(os.path.join(root, name))

def setup():
    #autotools.autoreconf("-fvi")
    autotools.configure("--with-x-toolkit=gtk \
                         --with-xft")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove versioned copy
    pisitools.remove("/usr/bin/emacs-*")
    removeCruft()

    pisitools.dodoc("ChangeLog", "BUGS", "README", "COPYING")
