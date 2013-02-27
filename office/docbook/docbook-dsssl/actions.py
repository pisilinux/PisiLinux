#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def install():
    autotools.rawInstall("BINDIR=%s/usr/bin DESTDIR=%s/usr/share/sgml/docbook/dsssl-stylesheets-%s install"
                         % (get.installDIR(),get.installDIR(),get.srcVERSION()))

    pisitools.rename("/usr/bin/collateindex.pl", "collateindex")
