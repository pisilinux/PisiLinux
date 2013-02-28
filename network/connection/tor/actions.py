#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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
