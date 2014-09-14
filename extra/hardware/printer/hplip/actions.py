#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

def setup():
    # Patch compressed PPDs
    for patch in sorted(os.listdir("ppd-patches")):
        shelltools.system("./patch-ppds ppd-patches/%s" % patch)

    for f in ("NEWS", "INSTALL", "README", "AUTHORS", "ChangeLog"):
        shelltools.touch(f)

    pisitools.dosed("Makefile.am", "^rulesdir = .*$", "rulesdir = /lib/udev/rules.d")

    # Migrate device ids from hpcups drv to hpijs drv
    shelltools.system("./copy-deviceids prnt/drv/hpcups.drv.in prnt/drv/hpijs.drv.in > hpijs.drv.in.new")
    shelltools.move("hpijs.drv.in.new", "prnt/drv/hpijs.drv.in")

    # Strip duplex constraints from hpcups
    pisitools.dosed("prnt/drv/hpcups.drv.in", "(UIConstraints.* \*Duplex)", "//\\1")

    # Change python shebang
    shelltools.system("find -name '*.py' -print0 | xargs -0 sed -i 's,^#!/usr/bin/env python,#!/usr/bin/python,'")

    # These are barely the defaults except:
    # --enable-foomatic-drv-install (default=no) (respected by Fedora, enabled by Ubuntu)
    autotools.autoreconf("-fi")
    autotools.configure("--with-cupsbackenddir=/usr/lib/cups/backend \
                         --with-drvdir=/usr/share/cups/drv \
                         --with-hpppddir=/usr/share/cups/model/hplip \
                         --with-docdir=/usr/share/doc/hplip \
                         --with-mimedir=/usr/share/cups/mime \
                         --enable-qt4 \
                         --enable-hpijs-install \
                         --enable-udev-acl-rules \
                         --enable-pp-build \
                         --enable-fax-build \
                         --enable-gui-build \
                         --enable-dbus-build \
                         --enable-scan-build \
                         --enable-network-build \
                         --enable-hpcups-install \
                         --enable-cups-drv-install \
                         --enable-foomatic-drv-install \
                         --disable-qt3 \
                         --disable-policykit \
                         --disable-doc-build \
                         --disable-foomatic-ppd-install \
                         --disable-foomatic-rip-hplip-install")

    # Remove hardcoded rpaths
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s ppddir=/usr/share/cups/model/hplip" % get.installDIR())

    # Create a compatibility symlink for foomatic-rip-hplip
    pisitools.dosym("/usr/lib/cups/filter/foomatic-rip", "/usr/lib/cups/filter/foomatic-rip-hplip")
    
    # Remove the hal preprobe rules as they were causing breakage (bug #479648).
    # Remove hal directory as well.
    pisitools.removeDir("/usr/share/hal/")

    # Remove unpackaged stuff (Fedora)
    #pisitools.remove("/usr/share/hplip/fax/pstotiff*")
    #pisitools.remove("/usr/share/cups/mime/pstotiff.types")
    #pisitools.remove("/usr/share/hplip/pkservice.py")
    #pisitools.remove("/usr/bin/hp-pkservice")
    

    # Do not mess with sane, init, foomatic etc.
    pisitools.removeDir("/etc/sane.d")

    # Create empty plugins directory
    pisitools.dodir("/usr/share/hplip/prnt/plugins")
    
    # This notifies user through libnotify when the printer requires a firmware
    # Should port it to KNotify if possible, argh.
    pisitools.remove("/lib/udev/rules.d/56-hpmud.rules")

    # --disable-doc-build used. It doesn't go to the true directory.
    pisitools.dohtml("doc/*")
