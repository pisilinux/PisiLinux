#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="live"

def setup():
    shelltools.system("./genMakefiles shared")

def build():
    # http://bugs.gentoo.org/show_bug.cgi?id=247844
    autotools.make('-j1 LINK_OPTS="-L. %s"' % get.LDFLAGS().replace("-Wl,--as-needed",""))

def install():
    for directory in ["BasicUsageEnvironment", "groupsock", "liveMedia", "UsageEnvironment"]:
        pisitools.insinto("/usr/include/%s" % directory, "%s/include/*" % directory)
        pisitools.insinto("/usr/lib/", "%s/*.so" % directory)

    pisitools.dodoc("README", "COPYING")