#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def install():
    pisitools.insinto("/usr/share/icons", "kfaenza")
    shelltools.system("wget -q http://kde-look.org/CONTENT/content-files/153813-kfaenza-icon-patch-0.3.tar.gz -P /tmp")
    shelltools.system("tar -zxvf /tmp/153813-kfaenza-icon-patch-0.3.tar.gz -C %s/usr/share/icons/kfaenza" % get.installDIR())
    
    pisitools.dosym("/usr/share/icons/kfaenza/actions/16/application-exit.png", "/usr/share/icons/kfaenza/actions/16/cancel.png")
    pisitools.dosym("/usr/share/icons/kfaenza/actions/22/application-exit.png", "/usr/share/icons/actions/kfaenza/22/cancel.png")
    pisitools.dosym("/usr/share/icons/kfaenza/actions/32/application-exit.png", "/usr/share/icons/actions/kfaenza/32/cancel.png")
    pisitools.dosym("/usr/share/icons/kfaenza/actions/48/application-exit.png", "/usr/share/icons/actions/kfaenza/48/cancel.png")
