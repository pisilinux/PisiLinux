#!/usr/bin/python
# -*- coding: utf-8 -*-

import piksemel
import os

def updateCaches(filepath):
    parse = piksemel.parse(filepath)
    GIO_MODULE_PATH = "usr/lib/gio/modules"
    GSCHEMAS_MODULE_PATH = "usr/share/glib-2.0/schemas"

    for icon in parse.tags("File"):
        path = icon.getTagData("Path")
        if path.startswith(GIO_MODULE_PATH):
            os.system("/usr/bin/gio-querymodules /%s" % GIO_MODULE_PATH)
            break

    for icon in parse.tags("File"):
        path = icon.getTagData("Path")
        if path.startswith(GSCHEMAS_MODULE_PATH):
            os.system("/usr/bin/glib-compile-schemas /%s" % GSCHEMAS_MODULE_PATH)
            return

def setupPackage(metapath, filepath):
    updateCaches(filepath)

def postCleanupPackage(metapath, filepath):
    updateCaches(filepath)
