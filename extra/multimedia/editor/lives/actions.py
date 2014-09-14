# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("configure", "(HAVE_SYSTEM_WEED=)true", r"\1false")
    # fix sandbox violation
    pisitools.dosed("libweed/Makefile.in", "^(\srm -f )\/usr\/lib(\/libweed.*)", r"\1libweed\2")
    # fix doc dir
    pisitools.dosed('Makefile.in',  '^(docdir.*PACKAGE\)).*', r'\1"')
    autotools.configure("\
                         --disable-static \
                         --disable-rpath \
                        ")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("COPYING")
    pisitools.remove("/usr/bin/lives")
    pisitools.dosym("/usr/bin/lives-exe", "/usr/bin/lives")
