#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():
    # Installing application
    pisitools.insinto("/usr/share/java/geogebra", "*.jar")
    pisitools.insinto("/usr/share/java/geogebra/unsigned", "unsigned/*.jar")

    pisitools.insinto("/usr/share/applications/", "geogebra.desktop")
    pisitools.insinto("usr/share/mime/packages/", "geogebra.xml")


    for size in ["16", "22", "24", "32", "48", "64", "128", "256"]:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" %(size, size), "icons/hicolor/%sx%s/apps/geogebra.png" % (size,size))
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/mimetypes" %(size, size), "icons/hicolor/%sx%s/mimetypes/application-vnd.geogebra.file.png" % (size,size))
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/mimetypes" %(size, size), "icons/hicolor/%sx%s/mimetypes/application-vnd.geogebra.tool.png" % (size,size))

    pisitools.dosym("/usr/share/icons/hicolor/256x256/apps/geogebra.png", "/usr/share/pixmaps/geogebra.png")
