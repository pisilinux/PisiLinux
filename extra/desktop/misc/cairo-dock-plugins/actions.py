#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt


from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

shelltools.export("HOME", get.workDIR())

def setup():
    pisitools.dosed("Dbus/interfaces/python/PythonInstall.cmake.in",  "\@ROOT_PREFIX\@",  get.installDIR())
    pisitools.dosed("Dbus/interfaces/bash/BashInstall.cmake.in",  "\@ROOT_PREFIX\@",  get.installDIR())
    cmaketools.configure()
    if not shelltools.isDirectory("weblets/src/webkit"):
        shelltools.makedirs("weblets/src/webkit")
        shelltools.sym("%s/weblets/src/webkit" % get.curDIR(), "weblets/src/webkit/webkit")
        for file in shelltools.ls("/usr/include/webkit-1.0/webkit"):
            shelltools.sym("/usr/include/webkit-1.0/webkit/%s" % file,  "weblets/src/webkit/%s" % file)
        pisitools.dosed("weblets/src/applet-struct.h",  "<webkit\/webkit.h>",  '"webkit/webkit.h"')

def build():
    cmaketools.make()

def install():
    cmaketools.install()