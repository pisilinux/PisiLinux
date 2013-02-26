#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    options = "--disable-static"

    if not get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib"

    autotools.configure(options)

    pisitools.dosed("libtool", "^sys_lib_dlsearch_path_spec=.*", "sys_lib_dlsearch_path_spec=\"/%{_lib} %{_libdir} \"")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32": return

    pisitools.dodoc("ChangeLog", "README", "NEWS", "AUTHORS", "COPYING")
