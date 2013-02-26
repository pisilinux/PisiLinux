#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2006, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.

import os
import sys
import glob

def main():
    try:
        sys.argv[1]
    except:
        usage()
    else:
        ttf2gs()

def usage():
    print """
    Error:

    Usage:
      ttf2gs    TTF Font Directory  (ttf2gs /usr/share/fonts/dejavu/)
    """
    sys.exit(1)

def ttf2gs():
    for font in glob.glob("%s/*.[tT][tT][fF]" % sys.argv[1]):
        p = os.popen("/usr/bin/ttf2pt1 -A %s - 2> /dev/null" % font)
        o = p.readlines()
        p.close()
        for line in o:
            if line.startswith("FontName"):
                family = line.split("FontName")[1].strip()
                print "/%s (%s);" % (family, font)

if __name__ == "__main__":
    sys.exit(main())
