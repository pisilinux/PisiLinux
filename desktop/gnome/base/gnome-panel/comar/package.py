#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system('/usr/bin/gconftool-2 --direct --config-source=xml:merged:/etc/gconf/gconf.xml.defaults\
              --load /etc/gconf/schemas/panel-default-setup.entries')
    os.system('/usr/bin/gconftool-2 --direct --config-source=xml:merged:/etc/gconf/gconf.xml.defaults\
              --load /etc/gconf/schemas/panel-default-setup.entries /apps/panel')

def preRemove():
    os.system('/usr/bin/gconftool-2 --direct --config-source=xml:merged:/etc/gconf/gconf.xml.defaults\
              --unload /etc/gconf/schemas/panel-default-setup.entries /apps/panel')
    os.system('/usr/bin/gconftool-2 --direct --config-source=xml:merged:/etc/gconf/gconf.xml.defaults\
              --unload /etc/gconf/schemas/panel-default-setup.entries')
