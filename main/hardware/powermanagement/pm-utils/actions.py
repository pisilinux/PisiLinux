#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # Drop man pages to regenerate them
    shelltools.unlink("man/*.[18]")

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Install video quirks
    shelltools.copytree("../video-quirks", "%s/usr/lib/pm-utils" % get.installDIR())

    # Create some initial directories
    for d in ("locks", "storage"):
        pisitools.dodir("/run/pm-utils/%s" % d)

    pisitools.dodoc("COPYING", "ChangeLog", "AUTHORS")

    # nm >=0.8.2 has native udev suspend/resume support
    pisitools.remove("/usr/lib/pm-utils/sleep.d/55NetworkManager")

    # Remove hooks that cause hardware failure or don't make sense at all
    pisitools.remove("/usr/lib/pm-utils/power.d/harddrive")
    pisitools.remove("/usr/lib/pm-utils/power.d/disable_wol")
