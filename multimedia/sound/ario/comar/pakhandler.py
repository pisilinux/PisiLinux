#!/usr/bin/python
# -*- coding: utf-8 -*-

import piksemel
import os
import fnmatch

def updateData(filepath):
    parse = piksemel.parse(filepath)

    iconFound = False

    for icon in parse.tags("File"):
        path = icon.getTagData("Path")
        if path.startswith("usr/share/icons/hicolor") and not iconFound:
            os.system("/usr/bin/gtk-update-icon-cache -f /usr/share/icons/hicolor")
            iconFound = True
            if immoduleFound:
                return

def setupPackage(metapath, filepath):
    updateData(filepath)

def postCleanupPackage(metapath, filepath):
    updateData(filepath)
