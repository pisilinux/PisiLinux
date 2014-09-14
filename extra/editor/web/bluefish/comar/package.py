#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/xmlcatalog  --noout \
            --add 'public' 'Bluefish/DTD/Bflang' 'bflang.dtd' \
            --add 'system' 'http://bluefish.openoffice.nl/DTD/bflang.dtd' 'bflang.dtd' \
            --add 'rewriteURI' 'http://bluefish.openoffice.nl/DTD' '/usr/share/xml/bluefish-unstable' \
            /etc/xml/catalog")

def preRemove():
    os.system("/usr/bin/xmlcatalog  --noout \
            --del 'Bluefish/DTD/Bflang' \
            --del 'http://bluefish.openoffice.nl/DTD/bflang.dtd' \
            --del 'http://bluefish.openoffice.nl/DTD' \
            /etc/xml/catalog")

