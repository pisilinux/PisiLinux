#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    update-mime-database usr/share/mime > /dev/null 2>&1
    update-desktop-database -q > /dev/null 2>&1