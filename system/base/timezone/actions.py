#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "tzdata"
tzcode  = "tzcode2012f"
tzdata  = "tzdata2012f"

configTemplate = """
objpfx = %(pwd)s/obj/
sbindir = %(sbindir)s
datadir = %(datadir)s
install_root = %(buildroot)s
sysdep-CFLAGS = %(cflags)s
"""

configVars = {"pwd": "%s/%s" % (get.workDIR(), WorkDir),
              "sbindir": "/%s" % get.sbinDIR(),
              "datadir": "/%s" % get.dataDIR(),
              "buildroot": get.installDIR(),
              "cflags": get.CFLAGS()
}


def disableLocale():
    for i in ["LANG", "LANGUAGE", "LC_ALL"]:
        shelltools.export(i, "POSIX")

def setup():
    shelltools.sym("Makeconfig.in", "Makeconfig")
    shelltools.echo("config.mk", configTemplate % configVars)
    shelltools.cd("tzcode2012f")
    autotools.make("version.h")

def build():
    disableLocale()
    autotools.make("-j1")

# unfortunately check depends on files which are generated during install, that are never put in
# workdir. We will check after installation not to mess up the already complicated build system
def mycheck():
    print "------------------- Start of tests ------------------------"
    disableLocale()
    autotools.make("check")
    print "------------------- End of tests ------------------------"

def install():
    disableLocale()
    autotools.rawInstall()

    for i in ["README", "Theory", "tz-link.htm"]:
        pisitools.dodoc("%s/%s" % (tzcode, i))

    mycheck()

    # Create Timezone db in /usr/share/zoneinfo
    shelltools.chmod("dump-tz-db", 0755)
    shelltools.system("./dump-tz-db %s" % get.installDIR())

