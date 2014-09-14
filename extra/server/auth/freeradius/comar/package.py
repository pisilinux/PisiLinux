#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown -R radiusd:radiusd /var/log/radius")
    os.system("/bin/chown -R radiusd:radiusd /run/radiusd")

    os.system("/bin/chown -R root:radiusd /etc/raddb")
    os.system("/bin/chgrp -R radiusd /etc/raddb/certs/*")

    # Run the bootstrap script to create the certificate if not exists (pb#18531)
    if not os.path.exists("/etc/raddb/certs/server.pem"):
        os.system("/etc/raddb/certs/bootstrap")
