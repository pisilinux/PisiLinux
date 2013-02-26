#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import get


def setup():
    shelltools.export("AUTOPOINT", "/bin/true")
    #autotools.autoreconf("-vfi")
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

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # remove unnecessary files
    perlmodules.removePacklist()
    perlmodules.removePodfiles()
