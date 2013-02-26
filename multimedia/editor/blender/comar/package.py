#/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if os.path.islink("/usr/lib/blender/plugins/include"):
        os.system("/bin/rm -f /usr/lib/blender/plugins/include")
