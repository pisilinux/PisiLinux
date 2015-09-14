#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "mozilla-release"
ObjDir = "build"
locales = "az be  bs ca  da  de  el  en-US en-GB en-ZA  es-AR  es-CL  es-ES  fi  fr  hr  hu  it  lt nl  pl  pt-BR  pt-PT  ro  ru  sr  sv-SE  tr  uk".split()
xpidir = "%s/xpi" % get.workDIR()
arch = get.ARCH()
ver = ".".join(get.srcVERSION().split(".")[:3])

shelltools.export("SHELL", "/bin/sh")

def setup():
    # Google API key
    shelltools.echo("google_api_key", "AIzaSyBINKL31ZYd8W5byPuwTXYK6cEyoceGh6Y")
    pisitools.dosed(".mozconfig", "%%PWD%%", get.curDIR())
    pisitools.dosed(".mozconfig", "%%FILE%%", "google_api_key")
    pisitools.dosed(".mozconfig", "##JOBCOUNT##", get.makeJOBS())

    # LOCALE
    shelltools.system("rm -rf langpack-ff/*/browser/defaults")
    if not shelltools.isDirectory(xpidir): shelltools.makedirs(xpidir)
    for locale in locales:
        shelltools.system("wget -c -P %s http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%s/linux-%s/xpi/%s.xpi" % (xpidir, ver, arch, locale))
        shelltools.makedirs("langpack-ff/langpack-%s@firefox.mozilla.org" % locale)
        shelltools.system("unzip -uo %s/%s.xpi -d langpack-ff/langpack-%s@firefox.mozilla.org" % (xpidir, locale, locale))
        print "Replacing browser.properties for %s locale" % locale
        shelltools.copy("browserconfig.properties", "langpack-ff/langpack-%s@firefox.mozilla.org/browser/chrome/%s/locale/branding/" % (locale, locale))
        shelltools.copy("browserconfig.properties", "browser/branding/official/locales/")

    shelltools.makedirs(ObjDir)
    shelltools.cd(ObjDir)
    shelltools.system("../configure --prefix=/usr --libdir=/usr/lib --disable-strip --disable-install-strip")
    shelltools.system("sed -i '/^ftglyph.h/ i ftfntfmt.h' ../config/system-headers")
    

def build():
    shelltools.cd(ObjDir)
    autotools.make("-f ../client.mk build")

def install():
    autotools.rawInstall("-f client.mk DESTDIR=%s INSTALL_SDK= install" % get.installDIR())

    # Install language packs
    pisitools.insinto("/usr/lib/firefox/browser/extensions", "./langpack-ff/*")

    # Create profile dir, we'll copy bookmarks.html in post-install script
    pisitools.dodir("/usr/lib/firefox/browser/defaults/profile")

    # Install branding icon
    pisitools.insinto("/usr/share/pixmaps", "browser/branding/official/default256.png", "firefox.png")
    
    # Install docs
    pisitools.dodoc("LEGAL", "LICENSE")