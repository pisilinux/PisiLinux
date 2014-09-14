# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for exe in ("loadkeys", "setfont", "unicode_start", "unicode_stop"):
        pisitools.domove("/usr/bin/%s" % exe, "/bin")
        pisitools.dosym("/bin/%s" % exe, "/usr/bin/%s" % exe)

    pisitools.remove("/usr/share/keymaps/i386/qwerty/trf.map.gz")

    pisitools.dohtml("doc/*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
