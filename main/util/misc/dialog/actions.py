#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "dialog-%s" % get.srcVERSION().replace('_','-')

def setup():
    autotools.configure("--prefix=/usr \
                         --mandir=/usr/share/man \
                         --with-ncursesw \
                         --enable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/doc/%s/samples" % get.srcNAME(), "samples/*")
    pisitools.dodoc("CHANGES", "README")
