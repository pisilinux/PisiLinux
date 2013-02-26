#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

# You can use these as variables, they will replace GUI values before build.
# Package Name : python3
# Version : 3.2.3
# Summary : Next generation of the python high-level scripting language

# If the project that you are tying to compile is in a sub directory in the 
# source archive, than you can define working directory. For example; 
# WorkDir="python3-"+ get.srcVERSION() +"/sub_project_dir/"
pyDIR = "Python-3.2.3"
def setup():
    pisitools.dosed("Lib/cgi.py","^#.* /usr/local/bin/python","#!/usr/bin/python")
    shelltools.unlinkDir("Modules/expat")
    shelltools.unlinkDir("Modules/zlib")
    shelltools.unlinkDir("Modules/_ctypes/darwin")
    shelltools.unlinkDir("Modules/_ctypes/libffi")
    shelltools.unlinkDir("Modules/_ctypes/libffi_arm_wince")
    shelltools.unlinkDir("Modules/_ctypes/libffi_msvc")
    shelltools.unlinkDir("Modules/_ctypes/libffi_osx")

    autotools.rawConfigure("--prefix=/usr --enable-shared \
                            --with-threads \
                            --with-computed-gotos \
                            --enable-ipv6 \
                            --with-valgrind \
                            --with-wide-unicode \
                            --with-dbmliborder=gdbm:ndbm \
                            --with-system-expat \
                            --with-system-ffi")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/usr/bin/2to3")
    pisitools.dodoc("LICENSE", "README")
