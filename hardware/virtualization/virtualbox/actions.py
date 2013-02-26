# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

VBoxLibDir = "/usr/lib/virtualbox"
VBoxDataDir = "/usr/share/virtualbox"
XorgVersion = "113"

def setup():
    pisitools.dosed("LocalConfig.kmk", "__VBOXLIBDIR__", VBoxLibDir)
    pisitools.dosed("LocalConfig.kmk", "__VBOXDATADIR__", VBoxDataDir)

    shelltools.echo("vbox.cfg", "INSTALL_DIR=%s" % VBoxLibDir)

    # TODO: Enable web service when we have soapcpp2
    autotools.rawConfigure("--disable-java \
                            --disable-kmods \
                            --disable-docs \
                            --enable-hardening \
                            --ose \
                            --with-gcc=%s \
                            --with-g++=%s" % (get.CC(), get.CXX()))

def build():
    shelltools.system("source %s/env.sh && kmk" % get.curDIR())

def install():
    pisitools.insinto("/etc/vbox", "vbox.cfg")
    shelltools.chmod("src/VBox/Additions/x11/Installer/98vboxadd-xclient", 0755)
    pisitools.insinto("/usr/bin", "src/VBox/Additions/x11/Installer/98vboxadd-xclient", "VBoxClient-all")
    #pisitools.insinto("/lib/udev/rules.d", "src/VBox/Additions/linux/installer/70-xorg-vboxmouse.rules")
    pisitools.insinto("/usr/share/X11/pci", "src/VBox/Additions/x11/Installer/vboxvideo.ids")
    #pisitools.insinto("/usr/share/X11/xorg.conf.d", "src/VBox/Additions/x11/Installer/50-vboxmouse.conf")

    arch = "amd64" if get.ARCH() == "x86_64" else "x86"
    shelltools.cd("out/linux.%s/release/bin" % arch)

    # libraries installation. The files below are unnecessary files.
    # TODO: change loop and make it more discrete (i.e copying each single file)
    exclude = ("additions", "icons", "nls", "scm", "sdk", "src", "SUP", "vboxkeyboard",
               "VBox.sh", "VBoxSysInfo.sh", "VBoxCreateUSBNode.sh", "VBoxTunctl", "testcase", "tst", "xpidl")

    for _file in shelltools.ls("."):
        if _file.startswith(exclude):
            continue

        print "Installing %s ..." % _file
        pisitools.insinto(VBoxLibDir, _file)

    pisitools.dobin("VBox*.sh", VBoxDataDir)
    pisitools.insinto(VBoxDataDir, "nls")

    # TODO: Add vboxwebsrv when ready
    # Binaries and Wrapper with Launchers
    apps = ("VBoxHeadless", "VBoxManage", "VBoxSDL", "VBoxVRDP", "VirtualBox", "VBoxBalloonCtrl")
    for link in apps:
        pisitools.dosym("../share/virtualbox/VBox.sh", "/usr/bin/%s" % link)

    pisitools.dobin("VBoxTunctl")

    # Desktop file, mimetype file for xml and icon
    pisitools.domove("%s/*.desktop" % VBoxLibDir, "/usr/share/applications")
    pisitools.domove("%s/*.png" % VBoxLibDir, "/usr/share/pixmaps")
    pisitools.domove("%s/*.xml" % VBoxLibDir, "/usr/share/mime/packages")

    # Mimetypes icons
    for size in ["16", "20", "24", "32", "48", "64", "72", "96", "128", "256"]:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/mimetypes" % (size, size),
                          "icons/%sx%s/*.png" % (size, size))

    # Guest additions
    pisitools.dobin("additions/VBoxClient")
    pisitools.dobin("additions/VBoxControl")

    pisitools.dosbin("additions/VBoxService")
    pisitools.dosbin("additions/mount.vboxsf", "/sbin")

    pisitools.insinto("/lib/security", "additions/pam_vbox.so")

    pisitools.dolib("additions/VBoxOGL*")
    pisitools.dosym("../../../VBoxOGL.so", "/usr/lib/xorg/modules/dri/vboxvideo_dri.so")

    pisitools.insinto("/usr/lib/xorg/modules/drivers", "additions/vboxvideo_drv_%s.so" % XorgVersion, "vboxvideo_drv.so")
    #pisitools.insinto("/usr/lib/xorg/modules/input",   "additions/vboxmouse_drv_%s.so" % XorgVersion, "vboxmouse_drv.so")

    # Python bindings
    pisitools.insinto("%s/sdk/bindings/xpcom" % VBoxLibDir, "sdk/bindings/xpcom/python")

    shelltools.cd("sdk/installer")
    shelltools.copy("vboxapisetup.py", "setup.py")
    shelltools.export("VBOX_INSTALL_PATH", VBoxLibDir)
    pythonmodules.install()
