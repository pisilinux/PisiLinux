#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def build():
    autotools.make('verbose=1 CXXFLAGS="%s"' % get.CXXFLAGS())

def install():
    autotools.rawInstall("install_prefix=%s/usr" % get.installDIR())

    # Fix conflicts with mono
    pisitools.rename("/usr/bin/xsd", "xsdcxx")
    pisitools.rename("/usr/share/man/man1/xsd.1", "xsdcxx.1")
