#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    # Disable test causing sandbox violations
    pisitools.dosed("test/util/Makefile.in", "^(check_PROGRAMS.*?)\sopal_path_nfs\$\(EXEEXT\)", "\\1")

    shelltools.export("LDFLAGS","%s -Wl,-z,noexecstack" % get.LDFLAGS())

    autotools.configure("--enable-pretty-print-stacktrace \
                         --enable-orterun-prefix-by-default \
                         --without-slurm")

    pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS","LICENSE","README","NEWS")
