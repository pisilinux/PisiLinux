#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-fisv")

    options = "\
               --disable-static \
               --disable-silent-rules \
               --%sable-gssapi \
               --with-pic \
              " % ("dis" if get.buildTYPE() == "emul32" else "en")

    autotools.configure(options)

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/etc", "doc/netconfig", "netconfig")
    pisitools.dodoc("AUTHORS", "NEWS", "ChangeLog", "README", "THANKS", "TODO")
