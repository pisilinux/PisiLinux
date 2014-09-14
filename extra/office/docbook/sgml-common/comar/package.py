#!/usr/bin/python

import os
import shutil

def postInstall(fromVersion, fromRelease, toVersion, toRelease):

    os.system("/usr/bin/install-catalog --add \
                      /etc/sgml/sgml-ent.cat \
                      /usr/share/sgml/sgml-iso-entities-8879.1986/catalog")

    os.system("/usr/bin/install-catalog --add \
                     /etc/sgml/sgml-docbook.cat \
                     /etc/sgml/sgml-ent.cat")

def postRemove():

    os.system("/usr/bin/install-catalog --remove \
                      /etc/sgml/sgml-ent.cat \
                      /usr/share/sgml/sgml-iso-entities-8879.1986/catalog")

    os.system("/usr/bin/install-catalog --remove \
                     /etc/sgml/sgml-docbook.cat \
                     /etc/sgml/sgml-ent.cat")

