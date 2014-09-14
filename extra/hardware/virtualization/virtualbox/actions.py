# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import kerneltools

VBoxLibDir = "/usr/lib/virtualbox"
VBoxDataDir = "/usr/share/virtualbox"
KDIR = kerneltools.getKernelVersion()

def setup():
    #pisitools.dosed("LocalConfig.kmk", "__VBOXLIBDIR__", VBoxLibDir)
    #pisitools.dosed("LocalConfig.kmk", "__VBOXDATADIR__", VBoxDataDir)

    shelltools.echo("vbox.cfg", "INSTALL_DIR=%s" % VBoxLibDir)

    # TODO: Enable web service when we have soapcpp2
    autotools.rawConfigure("\
                             --with-makeself=/usr/bin/echo \
                             --disable-docs \
                             --enable-vde \
                             --enable-vnc \
                             --enable-webservice \
                             --with-linux=/usr/src/linux-headers-%s \
                             --with-gcc=%s \
                             --with-g++=%s \
                           " % (KDIR, get.CC(), get.CXX()))

def build():
    shelltools.system("source %s/env.sh && kmk" % get.curDIR())

def install():
    shelltools.system("awk '$1 ~ /Version:/ { print gensub(/([0-9]+)\.([0-9]+).*/, \"\\\\1\\\\2\", \"g\", $2) }' /usr/lib/pkgconfig/xorg-server.pc > XorgVersion")
    with open("XorgVersion", "r") as f:
        XorgVersion = f.readline().strip()
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

    shelltools.cd("../..")
    mvb_name = "module-virtualbox-%s" % get.srcVERSION()
    mvbg_name = "module-virtualbox-guest-%s" % get.srcVERSION()

    shelltools.copy("src", "%s/%s" % (get.workDIR(), mvb_name))
    shelltools.copy("additions/src", "%s/%s" % (get.workDIR(), mvbg_name))
    shelltools.cd(get.workDIR())
    shelltools.system("tar c %s | xz -9 > %s.tar.xz" % ((mvb_name, )*2))
    shelltools.unlinkDir(mvb_name)
    shelltools.system("tar c %s | xz -9 > %s.tar.xz" % ((mvbg_name, )*2))
    shelltools.unlinkDir(mvbg_name)
