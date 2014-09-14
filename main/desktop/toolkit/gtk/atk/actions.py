#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed(".", "^(SUBDIRS =.*)tests(.*)$", "\\1\\2", filePattern="^Makefile.(am|in)", level=0)
    autotools.autoreconf("-fiv")
    autotools.configure("\
                         --disable-static \
                         --enable-introspection=%s \
                        " % ("no" if get.buildTYPE() == "emul32" else "yes"))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/gtk-doc")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
