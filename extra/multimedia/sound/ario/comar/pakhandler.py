#!/usr/bin/python
# -*- coding: utf-8 -*-

import piksemel
import os
import fnmatch

def updateData(filepath):
    parse = piksemel.parse(filepath)

    for icon in parse.tags("File"):
        path = icon.getTagData("Path")
        if path.startswith("usr/share/icons/hicolor"):
            os.system("/usr/bin/gtk-update-icon-cache -f /usr/share/icons/hicolor")
            break

def setupPackage(metapath, filepath):
    updateData(filepath)

def postCleanupPackage(metapath, filepath):
    updateData(filepath)
