# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("CC=%s OPT_CFLAGS='%s' EXTRA_LDFLAGS='%s'" % (get.CC(), get.CFLAGS(), get.LDFLAGS()))

def install():
    autotools.install("INSTALL_PLUGINS_DIR=%s/usr/lib/ladspa \
                       INSTALL_LRDF_DIR=%s/usr/share/ladspa/rdf"
                       % (get.installDIR(), get.installDIR()))

    pisitools.dodoc("README", "COPYING", "CREDITS")
