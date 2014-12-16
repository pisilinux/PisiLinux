#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi import api as pisiapi
import platform
import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):

    fileassociations = open("/usr/share/applications/mimeapps.list","a")
    fileassociations.write("application/pdf=evince.desktop;\n")
    fileassociations.write("application/zip=xarchiver.desktop;\n")
    fileassociations.write("application/x-rar=xarchiver.desktop;\n")
    fileassociations.write("application/x-compressed-tar=file-roller.desktop;\n")
    fileassociations.write("application/x-tar=xarhiver.desktop;\n")
    fileassociations.write("application/x-bzip-compressed-tar=xarchiver.desktop;\n")
    fileassociations.write("image/jpeg=lximage-qt.desktop;\n")
    fileassociations.write("image/png=lximage-qt.desktop;\n")
    fileassociations.write("image/gif=lximage-qt.desktop;\n")
    fileassociations.write("image/x-ms-bmp=lximage-qt.desktop;\n")
    fileassociations.write("text/plain=juffed.desktop;\n")
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