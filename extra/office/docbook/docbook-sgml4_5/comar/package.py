#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/install-catalog --add /etc/sgml/sgml-docbook-4.5.cat \
               /usr/share/sgml/docbook/sgml-dtd-4.5/catalog")
    os.system("/usr/bin/install-catalog --add /etc/sgml/sgml-docbook-4.5.cat \
               /etc/sgml/sgml-docbook.cat")

def preRemove():
    os.system("/usr/bin/install-catalog --remove /etc/sgml/sgml-docbook-4.5.cat \
               /usr/share/sgml/docbook/sgml-dtd-4.5/catalog")
    os.system("/usr/bin/install-catalog --remove /etc/sgml/sgml-docbook-4.5.cat \
               /etc/sgml/sgml-docbook.cat")
