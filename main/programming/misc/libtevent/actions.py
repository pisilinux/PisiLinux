#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

jobs = get.makeJOBS().replace("-j", "")

def setup():
    autotools.configure("\
                         --builtin-libraries=replace \
                         --bundled-libraries=NONE \
                         --disable-rpath \
                        ")

def build():
    autotools.make("JOBS=%s" % jobs)

def install():
    autotools.rawInstall("DESTDIR=%s JOBS=%s" % (get.installDIR(), jobs))

#    pisitools.remove("/usr/lib/*.a")

    # Create symlinks for so file
#    pisitools.dosym("libtevent.so.%s" % get.srcVERSION(), "/usr/lib/libtevent.so.%s" % get.srcVERSION().split(".")[0])
#    pisitools.dosym("libtevent.so.%s" % get.srcVERSION(), "/usr/lib/libtevent.so")
