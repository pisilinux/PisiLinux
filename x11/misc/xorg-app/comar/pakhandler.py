# -*- coding: utf-8 -*-

import piksemel

def updateIndex():
    import os
    import subprocess

    join = os.path.join
    fontsPath = "/usr/share/fonts"
    encodingsPath = join(fontsPath, "encodings")
    fontsScale = "fonts.scale"
    fontsDir = "fonts.dir"

    for root, dirs, files in os.walk(fontsPath):
        if root.startswith(encodingsPath):
            continue

        fonts = files[:]

        if fontsScale in fonts:
            fonts.remove(fontsScale)
            os.unlink(join(root, fontsScale))

        if fontsDir in fonts:
            fonts.remove(fontsDir)
            os.unlink(join(root, fontsDir))

        if not fonts:
            continue

        print "Creating %s ..." % join(root, fontsScale)
        subprocess.call(["/usr/bin/mkfontscale", "-u", root])

        print "Creating %s ..." % join(root, fontsDir)
        subprocess.call(["/usr/bin/mkfontdir", root])

def checkPaths(filepath):
    doc = piksemel.parse(filepath)

    for item in doc.tags("File"):
        path = item.getTagData("Path")
        if path.startswith("usr/share/fonts/"):
            updateIndex()
            break

def setupPackage(metapath, filepath):
    checkPaths(filepath)

def cleanupPackage(metapath, filepath):
    pass

def postCleanupPackage(metapath, filepath):
    checkPaths(filepath)
