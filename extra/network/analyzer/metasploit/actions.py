#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "msf3"

libdir = "/usr/lib/metasploit"
datadir = "/usr/share/metasploit"
bindir = "/usr/bin"


def cleanUP(target):
    # .exe, .dll and .svn crap
    for root, dirs, files in os.walk(target):
        for name in dirs:
            if name ==".svn":
                shelltools.unlinkDir(os.path.join(root, name))
        for name in files:
            if name.endswith(".dll") or name.endswith(".exe"):
                shelltools.unlink(os.path.join(root, name))

def setup():
    cleanUP("./")

def install():
    for i in ["data", "external", "lib", "modules", "plugins", "scripts", "tools"]:
        pisitools.insinto(datadir, i)

    if shelltools.isDirectory("%s/%s/external/source" % (get.installDIR(), datadir)):
            pisitools.removeDir("%s/external/source" % datadir)

    executables = shelltools.ls("msf*")
    # is it really necessary ?
    # executables.append("armitage")

    # needs ruby gtk, and it is said it is kind of bad
    #executables.remove("msfgui")

    # msfweb disabled until Rails is packaged
    # executables.remove("msfweb")

    for i in executables:
        pisitools.insinto(bindir, i)
        # FHS patch obsoletes this
        # pisitools.dosym("/usr/bin/metasploit", i)

    # Cleanup gui
    # FIXME: We leave gui components since they are checked by cli, but we don't support them
    # until necessary packages hit the repos, or the user installs them with gems
    #for i in ["meterpreter", "msfgui", "templates"]:
    #    if shelltools.isDirectory("%s/%s/data/%s" % (get.installDIR(), datadir, i)):
    #        pisitools.removeDir("%s/data/%s" % (datadir, i))

    # pisitools.dodoc("documentation/*.txt", "documentation/*.pdf", "documentation/COPYING")
    pisitools.insinto("/%s" % get.docDIR(), "documentation", get.srcNAME())
    pisitools.insinto("/%s/%s" % (get.docDIR(), get.srcNAME()), "test")
    pisitools.dodoc("HACKING")


