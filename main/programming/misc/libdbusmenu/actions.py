#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
import os

shelltools.export("HOME", get.workDIR())
shelltools.export("HAVE_VALGRIND_FALSE", "yes")

def setup():
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
    
    options = "--disable-static \
               --disable-silent-rules \
               --disable-scrollkeeper \
               --disable-dumper \
               --disable-tests \
               --enable-introspection=yes"
    
    shelltools.makedirs("../gtk2-rebuild")
    shelltools.system("cp -R * ../gtk2-rebuild &>/dev/null")

    autotools.autoreconf("-fvi")
    autotools.configure("%s --with-gtk=3" % options)
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")
    shelltools.cd("../gtk2-rebuild")
    autotools.autoreconf("-fvi")
    autotools.configure("%s --with-gtk=2" % options)    
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()
    shelltools.cd("../gtk2-rebuild")
    autotools.make()

"""
#Requires dbus-test-runner (https://launchpad.net/dbus-test-runner)

def check():
    autotools.make("check")
"""

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*", "README", "NEWS")

    shelltools.cd("../gtk2-rebuild")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/gtk-doc")
