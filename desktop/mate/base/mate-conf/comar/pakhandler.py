#!/usr/bin/python
# -*- coding: utf-8 -*-

import piksemel
import os

def installMateconfSchemas(filepath):
    os.environ['MATECONF_CONFIG_SOURCE'] = 'xml:merged:/etc/mateconf/mateconf.xml.defaults'
    parse = piksemel.parse(filepath)
    schemas = []
    for schema in parse.tags("File"):
        path = schema.getTagData("Path")
        if path.startswith("etc/mateconf/schemas"):
            schemas.append("/"+path)

    if schemas:
        os.system("/usr/bin/mateconftool-2 --makefile-install-rule %s" % " ".join(schemas))

def uninstallMateconfSchemas(filepath):
    os.environ['MATECONF_CONFIG_SOURCE'] = 'xml:merged:/etc/mateconf/mateconf.xml.defaults'
    parse = piksemel.parse(filepath)
    schemas = []
    for schema in parse.tags("File"):
        path = schema.getTagData("Path")
        if path.startswith("etc/mateconf/schemas"):
            schemas.append("/"+path)

    if schemas:
        os.system("/usr/bin/mateconftool-2 --makefile-uninstall-rule %s" % " ".join(schemas))

def setupPackage(metapath, filepath):
    installMateconfSchemas(filepath)

def cleanupPackage(metapath, filepath):
    uninstallMateconfSchemas(filepath)
 
