#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "cdk-5.0-20060507"

def setup():
    autotools.configure("--with-ncurses \
                         --with-libtool")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s DOCUMENT_DIR=%s" % ( get.installDIR(), get.docDIR() ) )
