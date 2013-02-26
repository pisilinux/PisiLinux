import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("chmod 04771 /usr/bin/cdrecord")
