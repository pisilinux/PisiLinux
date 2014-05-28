#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import get


def setup():
    shelltools.export("AUTOPOINT", "/bin/true")
#    autotools.autoreconf("-vfi")
    autotools.configure("--disable-silent-rules \
                         --disable-static \
                         --disable-rpath \
                         --enable-perl \
                         --enable-ruby \
                         --enable-lua \
                         --enable-tcl \
                         --enable-python \
                         --with-rrd-default-font=/usr/share/fonts/dejavu/DejaVuSansMono.ttf \
                         --with-perl-options='installdirs=vendor destdir=%(DESTDIR)s' \
                         --with-ruby-options='sitedir=%(DESTDIR)s/usr/lib/ruby' \
                         " % {"DESTDIR": get.installDIR()})
 
    pisitools.dosed("Makefile", "^RRDDOCDIR.*$", "RRDDOCDIR=${datadir}/doc/${PACKAGE}")
    pisitools.dosed("doc/Makefile", "^RRDDOCDIR.*$", "RRDDOCDIR=${datadir}/doc/${PACKAGE}")
    pisitools.dosed("bindings/Makefile", "^RRDDOCDIR.*$", "RRDDOCDIR=${datadir}/doc/${PACKAGE}")
    pisitools.dosed("examples/Makefile", "examplesdir = .*$", "examplesdir = $(datadir)/doc/${PACKAGE}/examples")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s includedir=/usr/include" % get.installDIR())

    # remove unnecessary files
    perlmodules.removePacklist()
    perlmodules.removePodfiles()
