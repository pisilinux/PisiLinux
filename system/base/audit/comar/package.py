#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("ln -s /usr/sbin/audispd /sbin/audispd")
    os.system("ln -s /usr/sbin/auditd /sbin/auditd")
    os.system("/bin/systemctl enable auditd.service")
