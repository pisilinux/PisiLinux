#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.cd("configure")
    shelltools.system("python configure.py \
                       -I/usr/qt/4/include/qwt \
                       --sip-include-dirs=/usr/include/%s \
                       --module-install-path=/usr/lib/%s/site-packages/PyQt4/Qwt5 \
                       --qwt-sources=../qwt-5.2 \
                       --qt4" % (get.curPYTHON(), get.curPYTHON()))

def build():
    shelltools.cd("configure")
    autotools.make()

def install():
    qwt_lib_dir = "/usr/lib/%s/site-packages/PyQt4/Qwt5" % get.curPYTHON()

    shelltools.cd("configure/iqt5qt4")

    pisitools.dolib("_iqt.so", qwt_lib_dir)

    shelltools.cd("../qwt5qt4")
    pisitools.dolib("Qwt.so", qwt_lib_dir)

    pisitools.insinto(qwt_lib_dir, "*.py")

    pisitools.insinto("/usr/share/sip/PyQt4/Qwt5", "../../sip/qwt5qt4/*.sip")

    pisitools.insinto("%s/PyQwt/examples" % get.docDIR(), "../../qt4examples/*")

    pisitools.dodoc("../../ANNOUNCEMENT-%s" % get.srcVERSION(), "../../README", "../../COPYING")
