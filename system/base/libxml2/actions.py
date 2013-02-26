#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    # fix sandbox violations when attempt to read "/missing.xml"
    pisitools.dosed("testapi.c", "\/missing.xml", "missing.xml")
    
    options = "--with-zlib \
               --with-python \
               --with-readline \
               --enable-ipv6 \
               --disable-static \
               --with-threads"

    if get.buildTYPE() == "emul32":
        options += " --bindir=/emul32/bin \
                     --without-python"
        shelltools.export("CC", "%s -m32" % get.CC())
    else: options += " --with-python"

    autotools.configure(options)

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32": 
        pisitools.removeDir("/usr/share/gtk-doc")
        return

    #for i in ["", "-python"]:
        #pisitools.rename("/%s/libxml2%s-%s" % (get.docDIR(), i, get.srcVERSION()), "libxml2%s" % i)

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")
