#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/doc/libjpeg-turbo/", "ChangeLog.txt")
    pisitools.insinto("/usr/share/doc/libjpeg-turbo/", "README*")
    #jpeg-devel confilicts
    pisitools.remove("/usr/share/doc/README")
    pisitools.remove("/usr/include/jerror.h")
    pisitools.remove("/usr/include/jconfig.h")
    pisitools.remove("/usr/include/jpeglib.h")
    pisitools.remove("/usr/include/jmorecfg.h")

