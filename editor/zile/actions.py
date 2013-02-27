#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
import pisi.actionsapi.get as get
from pisi.util import join_path
import os

def append_file(destination, source):
    dest = file(destination, 'ab')
    src = file(source, 'rb')
    chunk = src.read(65536)
    while len(chunk) != 0:
        dest.write(chunk)
        chunk = src.read(65536)
    src.close()
    dest.close()
    
def setup():
    autotools.configure()
    #prepare "full" dotzile.sample, the key bindings are necessary
    #append_file("src/dotzile.sample", "src/dotzile-extra.el")
    #Necessary to get rid of build dependencies "lua", "help2man" (due to patch)
    #st = os.stat("src/macro.c")
    #os.utime("src/main.c", (st.st_mtime, st.st_mtime))
    #st = os.stat("src/zile.1")
    #os.utime("src/zile.1.in", (st.st_mtime, st.st_mtime))

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "THANKS")
