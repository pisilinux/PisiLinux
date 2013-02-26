#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyleft 2012 Pardus ANKA Community
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.configure("--disable-static \
                         --enable-introspection \
                         --with-gtk=3.0")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/libexec")
    pisitools.dodoc("AUTHORS", "ChangeLog", "HACKING", "MAINTAINERS", "COPYING", "NEWS", "README")
