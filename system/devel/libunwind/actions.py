#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    pisitools.flags.add("-U_FORTIFY_SOURCE")
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-shared \
                         --disable-static")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

# https://savannah.nongnu.org/bugs/?22368
# https://bugs.gentoo.org/273372
#def check():
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # FIXME: Fedora removes it, Suse keeps it, breaks samba build, investigate further
    pisitools.remove("/usr/lib/libunwind*.a")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS", "TODO")
