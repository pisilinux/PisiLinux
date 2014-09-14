#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

console_tools = ["as10k1", "hdsploader", "hda-verb",
                 "mixartloader", "vxloader",
                 "usx2yloader", "sscape_ctl",
                 "sb16_csp", "as10k1", "ld10k1",
                 "us428control", "seq/sbiload"]

gui_tools = ["envy24control", "rmedigicontrol", "hdspconf",
             "hdspmixer", "echomixer", "hwmixvolume"]

alsa_tools = gui_tools + console_tools

docs = ["README", "AUTHORS", "COPYING", "TODO", "NEWS", "ChangeLog"]

if "_" in get.srcVERSION():
    WorkDir = get.srcNAME()

def setup():
    for tool in alsa_tools:
        shelltools.cd(tool)
        if tool in ["hdspconf", "ld10k1"]:
            autotools.autoreconf("-fi")
        autotools.configure()
        shelltools.cd("..")

def build():
    for tool in alsa_tools:
        shelltools.cd(tool)
        autotools.make()
        shelltools.cd("..")

def install():
    for tool in alsa_tools:
        shelltools.cd(tool)
        autotools.rawInstall("DESTDIR=\"%s\"" % get.installDIR())

        for doc in [d for d in docs if shelltools.can_access_file(d)]:
            if tool in gui_tools:
                srctag = "alsa-tools-gui"
            else:
                srctag = get.srcNAME()

            pisitools.insinto("/usr/share/doc/%s/%s" % (srctag, tool), doc)

        shelltools.cd("..")

    pisitools.remove("/usr/share/applications/hdspmixer.desktop")
    pisitools.remove("/usr/share/applications/hdspconf.desktop")
