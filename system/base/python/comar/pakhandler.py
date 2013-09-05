# -*- coding: utf-8 -*-

import piksemel
import sys
import os

pythonPath="/usr/lib/python%d.%d" % sys.version_info[:2]

def byteCompile(filepath):
    doc = piksemel.parse(filepath)
    paths = []
    for item in doc.tags("File"):
        path = item.getTagData("Path")
        if path.endswith(".py") and not path.startswith("usr/share/doc/"):
            paths.append("/"+path)

    if paths:
        os.system("/usr/bin/python %s/py_compile.py %s" % (pythonPath, " ".join(paths)))

def removeByteCompiled(filepath):
    doc = piksemel.parse(filepath)
    for item in doc.tags("File"):
        path = item.getTagData("Path")
        if path.endswith(".py"):
            try:
                # Remove .pyc and .pyo
                os.unlink("/%sc" % path)
                os.unlink("/%so" % path)
            except OSError:
                pass

def setupPackage(metapath, filepath):
    byteCompile(filepath)

def cleanupPackage(metapath, filepath):
    pass

def postCleanupPackage(metapath, filepath):
    removeByteCompiled(filepath)
