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
    autotools.configure("--disable-static \
                         --enable-pcre \
                         --enable-xml2 \
                         --with-regex-library=pcre \
                         --disable-gtk-doc \
                         --with-html-dir=%s" % docdir)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("rasqal/rasqal.h", "/usr/include/rasqal.h")
    pisitools.insinto("%s/html" % docdir, "%s/%s/rasqal/*" % (get.installDIR(), docdir))
    pisitools.removeDir("%s/rasqal" % docdir)
    pisitools.dohtml("*.html")
    pisitools.dodoc("AUTHORS", "ChangeLog*", "COPYING*", "NEWS", "README")
