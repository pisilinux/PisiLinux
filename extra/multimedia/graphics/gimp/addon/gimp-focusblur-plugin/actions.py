#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    #fix error "Only <glib.h> can be included directly."
    for f in shelltools.ls("src/*"):
        pisitools.dosed(f, "(#include\s<glib)\/[^\.]+(\.h>)", r"\1\2")
    autotools.configure("LIBS=-lm")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
