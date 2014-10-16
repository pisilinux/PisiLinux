#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

import os
import fnmatch
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    pisitools.dosed("clamtk", "use ClamTk::Prefs", "use lib \"/usr/lib/\";\nuse ClamTk::Prefs")
    pisitools.dosed("clamtk", "use ClamTk::GUI", "use lib \"/usr/lib/\";\nuse ClamTk::GUI")
    pisitools.dosed("clamtk", "use ClamTk::Analysis", "use lib \"/usr/lib/\";\nuse ClamTk::Analysis")

def install():
    pisitools.dobin("clamtk")
    pisitools.dolib("lib/*", "/usr/lib/perl5/vendor_perl/"+ get.curPERL()+ "/ClamTk")
    pisitools.doman("clamtk.1.gz")
    pisitools.insinto("/usr/share/applications", "clamtk.desktop")
    pisitools.insinto("/usr/share/pixmaps", "images/clamtk.png")
    pisitools.insinto("/usr/share/pixmaps", "images/clamtk.xpm")
    pisitools.dodoc("CHANGES", "DISCLAIMER", "LICENSE", "README")

    #Locales
    for i in os.listdir("po"):
        if fnmatch.fnmatch(i, '*.po'):
            pisitools.domo("po/" + i, i.replace(".po", ""), "clamtk.mo")
