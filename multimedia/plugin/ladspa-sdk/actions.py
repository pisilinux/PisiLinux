#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-3.0.txt


from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ladspa_sdk/src"

def setup():
    pisitools.dosed("makefile", "-Werror", get.CFLAGS())

def build():
    autotools.make('CC="%s" \
                    CXX="%s" \
                    LD="%s" \
                    targets' % (get.CC(), get.CXX(), get.LD()))

def install():
    autotools.install('INSTALL_PLUGINS_DIR="/usr/lib/ladspa" \
                       MKDIR_P="mkdir -p" \
                       DESTDIR="%s"' % get.installDIR())

    shelltools.cd("..")
    pisitools.dohtml("doc/*.html")
    pisitools.dodoc("doc/COPYING","doc/ladspa.h.txt")
