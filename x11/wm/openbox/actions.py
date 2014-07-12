#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def setup():
    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-fiv")
    autotools.configure("--disable-static \
                         --with-x \
                         --enable-nls \
                         --sysconfdir=/etc \
                         --libexecdir=/usr/libexec/openbox \
                         --enable-startup-notification \
                         --docdir=/%s/%s" % (get.docDIR(), get.srcNAME()))

    pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodir("/etc/xdg/obmenu-generator/")
    shelltools.copy("%s/obmenu-generator-0.59/obmenu-generator" % get.workDIR(), "%s/usr/bin/" % get.installDIR())
    shelltools.copy("%s/obmenu-generator-0.59/schema.pl" % get.workDIR(), "%s/etc/xdg/obmenu-generator/schema.pl" %  get.installDIR())
    pisitools.dodoc("AUTHORS", "CHANGELOG", "COPYING", "README")
