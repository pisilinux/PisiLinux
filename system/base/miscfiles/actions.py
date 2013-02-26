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

dirs = ("dict", "rfc")

def setup():
    autotools.configure("--datadir=/usr/share/misc")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    for d in dirs:
        pisitools.dodir("/usr/share/%s" % d)
        for line in tuple(open("Makefile.am", 'r')):
            if line.startswith(d):
                for f in line.strip().split("=")[1][1:].split(" "):
                    pisitools.domove("/usr/share/misc/%s" % f, "/usr/share/%s/" % d)

    pisitools.dodoc("GNU*", "NEWS", "ORIGIN", "README", "dict-README")
