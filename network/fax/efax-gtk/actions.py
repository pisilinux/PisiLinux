#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi") #needed by spooldir patch
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # install efix tool
    pisitools.dobin("efax/efix-0.9a")
    pisitools.doman("efax/efix.1")

    pisitools.domo("po/tr.po", "tr", "efax-gtk.mo")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
