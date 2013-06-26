# -*- coding: utf-8 -*-

import piksemel
import stat
import imp
import os

def doenv(filetag):
    for item in filetag:
        path = item.getTagData("Path")
        if path.startswith("etc/env.d"):
            updenv = imp.load_source("updenv", "/sbin/update-environment")
            updenv.update_environment("/")
            return

def docopy(filetag):
    if not os.path.exists("/var/rundirs"): os.makedirs("/var/rundirs")
    for item in filetag:
        path = item.getTagData("Path")
        if path.startswith("var/run/"): path = path[4:]
        if path.startswith("run/"):
            if not os.path.exists("/var/rundirs/%s" % path[4:]): os.makedirs("/var/rundirs/%s" % path[4:])
            subpath = ""
            for d in path.split("/")[1:]:
                subpath = os.path.join(subpath, d)
                s = os.stat("/run/%s" % subpath)
                os.chmod("/var/rundirs/%s" % subpath, stat.S_IMODE(s.st_mode))
                os.chown("/var/rundirs/%s" % subpath, s.st_uid, s.st_gid)

def doclean(filetag):
    for item in filetag:
        path = item.getTagData("Path")
        if path.startswith("var/run/"): path = path[4:]
        if path.startswith("run/"):
            if os.path.exists("/var/rundirs/%s" % path[4:]):
                os.removedirs("/var/rundirs/%s" % path[4:])


def setupPackage(metapath, filepath):
    doc = piksemel.parse(filepath)
    doenv(doc.tags("File"))
    docopy(doc.tags("File"))

def postCleanupPackage(metapath, filepath):
    doc = piksemel.parse(filepath)
    doenv(doc.tags("File"))
    doclean(doc.tags("File"))
