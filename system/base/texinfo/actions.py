#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("doc/texinfo.txi", "setfilename texinfo", "setfilename texinfo.info")
    pisitools.dosed("doc/Makefile.in", "INFO_DEPS = texinfo", "INFO_DEPS = texinfo.info")
    pisitools.dosed("doc/Makefile.in", "texinfo:", "texinfo.info:")

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.newdoc("info/README", "README.info")
    pisitools.newdoc("makeinfo/README", "README.makeinfo")
    pisitools.dodoc("AUTHORS", "ChangeLog", "INTRODUCTION", "NEWS", "README", "TODO")
