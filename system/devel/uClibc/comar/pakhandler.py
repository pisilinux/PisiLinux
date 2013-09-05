#!/usr/bin/python

import piksemel
import os

UCLIBC_ROOT = "/usr/lib/uClibc"

def updateLdSoConf(filepath):
    parse = piksemel.parse(filepath)
    for f in parse.tags("File"):
        if UCLIBC_ROOT in f.getTagData("Path"):
            os.system("%s/sbin/ldconfig -X" % UCLIBC_ROOT)

def setupPackage(metapath, filepath):
    updateLdSoConf(filepath)

def cleanupPackage(metapath, filepath):
    pass

def postCleanupPackage(metapath, filepath):
    updateLdSoConf(filepath)
