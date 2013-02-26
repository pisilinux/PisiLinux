#!    pisitools.remove("/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import get

#WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().replace("_", "-"))
shelltools.export("HOME", get.workDIR())

def setup():
    # This docbook is buggy
    # pisitools.dosed("doc-translations/CMakeLists.txt", "^(add_subdirectory\( pt_digikam/digikam \))$", "#\\1")

    kde4.configure("-DDIGIKAMSC_COMPILE_DOC=on \
                    -DDIGIKAMSC_CHECKOUT_PO=on \
                    -DDIGIKAMSC_COMPILE_PO=on")

def build():
    kde4.make()

def install():
    kde4.install()

    """
    for d in ["sv"]:
        pisitools.remove("/usr/share/kde4/doc/HTML/%s/%s/common" % (d, get.srcNAME()))
        pisitools.dosym("/usr/share/kde4/doc/HTML/en/common", "/usr/share/kde4/doc/HTML/%s/%s/common" % (d, get.srcNAME()))
    """

    pisitools.dodoc("NEWS", "README")
    
    pisitools.remove("/usr/share/icons/hicolor/64x64/apps/kdcraw.png")
    pisitools.remove("/usr/lib/libksane.so.0")
    pisitools.remove("/usr/lib/libkipi.so.10.0.0")
    pisitools.remove("/usr/lib/libkdcraw.so")
    pisitools.remove("/usr/lib/libkdcraw.so.22")
    pisitools.remove("/usr/share/kde4/apps/kipi/data/kipi-icon.svg")
    pisitools.remove("/usr/bin/kxmlkipicmd")
    pisitools.remove("/usr/share/kde4/apps/libkdcraw/profiles/srgb-d65.icm")
    pisitools.remove("/usr/lib/libkdcraw.so.22.0.0")
    pisitools.remove("/usr/share/kde4/apps/kxmlkipicmd/kxmlkipicmd_defaultui.rc")
    pisitools.remove("/usr/share/kde4/apps/libkdcraw/profiles/prophoto.icm")
    pisitools.remove("/usr/share/icons/hicolor/32x32/apps/kdcraw.png")
    pisitools.remove("/usr/share/kde4/apps/libkdcraw/profiles/applergb.icm")
    pisitools.remove("/usr/share/icons/hicolor/16x16/actions/black-white.png")
    pisitools.remove("/usr/share/kde4/apps/kipi/data/kipi-plugins_logo.png")
    pisitools.remove("/usr/lib/libkexiv2.so")
    pisitools.remove("/usr/lib/libkipi.so")
    pisitools.remove("/usr/share/icons/hicolor/48x48/apps/kdcraw.png")
    pisitools.remove("/usr/share/kde4/apps/kipi/kipiplugin_kxmlhelloworldui.rc")
    pisitools.remove("/usr/lib/kde4/kipiplugin_kxmlhelloworld.so")
    pisitools.remove("/usr/lib/pkgconfig/libkdcraw.pc")
    pisitools.remove("/usr/share/kde4/apps/libkdcraw/profiles/srgb.icm")
    pisitools.remove("/usr/share/icons/hicolor/16x16/apps/kipi.png")
    pisitools.remove("/usr/lib/pkgconfig/libksane.pc")
    pisitools.remove("/usr/share/icons/hicolor/32x32/apps/kipi.png")
    pisitools.remove("/usr/share/kde4/apps/kipi/data/kipi-logo.svg")
    pisitools.remove("/usr/lib/pkgconfig/libkexiv2.pc")
    pisitools.remove("/usr/lib/libksane.so.0.2.0")
    pisitools.remove("/usr/share/kde4/services/kipiplugin_kxmlhelloworld.desktop")
    pisitools.remove("/usr/lib/cmake/KSane/KSaneConfig.cmake")
    pisitools.remove("/usr/lib/libkipi.so.10")
    pisitools.remove("/usr/lib/libkexiv2.so.11")
    pisitools.remove("/usr/share/kde4/apps/libkdcraw/profiles/adobergb.icm")
    pisitools.remove("/usr/share/icons/hicolor/16x16/actions/color.png")
    pisitools.remove("/usr/lib/libksane.so")
    pisitools.remove("/usr/share/icons/hicolor/128x128/apps/kdcraw.png")
    pisitools.remove("/usr/share/icons/hicolor/16x16/actions/gray-scale.png")
    pisitools.remove("/usr/share/icons/hicolor/48x48/apps/kipi.png")
    pisitools.remove("/usr/share/kde4/servicetypes/kipiplugin.desktop")
    pisitools.remove("/usr/share/kde4/apps/libkdcraw/profiles/widegamut.icm")
    pisitools.remove("/usr/share/icons/hicolor/128x128/apps/kipi.png")
    pisitools.remove("/usr/lib/pkgconfig/libkipi.pc")
    pisitools.remove("/usr/share/kde4/apps/libkexiv2/data/topicset.iptc-subjectcode.xml")
    pisitools.remove("/usr/lib/libkexiv2.so.11.1.0")
    pisitools.remove("/usr/share/kde4/apps/kxmlkipicmd/kxmlkipicmd_gwenviewui.rc")
    pisitools.remove("/usr/share/icons/hicolor/22x22/apps/kipi.png")
    pisitools.remove("/usr/include/kde4/libksane/version.h")
    pisitools.remove("/usr/include/kde4/libksane/libksane_export.h")
    pisitools.remove("/usr/include/kde4/libksane/ksane.h")
