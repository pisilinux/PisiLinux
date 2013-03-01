#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --enable-inotify")

    for root, dirs, files in os.walk(get.workDIR()):
        for name in files:
            if name.endswith(".py"):
                pisitools.dosed("%s/%s" % (root, name), "#!/usr/bin/env python", "#!/usr/bin/python")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # remove static lib.
    pisitools.remove("/usr/lib/libgamin_shared.a")

    pisitools.dodoc("AUTHORS", "README", "COPYING", "NEWS", "TODO")

