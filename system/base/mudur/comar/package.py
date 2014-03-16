#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
import shutil

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    shutil.copyfile("/etc/fstab", "/etc/fstab.bak")
    new = []
    for line in [line.strip() for line in open("/etc/fstab.bak")]:
        if re.search("\s+\/(run|dev\/shm)\s+", line): continue
        new.append(line)
    new.append("tmpfs                   /run                    tmpfs   nodev,nosuid,size=10%,mode=755    0 0\n")
    with open("/etc/fstab", "w") as f: f.write("\n".join(new))

    # add disks into fstab
    # os.system("/sbin/update-fstab")
