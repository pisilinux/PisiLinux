# -*- coding: utf-8 -*-

import piksemel
import subprocess

def updateCache(filepath):
    doc = piksemel.parse(filepath)
    for item in doc.tags("File"):
        path = item.getTagData("Path")
        if path.startswith("usr/share/fonts"):
            subprocess.call(["/usr/bin/fc-cache"])
            return

def setupPackage(metapath, filepath):
    updateCache(filepath)

def cleanupPackage(metapath, filepath):
    pass

def postCleanupPackage(metapath, filepath):
    updateCache(filepath)
