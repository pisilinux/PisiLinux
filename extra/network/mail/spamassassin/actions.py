#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir="Mail-SpamAssassin-%s" % get.srcVERSION()

def setup():

    perlmodules.configure('BUILD_SPAMC="yes" \
                           ENABLE_SSL="yes" \
                           CONTACT_ADDRESS="root@localhost" \
                           SYSCONFDIR=/etc \
                           DATADIR=/usr/share/spamassassin')

def build():
    perlmodules.make()

def install():
    perlmodules.install()

    pisitools.dodoc("README", "MANIFEST", "Changes")
    pisitools.dodir("/var/lib/spamd")
