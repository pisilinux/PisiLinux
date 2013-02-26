#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system('/usr/bin/mateconftool-2 --config-source=xml:merged:/etc/mateconf/mateconf.xml.defaults --direct --load\
              /etc/mateconf/schemas/panel-default-setup.entries')
    os.system('/usr/bin/mateconftool-2 --config-source=xml:merged:/etc/mateconf/mateconf.xml.defaults --direct --load\
              /etc/mateconf/schemas/panel-default-setup.entries /apps/panel')

def preRemove():
    os.system('/usr/bin/mateconftool-2 --config-source=xml:merged:/etc/mateconf/mateconf.xml.defaults --direct --unload\
              /etc/mateconf/schemas/panel-default-setup.entries /apps/panel')
    os.system('/usr/bin/mateconftool-2 --config-source=xml:merged:/etc/mateconf/mateconf.xml.defaults --direct --unload\
              /etc/mateconf/schemas/panel-default-setup.entries')
