#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # for underlinking
    pisitools.dosed("clutter/Makefile.am", "pardusPythonVersion", get.curPYTHON())
    autotools.autoreconf("-i")
    shelltools.system("PYTHON=/usr/bin/python2.7")
    shelltools.export("CXXFLAGS", "%s -I/usr/include/clutter-1.0" % get.CXXFLAGS())
    #shelltools.export("CPPFLAGS", "%s -I/usr/include/clutter-1.0" % get.CPPFLAGS())
    shelltools.export("CXXFLAGS", "%s -I/usr/include/json-glib-1.0" % get.CXXFLAGS())
    #shelltools.export("CPPFLAGS", "%s -I/usr/include/json-glib-1.0" % get.CPPFLAGS())
    pisitools.dosed("clutter/pyclutter.h", r"#include <cogl/cogl-pango.h>", r"#include <cogl-pango/cogl-pango.h>\n#include <GL/gl.h>")
    autotools.configure("--enable-docs")
    
    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")    

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall('DESTDIR=%s INSTALL="install -p"' % get.installDIR())

    for i in shelltools.ls("examples/"):
        if not i.startswith("Makefile"):
            pisitools.insinto("/%s/%s/examples/" % (get.docDIR(), get.srcNAME()), "examples/%s" % i)

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README*", "NEWS")
