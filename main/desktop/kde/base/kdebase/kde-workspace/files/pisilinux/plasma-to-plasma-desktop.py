#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import Qt

import sys
import os
import shutil

def remove(f):
    try:
        os.remove(f)
    except OSError:
        pass

def migratePlasmarc():
    oldrc = kdecore.KStandardDirs.locateLocal("config", "plasmarc")

    if (not oldrc) or oldrc.isEmpty() or (not os.path.exists(oldrc)):
        sys.stderr.write("%s file doesn't exists.\n" % oldrc)
        return

    newrc = kdecore.KStandardDirs.locateLocal("config", "plasma-desktoprc")

    if os.path.exists(newrc):
        sys.stderr.write("%s file already exists.\n" % newrc)
        return

    shutil.copyfile(oldrc, newrc)

    newConfig = kdecore.KConfig("plasma-desktoprc", kdecore.KConfig.NoGlobals)

    for grp in newConfig.groupList():
        if grp.startsWith("Theme") or grp == "CachePolicies":
            newGroup = kdecore.KConfigGroup(newConfig, grp)
            newGroup.deleteGroup()

    plasmarc = kdecore.KConfig("plasmarc", kdecore.KConfig.NoGlobals)
    themeGroup = kdecore.KConfigGroup(plasmarc, "Theme")

    if plasmarc.hasGroup("Theme"):
        if themeGroup.readEntry("name") == "air":
            sys.stderr.write("New default plasma style is Air, no need to specify theme name if it's air.\n")
            themeGroup.deleteGroup()
            kdeui.KPixmapCache.deleteCache("plasma_theme_air")

            remove(kdecore.KStandardDirs.locateLocal("cache", "kpc/plasma_theme_air.data"))
            remove(kdecore.KStandardDirs.locateLocal("cache", "kpc/plasma_theme_air.index"))
            remove(kdecore.KStandardDirs.locateLocal("cache", "plasma-svgelements-air"))

    else:
        sys.stderr.write("Old default plasma style was Oxygen, so writing oxygen to plasmarc manually.\n")
        themeGroup.writeEntry("name", "oxygen")

        kdeui.KPixmapCache.deleteCache("plasma_theme_default")

        remove(kdecore.KStandardDirs.locateLocal("cache", "kpc/plasma_theme_default.data"))
        remove(kdecore.KStandardDirs.locateLocal("cache", "kpc/plasma_theme_default.index"))
        remove(kdecore.KStandardDirs.locateLocal("cache", "plasma-svgelements-default"))

def migrateAppletsrc():
    oldrc = kdecore.KStandardDirs.locateLocal("config", "plasma-appletsrc")

    if (not oldrc) or oldrc.isEmpty() or (not os.path.exists(oldrc)):
        sys.stderr.write("%s file doesn't exists.\n" % oldrc)
        return

    newrc = kdecore.KStandardDirs.locateLocal("config", "plasma-desktop-appletsrc")

    if os.path.exists(newrc):
        sys.stderr.write("%s file already exists.\n" % newrc)
        return

    shutil.move(oldrc, newrc)

if __name__ == "__main__":
    cd = kdecore.KComponentData("plasma-to-plasma-desktop")

    migratePlasmarc()
    migrateAppletsrc()
