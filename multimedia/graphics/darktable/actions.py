#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import os

def setup():
    # fix build with glib 2.35.0
    for (path, dirs, files) in os.walk(get.workDIR()):
        for file in files:
            if file.endswith(".c"):
                with open("%s/%s" % (path, file)) as f:
                    lines = f.readlines()
                new_file = ""
                for line in lines:
                    if not line.find("g_type_init()") == -1:
                        new_file = new_file + "#if !GLIB_CHECK_VERSION(2,35,0)\n" + line + "#endif\n"
                    else: 
                        new_file = new_file + line
                open("%s/%s" % (path, file), "w").write(new_file)
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DDONT_INSTALL_GCONF_SCHEMAS=1 \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DBINARY_PACKAGE_BUILD=1 \
                          -DBUILD_USERMANUAL=0", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.install()
