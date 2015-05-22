#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    python = "--without-python" if get.buildTYPE() == "emul32" else "--with-python=/usr/bin/python2.7 "
    # don't remove --with-debugger as it is needed for reverse dependencies
    autotools.configure("%s \
                         --with-crypto \
                         --with-debugger \
                         --disable-static \
                         --with-xz \
                         --with-zlib \
                         --disable-silent-rules \
                        " % python)

    pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "Copyright", "FEATURES", "NEWS", "README", "TODO")
