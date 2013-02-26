#!/usr/bin/python
# -*- coding: utf-8 -*-

import piksemel
import os

def updateCaches(filepath):
    parse = piksemel.parse(filepath)
    GIO_MODULE_PATH = "usr/lib32/gio/modules"

    for icon in parse.tags("File"):
        path = icon.getTagData("Path")
        if path.startswith(GIO_MODULE_PATH):
            os.system("/usr/bin/32/gio-querymodules /%s" % GIO_MODULE_PATH)
            break

def setupPackage(metapath, filepath):
    updateCaches(filepath)

def postCleanupPackage(metapath, filepath):
    updateCaches(filepath)
