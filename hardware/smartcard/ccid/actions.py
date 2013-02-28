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
    # FIXME: GROUP conversion here (pcscd -> pnp)
    pisitools.dosed("src/92_pcscd_ccid.rules", 'GROUP="pcscd"', 'GROUP="pnp"')
    autotools.configure("--enable-twinserial \
                         --disable-static \
                         --disable-dependency-tracking")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/lib/udev/rules.d/", "src/92_pcscd_ccid.rules", "92-pcscd_ccid.rules")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
