#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import get

import os
import gzip

NoStrip = ["/"]

WorkDir = "oxygen-icons-%s" % get.srcVERSION()

def mygunzip(_file):
    r_file = gzip.GzipFile(_file, "r")
    write_file = _file.replace(".svgz", ".svg")
    # Fix .png.svg typos
    if write_file.endswith(".png.svg"):
        write_file = write_file.replace(".png.svg", ".svg")
    w_file = open(write_file, "w")
    w_file.write(r_file.read())
    w_file.close()
    r_file.close()
    os.unlink(_file)

def setup():
    kde4.configure()

def install():
    kde4.install()

    #install SVG files
    shelltools.copytree("scalable", "%s/usr/share/icons/oxygen/scalable" % get.installDIR())
    pisitools.remove("/usr/share/icons/oxygen/scalable/*.sh")

    pisitools.dosym("/usr/share/icons/oxygen/16x16/actions/list-add.png", "/usr/share/icons/oxygen/16x16/actions/add.png")
    pisitools.dosym("/usr/share/icons/oxygen/22x22/actions/list-add.png", "/usr/share/icons/oxygen/22x22/actions/add.png")
    pisitools.dosym("/usr/share/icons/oxygen/32x32/actions/list-add.png", "/usr/share/icons/oxygen/32x32/actions/add.png")
    pisitools.dosym("/usr/share/icons/oxygen/48x48/actions/list-add.png", "/usr/share/icons/oxygen/48x48/actions/add.png")
    
    pisitools.dosym("/usr/share/icons/oxygen/16x16/actions/application-exit.png", "/usr/share/icons/oxygen/16x16/actions/cancel.png")
    pisitools.dosym("/usr/share/icons/oxygen/22x22/actions/application-exit.png", "/usr/share/icons/oxygen/22x22/actions/cancel.png")
    pisitools.dosym("/usr/share/icons/oxygen/32x32/actions/application-exit.png", "/usr/share/icons/oxygen/32x32/actions/cancel.png")
    pisitools.dosym("/usr/share/icons/oxygen/48x48/actions/application-exit.png", "/usr/share/icons/oxygen/48x48/actions/cancel.png")
    
    #delete kmplayer icons from oxygen theme
    prefix = "/usr/share/icons/oxygen/"
    conflictingIcons = ("kmplayer", "digikam", "showfoto")

    for size in (16, 22, 32, 48, 64, 128):
        for icon in conflictingIcons:
            pisitools.remove("%s%sx%s/apps/%s.png" % (prefix, size, size, icon))

    for icon in conflictingIcons:
        pisitools.remove("%sscalable/apps/%s.svgz" % (prefix, icon))

    #Unzip svgz icons to better compress them with lzma (in install.tar.lzma)
    for root, dirs, files in os.walk("%s/%s/scalable" % (get.installDIR(), prefix)):
        for name in files:
            if name.endswith(".svgz"):
                f = os.path.join(root, name)
                mygunzip(f)

    pisitools.dodoc("AUTHORS", "CONTRIBUTING", "COPYING")
