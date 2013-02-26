#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    for com in [ "bcc86", "unproto", "copt", "as86", "ld86",
                 "-C cpp", "-C ar", "-C ld" ]:
        make_opts = { 'cflags' : get.CFLAGS(),
                      'com'    : com }

        autotools.make('%(com)s CFLAGS="%(cflags)s -D_POSIX_SOURCE" -j1' % make_opts)

    # ncc does not support gcc optflags
    autotools.make('-j1')

def install():
    for binary in ["bin/*","cpp/bcc-cpp","bcc/bcc-cc1"]:
        pisitools.dobin(binary)

    pisitools.rename("/usr/bin/Bcc","bcc")

    pisitools.doman("man/*.1")
    pisitools.dodoc("Changes","COPYING","MAGIC","README")
