#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi import api as pisiapi
import platform
import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):

    fileassociations = open("/usr/share/applications/mimeapps.list","a")
    fileassociations.write("application/pdf=evince.desktop;\n")
    fileassociations.write("application/zip=file-roller.desktop;\n")
    fileassociations.write("application/x-rar=file-roller.desktop;\n")
    fileassociations.write("application/x-compressed-tar=file-roller.desktop;\n")
    fileassociations.write("application/x-tar=file-roller.desktop;\n")
    fileassociations.write("application/x-bzip-compressed-tar=file-roller.desktop;\n")
    fileassociations.write("image/jpeg=ristretto.desktop;\n")
    fileassociations.write("image/png=ristretto.desktop;\n")
    fileassociations.write("image/gif=ristretto.desktop;\n")
    fileassociations.write("image/x-ms-bmp=ristretto.desktop;\n")
    fileassociations.write("text/plain=geany.desktop;\n")
    fileassociations.write("application/x-pisi=package-manager.desktop;\n")
    fileassociations.close()
    

    #FIXME:
    try:
        os.unlink("/usr/share/xsessions/openbox-gnome.desktop")
    except:
        pass
    try:
        os.unlink("/usr/share/xsessions/openbox-kde.desktop")
    except:
        pass
