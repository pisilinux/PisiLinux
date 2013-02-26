#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system('update-desktop-database')

def preRemove():
    os.system('update-desktop-database')

