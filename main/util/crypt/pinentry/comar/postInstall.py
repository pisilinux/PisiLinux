import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chmod 4755 /usr/kde/3.5/bin/pinentry")
