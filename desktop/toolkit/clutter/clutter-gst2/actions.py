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
    # guess we should update to new autoconf
    #shelltools.system("gtkdocize")
    #autotools.autoreconf("-fi")
    autotools.configure("--disable-static")

def build():
    autotools.make("V=1")

def install():
    autotools.rawInstall('DESTDIR=%s INSTALL="install -p"' % get.installDIR())

    for i in shelltools.ls("examples"):
        if i.endswith(".png") or i.endswith(".c"):
            pisitools.insinto("/%s/%s/examples/" % (get.docDIR(), get.srcNAME()), "examples/%s" % i)
            
    pisitools.domove("/usr/share/gtk-doc/html/clutter-gst/*", "/usr/share/gtk-doc/html/clutter-gs2/")
    pisitools.removeDir("/usr/share/gtk-doc/html/clutter-gst/")

    pisitools.dodoc("AUTHORS", "ChangeLog*", "README*", "NEWS")