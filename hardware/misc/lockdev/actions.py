#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

pisitools.cflags.add("-fPIC")

def setup():
    shelltools.system('patch --remove-empty-files --no-backup-if-mismatch  -p1 -i "../lockdev_1.0.3-1.5.diff"')

    # disable tests
    pisitools.dosed("Makefile", "^.*cd LockDev && make test$", "")

    # Set CFLAGS
    pisitools.dosed("Makefile", "OPTIMIZE=\".*\"", "OPTIMIZE=\"%s\"" % get.CFLAGS())
    pisitools.dosed("Makefile", "^(CFLAGS\s*=\s*)-g", r"\1 %s" % get.CFLAGS())

    # Set PATH_LOCK
    pisitools.dosed('src/lockdev.c', '("\/)var(\/lock)"', r'\1run\2/lockdev"')

def build():
    autotools.make("CC=%s CFLAGS=\"%s\"" % (get.CC(), get.CFLAGS()))

def install():
    autotools.rawInstall('basedir="%s/usr"' % get.installDIR())

    pisitools.remove("/usr/lib/*.a")

    pisitools.dosym("liblockdev.so.1.0.3", "/usr/lib/liblockdev.so.1")
    shelltools.chmod("%s/usr/lib/liblockdev.so.1.0.3" % get.installDIR(), 0755)

    pisitools.dodir("/run/lock/lockdev")
    shelltools.chmod("%s/run/lock/lockdev" % get.installDIR(), 0775)
    shelltools.chown("%s/run/lock/lockdev" % get.installDIR(), "root", "lock")

    pisitools.dodoc("ChangeLog", "AUTHORS", "LICENSE")
