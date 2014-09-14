# -*- coding: utf-8 -*-

import piksemel
import os
import subprocess

def byteCompile(filepath):
    doc = piksemel.parse(filepath)
    for item in doc.tags("File"):
        path = item.getTagData("Path")
        if path.endswith(".el") and not os.path.exists("/%sc" % path):
            subprocess.call(["/usr/bin/emacs", "--no-init-file", "--no-site-file", "--multibyte", "-batch", "-f", "batch-byte-compile", "/%s" % path])

def removeByteCompiled(filepath):
    doc = piksemel.parse(filepath)
    for item in doc.tags("File"):
        path = item.getTagData("Path")
        if path.endswith(".el"):
            try:
                # Remove .elc
                os.unlink("/%sc" % path)
            except OSError:
                pass

def setupPackage(metapath, filepath):
    byteCompile(filepath)

def cleanupPackage(metapath, filepath):
    removeByteCompiled(filepath)
