#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system('/usr/bin/xmlcatalog --noout --add "public" \
               "-//OMF//DTD Scrollkeeper OMF Variant V1.0//EN" \
               "file:///usr/share/xml/scrollkeeper/dtds/scrollkeeper-omf.dtd" \
               /etc/xml/docbook')

def preRemove():
    os.system('/usr/bin/xmlcatalog --noout --del \
               "file:///usr/share/xml/scrollkeeper/dtds/scrollkeeper-omf.dtd" \
               /etc/xml/docbook')
