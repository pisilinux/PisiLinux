#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/etc/italc/keys/"):
        os.system("/usr/bin/ica -role teacher -createkeypair > /dev/null")
        os.system("/bin/chgrp -R italc /etc/italc")
        os.system("/bin/chmod -R 750 /etc/italc/keys/private")
        os.system("/bin/chmod 644 /etc/italc/keys/public/teacher/key")
