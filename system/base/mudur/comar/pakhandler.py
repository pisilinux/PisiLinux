# -*- coding: utf-8 -*-

import piksemel
import imp

def doenv(filepath):
    doc = piksemel.parse(filepath)
    for item in doc.tags("File"):
        path = item.getTagData("Path")
        if path.startswith("etc/env.d"):
            updenv = imp.load_source("updenv", "/sbin/update-environment")
            updenv.update_environment("/")
            return

def setupPackage(metapath, filepath):
    doenv(filepath)

def postCleanupPackage(metapath, filepath):
    doenv(filepath)
