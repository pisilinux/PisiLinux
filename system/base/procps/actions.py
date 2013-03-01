#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make('CC=%s CPPFLAGS="%s" CFLAGS="%s" LDFLAGS="%s" lib64=lib' % \
                   (get.CC(), get.CXXFLAGS(), get.CFLAGS(), get.LDFLAGS()))

def install():
    autotools.rawInstall('ln_f="ln -sf" ldconfig="true" lib64=lib DESTDIR=%s SKIP="/bin/kill /usr/share/man/man1/kill.1"' % get.installDIR())

    pisitools.dosym("libproc-%s.so" % get.srcVERSION(), "/lib/libproc.so")

    pisitools.dodoc("BUGS", "NEWS", "TODO", "ps/HACKING")
