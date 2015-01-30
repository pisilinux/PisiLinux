#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.ldflags.add("-lpython3", "-lpthread", "-ldl", "-lutil", "-lm")
	
    autotools.configure("--with-apxs=/usr/bin/apxs \
                         --with-python=/usr/bin/python")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README.rst", "LICENSE")
