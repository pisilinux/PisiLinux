#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

import os

WorkDir = "magicor-%s" % get.srcVERSION().replace("_", "-")

pythonlib = "/usr/lib/%s/site-packages/" % get.curPYTHON()
sharedir = "/usr/share/magicor"
config = "/etc/magicor.conf"
config_editor = "/etc/magicor.conf"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    autotools.make("clean")

    for d in ["etc", "magicor", "scripts"]:
        fixperms(d)

    pisitools.dosed("Magicor.py", "###CONFIG_PATH###", config)
    pisitools.dosed("Magicor-LevelEditor.py", "###CONFIG_PATH###", config_editor)

    pisitools.dosed("etc/magicor.conf", "###SHARE_PATH###", sharedir)
    pisitools.dosed("etc/magicor-editor.conf", "###SHARE_PATH###", sharedir)

    # pisitools.dosed("Magicor-LevelEditor.py", "###GLADE_FILE###", "%s/editor.glade" % sharedir)

def install():
    pisitools.dodir(pythonlib)
    shelltools.copytree("magicor", "%s/%s/" % (get.installDIR(), pythonlib))

    for f in ["Magicor.py", "Magicor-LevelEditor.py"]:
        pisitools.dobin(f)

    pisitools.rename("/usr/bin/Magicor.py", "magicor")
    pisitools.rename("/usr/bin/Magicor-LevelEditor.py", "magicor-editor")

    # pisitools.dodir(sharedir)
    # pisitools.insinto(sharedir, "etc/editor.glade", "magicor-editor.glade")
    pisitools.insinto("/etc", "etc/magicor.conf")
    pisitools.insinto("/etc", "etc/magicor-editor.conf")

    pythonmodules.fixCompiledPy("/usr")
    pisitools.dodoc("LICENSE", "README")

