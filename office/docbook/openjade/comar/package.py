#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/install-catalog --add /etc/sgml/openjade.cat \
               /usr/share/sgml/openjade/catalog")
    os.system("/usr/bin/install-catalog --add /etc/sgml/openjade.cat \
              /usr/share/sgml/openjade/dsssl/catalog")
    os.system("/usr/bin/install-catalog --add /etc/sgml/sgml-docbook.cat \
               /etc/sgml/openjade.cat")

def preRemove():
    os.system("/usr/bin/install-catalog --remove /etc/sgml/openjade.cat \
               /usr/share/sgml/openjade/catalog")
    os.system("/usr/bin/install-catalog --remove /etc/sgml/openjade.cat \
              /usr/share/sgml/openjade/dsssl/catalog")
    os.system("/usr/bin/install-catalog --remove /etc/sgml/sgml-docbook.cat \
               /etc/sgml/openjade.cat")
