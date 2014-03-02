#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.isfile("/etc/ssl/certs/java/cacerts"):
        os.system("/usr/bin/init-jks-keystore") 