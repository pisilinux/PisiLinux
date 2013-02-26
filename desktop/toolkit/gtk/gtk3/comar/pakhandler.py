#!/usr/bin/python
# -*- coding: utf-8 -*-

import piksemel
import os
import fnmatch

def updateData(filepath):
    parse = piksemel.parse(filepath)

    iconFound = False
    immoduleFound = False

    for icon in parse.tags("File"):
        path = icon.getTagData("Path")
        if path.startswith("usr/share/icons/hicolor") and not iconFound:
            os.system("/usr/bin/gtk-update-icon-cache -f /usr/share/icons/hicolor")
            iconFound = True
            if immoduleFound:
                return

        if fnmatch.fnmatch(path, "usr/lib/gtk-3.0/*immodules/*.so") and not immoduleFound:
            os.system("/usr/bin/gtk-query-immodules-3.0 > /etc/gtk-3.0/gtk.immodules")
            immoduleFound = True
            if iconFound:
                return

        if fnmatch.fnmatch(path, "usr/lib32/gtk-3.0/*immodules/*.so") and not immoduleFound:
            immodulesdir = "/etc/gtk-3.0/32bit"
            if not os.path.exists(immodulesdir):
                os.makedirs(immodulesdir, 0755)
            os.system("/usr/bin/gtk-query-immodules-3.0-32bit > %s/gtk.immodules" % immodulesdir)
            immoduleFound = True
            if iconFound:
                return

def setupPackage(metapath, filepath):
    updateData(filepath)

def postCleanupPackage(metapath, filepath):
    updateData(filepath)
