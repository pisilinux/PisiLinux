#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="."

def build():
    shelltools.cd("src")
    autotools.make()

def install():
    pisitools.insinto("/usr/share/acreloaded/bin_linux/", "src/native_client")
    pisitools.insinto("/usr/share/acreloaded/bin_linux/", "src/native_server")
    pisitools.insinto("/usr/share/acreloaded", "bin_linux/linux_64_client", "acreloaded_client")
    pisitools.insinto("/usr/share/acreloaded", "bin_linux/linux_64_server", "acreloaded_server")
    pisitools.insinto("/usr/share/acreloaded", "bot")
    pisitools.insinto("/usr/share/acreloaded", "config")
    pisitools.insinto("/usr/share/acreloaded", "locale")
    pisitools.insinto("/usr/share/acreloaded", "packages")
    pisitools.insinto("/usr/share/doc/acreloaded", "Readme*")