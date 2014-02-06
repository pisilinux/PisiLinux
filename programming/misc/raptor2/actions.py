#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

docdir = "/%s/%s" % (get.docDIR(), get.srcNAME())

def setup():
    autotools.configure("--with-xml-parser=libxml\
                         --with-www=curl \
                         --disable-gtk-doc \
                         --with-yajl=no \
                         --with-html-dir=%s/html\
                         --with-icu-config=/usr/bin/icu-config \
                         --disable-static" % docdir)
    
    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")     

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("raptor2/raptor.h", "/usr/include/raptor.h")
    pisitools.dosym("raptor2/raptor2.h", "/usr/include/raptor2.h")
    pisitools.insinto("%s/html" % docdir, "%s/%s/html/raptor2/*" % (get.installDIR(), docdir))
    pisitools.removeDir("%s/html/raptor2" % docdir)
    pisitools.dohtml("*.html")
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
