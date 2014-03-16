#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("JOBS", get.makeJOBS().replace("-j", ""))

def setup():
    shelltools.system("python waf configure --program-name=Ardour3 --prefix=/usr \
                                  --freedesktop \
                                  --lv2 \
                                  --lv2-system \
                                  --lxvst \
                                  --nls \
                                  --noconfirm \
                                  --no-phone-home \
                                  --optimize \
                                  --docs \
                                  --libdir=/usr/lib/ \
                                  --configdir=/etc \
                                  --datadir=/usr/share \
                                  --docdir=/usr/share/doc \
                                  --mandir=/usr/share/man \
                                  --includedir=/usr/include")

def build():
    shelltools.system("python waf build -v")
    shelltools.system("python waf i18n -v")

def install():
    shelltools.system("DESTDIR=%s python waf install" % get.installDIR())

    pisitools.dodoc("COPYING", "README")
