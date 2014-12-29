#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i 's/\${OIS_LIBRARIES}/${OIS_LIBRARIES} boost_system/g' Common/CMakeLists.txt")
    shelltools.system("sed -i '71 i set(MYGUI_GCC_VISIBILITY_FLAGS "")' CMakeLists.txt")
    cmaketools.configure("\
                          -DCMAKE_SKIP_RPATH=ON \
                          -DCMAKE_SKIP_INSTALL_RPATH=ON \
                          -DMYGUI_INSTALL_SAMPLES=TRUE \
                          -DMYGUI_INSTALL_TOOLS=TRUE \
                          -DMYGUI_INSTALL_DOCS=TRUE \
                          -DMYGUI_INSTALL_MEDIA=TRUE \
                          -DFREETYPE_INCLUDE_DIR=/usr/include/freetype2/ \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DBUILD_SHARED_LIBS=TRUE \
                         ")

def build():
    cmaketools.make()
    cmaketools.make("api-docs")

def install():
    # libMyGUI.OgrePlatform.a ?
    # non-bin files in bin: plugins.cfg, resources.xml? opt?
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dolib_so("lib/libCommon.so.3.2.1")
    pisitools.dosym("libCommon.so.3.2.1", "/usr/lib/libCommon.so")
    pisitools.dosym("libCommon.so.3.2.1", "/usr/lib/libCommon.so.3")

    for files in ["Demo_Colour", "Demo_Console", "Demo_Controllers", "Demo_Gui", "Demo_ItemBox", "Demo_PanelView", "Demo_Picking", "Demo_PluginStrangeButton", "Demo_Pointers", "Demo_RenderBox", "Demo_ScrollView", "Demo_Themes", "FontEditor", "ImageEditor", "LayoutEditor", "SkinEditor", "plugins.cfg", "resources.xml"]:
        shelltools.chmod("%s/usr/bin/%s" % (get.installDIR(), files), 0755)

    pisitools.dohtml("Docs/html")

    pisitools.dodoc("ChangeLog.txt", "COPYING.MIT", "Readme.txt")