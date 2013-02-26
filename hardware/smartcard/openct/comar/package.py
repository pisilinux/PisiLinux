#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def preRemove():
    if os.path.exists("/var/run/openct"):
        for f in os.listdir("/var/run/openct"):
            try:
                os.unlink(os.path.join("/var/run/openct", f))
            except OSError:
                pass
        os.rmdir("/var/run/openct")
