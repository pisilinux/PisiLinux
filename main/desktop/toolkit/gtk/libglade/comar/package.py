#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("xmlcatalog --noout --add \
              \"system\" \"http://glade.gnome.org/glade-2.0.dtd\" /usr/share/xml/libglade/glade-2.0.dtd")

def preRemove():
    os.system("xmlcatalog --noout --del /usr/share/xml/libglade/glade-2.0.dtd /etc/xml/catalog")
