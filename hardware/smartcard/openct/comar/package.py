#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def preRemove():
    if os.path.exists("/run/openct"):
        for f in os.listdir("/run/openct"):
            try:
                os.unlink(os.path.join("/run/openct", f))
            except OSError:
                pass
        os.rmdir("/run/openct")
