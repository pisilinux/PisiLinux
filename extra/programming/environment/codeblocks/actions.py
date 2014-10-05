#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    #autotools.autoreconf("-vif")
    plugins = "AutoVersioning,BrowseTracker,byogames,Cccc,CppCheck,cbkoders,codesnippets,codestat,copystrings,dragscroll,envvars,headerfixup,help,hexeditor,incsearch,keybinder,MouseSap,profiler,regex,exporter,symtab,Valgrind"
    autotools.configure("--with-wx-config=/usr/bin/wxconfig \
	                   --disable-debugger \
                           --with-contrib-plugins=%s" % plugins)

    # Disable rpath
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")


def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")