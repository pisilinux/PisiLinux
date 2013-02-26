#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #autotools.autoreconf("-vif")

    autotools.configure("--localstatedir=/var \
                         --disable-doc")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.doman("doc/*.[1-8]")
    pisitools.dodir("/var/lib/lxc")

    # Install management tools
    shelltools.unlink("lxc-management-tools/lxc-management-tools.spec")
    for script in shelltools.ls("lxc-management-tools/lxc-*"):
        pisitools.dobin(script)

    shelltools.move("%s/usr/lib/lxc/templates" % get.installDIR(), "%s/%s/lxc/" % (get.installDIR(), get.docDIR()))
