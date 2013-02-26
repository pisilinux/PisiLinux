#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown -R nginx:nginx /var/lib/nginx")
    os.system("/bin/chown -R nginx:nginx /var/log/nginx")
