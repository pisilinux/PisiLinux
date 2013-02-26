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

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static \
                         --without-docdir")
                         #FIXME: documentation is temporarily disabled since update release 7.
                         #--with-documentation=/usr/share/doc/%s" % get.srcNAME())

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.remove("/usr/share/doc/libupnp/IXML_Programming_Guide.pdf")
    #pisitools.remove("/usr/share/doc/libupnp/UPnP_Programming_Guide.pdf")

