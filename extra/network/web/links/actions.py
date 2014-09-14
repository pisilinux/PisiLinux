#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("LC_ALL", "C")
    shelltools.cd("intl")
    shelltools.system("./synclang")
    shelltools.system("./gen-intl")
    shelltools.cd("..")

    autotools.configure("--enable-graphics \
                         --with-gpm \
                         --with-ssl \
                         --with-zlib \
                         --with-bzip2 \
                         --without-svgalib \
                         --with-x \
                         --with-fb \
                         --with-directfb \
                         --without-pmshell \
                         --without-atheos \
                         --with-libjpeg \
                         --with-libtiff")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dosym("links", "/usr/bin/links2")

    pisitools.dohtml("doc/links_cal")
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "SITES")
