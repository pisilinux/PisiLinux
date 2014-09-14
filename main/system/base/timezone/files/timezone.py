#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

# Extracts the timezone information from /etc/localtime using
# timezone db from this package.
# Ozan Caglayan <ozan_at_pardus.org.tr> 2009

import os
import sys
import cPickle
from hashlib import sha1

zonedict = "/usr/share/zoneinfo/zoneinfo.dict"

if __name__ == "__main__":
    if os.path.exists(zonedict) and os.path.exists("/etc/localtime"):
        tzdb = cPickle.Unpickler(open(zonedict, "rb")).load()
        tz = tzdb.get(sha1(open("/etc/localtime", "r").read()).hexdigest(), 'Not found')
        print "%s" % tz
        sys.exit(0)
    else:
        sys.exit(1)
