#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "lash-0.6.0.594"

def setup():
    shelltools.export("CFLAGS", "%s -D_GNU_SOURCE -ldl -ldm -lm -lreadline" % get.CFLAGS())

    #fix unused direct deps.
    autotools.autoreconf("-fi")

    autotools.configure("--disable-static --disable-serv-inst")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.chmod("%s/usr/lib/%s/site-packages/lash.py" % (get.installDIR(), get.curPYTHON()), 0644)

    for s in ("16", "24", "48", "96"):
        pisitools.dodir("/usr/share/icons/hicolor/%sx%s/apps" % (s, s))
        pisitools.domove("usr/share/lash/icons/lash_%spx.png" % s, "/usr/share/icons/hicolor/%sx%s/apps" % (s, s), "lash.png")

    pisitools.domove("usr/share/lash/icons/lash.svg", "/usr/share/icons/hicolor/scalable/apps")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README*", "TODO")
