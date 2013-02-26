#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()

def build():
    autotools.make()
    #autotools.make("-C doc/design-paper tor-design.pdf")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ChangeLog", "README", "doc/*.txt")
    # delete script that uses obsolete tsocks prg.
    # use usewithtor/torsocks which comes with torsocks
    # package instead
    pisitools.remove("/usr/bin/torify")
