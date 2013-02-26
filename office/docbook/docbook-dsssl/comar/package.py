#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/install-catalog --add /etc/sgml/dsssl-docbook-stylesheets.cat \
               /usr/share/sgml/docbook/dsssl-stylesheets-1.79/catalog")
    os.system("/usr/bin/install-catalog --add /etc/sgml/dsssl-docbook-stylesheets.cat \
               /usr/share/sgml/docbook/dsssl-stylesheets-1.79/common/catalog")
    os.system("/usr/bin/install-catalog --add /etc/sgml/sgml-docbook.cat \
               /etc/sgml/dsssl-docbook-stylesheets.cat")

def preRemove():
        os.system("/usr/bin/install-catalog --remove /etc/sgml/dsssl-docbook-stylesheets.cat \
                   /usr/share/sgml/docbook/dsssl-stylesheets-1.79/catalog")
        os.system("/usr/bin/install-catalog --remove /etc/sgml/dsssl-docbook-stylesheets.cat \
                   /usr/share/sgml/docbook/dsssl-stylesheets-1.79/common/catalog")
        os.system("/usr/bin/install-catalog --remove /etc/sgml/sgml-docbook.cat \
                   /etc/sgml/dsssl-docbook-stylesheets.cat")
