#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="rsync-%s" % get.srcVERSION().replace('_','')

def setup():
    autotools.configure("--disable-debug \
                         --with-rsyncd-conf=/etc/rsyncd.conf \
                         --enable-acl-support \
                         --enable-attr-support \
                         --without-included-popt \
                         --enable-ipv6")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("NEWS","README","TODO")
