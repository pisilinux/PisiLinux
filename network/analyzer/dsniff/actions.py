#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "dsniff-2.4"
confdir = "/etc/dsniff"


def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--with-x")

def build():
    autotools.make('CC="%s" -j1' % get.CC())

def install():
    autotools.rawInstall("install_prefix=%s" % get.installDIR())

    pisitools.dodir(confdir)
    for i in ["dnsspoof.hosts", "dsniff.magic", "dsniff.services"]:
        shelltools.copy("%s/usr/share/dsniff/%s" % (get.installDIR(), i), "%s/%s" % (get.installDIR(), confdir))

    pisitools.dodoc("CHANGES", "README*", "TODO")
