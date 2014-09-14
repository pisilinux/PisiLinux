#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools, get, autotools, pisitools
import glob

WorkDir = "."
SkipFiles = [".pc", "filelist", "patches", "pisiBuildState"]

def install():
    for package in shelltools.ls("."):
        if package in SkipFiles:
            continue
        shelltools.cd(package)        
        pisitools.insinto("/usr/share/fonts/lohit-assamese/","*.ttf")
        
        # Create symlinks
        for i in glob.glob ("*.conf"):
            pisitools.insinto ("/etc/fonts/conf.avail/", i)
        pisitools.dosym("/etc/fonts/conf.avail/%s" % i, "/etc/fonts/conf.d/%s" % i)
        shelltools.cd("../")