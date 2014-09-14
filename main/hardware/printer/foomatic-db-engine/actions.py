#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import perlmodules

def setup():
    # The LANG vars aren't reset early enough so when sed tries to use [a-zA-Z], it borks
    shelltools.export("LC_ALL", "C")
    shelltools.export("LANG", "C")

    autotools.autoconf()
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("lib")
    perlmodules.configure()
    perlmodules.make()
    perlmodules.install()
    shelltools.cd("..")

    pisitools.dodoc("ChangeLog", "COPYING", "README", "TODO", "USAGE")
