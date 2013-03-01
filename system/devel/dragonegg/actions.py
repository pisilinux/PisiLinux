# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

import subprocess

# We use unversioned gcc executable
shelltools.export("GCC", "gcc")

def build():
    autotools.make("VERBOSE=1")

def install():
    gccPluginPath = subprocess.Popen("/usr/bin/gcc -print-file-name=plugin", shell=True, stdout=subprocess.PIPE).stdout.read().strip()
    pisitools.insinto(gccPluginPath, "dragonegg.so")

    pisitools.dodoc("README","COPYING", "TODO")
