#/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/var/lib/pisi/info/files.ldb"):
        os.mkdir("/var/lib/pisi/info/files.ldb")
    os.chmod("/var/lib/pisi/info/files.ldb", 509)
    os.chown("/var/lib/pisi/info/files.ldb", 0, 10)
    if not os.path.exists("/var/lib/pisi/package"):
        os.system("mkdir /var/lib/pisi/package")
        os.system("mv /var/lib/pisi/* /var/lib/pisi/package/")
        os.system("mv /var/lib/pisi/package/scripts /var/lib/pisi/")
