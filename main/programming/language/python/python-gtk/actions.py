#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "pygtk-%s" % (get.srcVERSION())

def setup():
    shelltools.unlink("py-compile" )
    shelltools.sym("/bin/true", "%s/py-compile" % get.curDIR())

    autotools.configure("--enable-thread \
                         --disable-docs")

    shelltools.touch("%s/style.css" % get.curDIR())
    pisitools.dosed("docs/Makefile", "CSS_FILES = .*", "CSS_FILES = %s/style.css" % get.curDIR())

    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "MAPPING", "NEWS", "README", "THREADS", "TODO")
