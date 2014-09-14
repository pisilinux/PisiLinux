#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "comm-esr31"
MOZAPPDIR= "/usr/lib/thunderbird"

locales = "be  ca  da  de  el  en-US  es-AR  es-ES  fi  fr  hr  hu  it  lt nl  pl  pt-BR  pt-PT  ro  ru  sr  sv-SE  tr  uk".split()
xpidir = "%s/xpi" % get.workDIR()
arch = get.ARCH()
ver = ".".join(get.srcVERSION().split(".")[:3])

def setup():
    pisitools.flags.sub("-ggdb3", "-g")
    pisitools.ldflags.add("-Wl,-rpath,/usr/lib/thunderbird")

    # configure script misdetects the preprocessor without an optimization level
    # https://bugs.archlinux.org/task/34644
    shelltools.system("sed -i '/ac_cpp=/s/$CPPFLAGS/& -O2/' mozilla/configure")

    # LOCALE
    shelltools.system("rm -rf langpack-tb/*/browser/defaults")
    if not shelltools.isDirectory(xpidir): shelltools.makedirs(xpidir)
    for locale in locales:
        shelltools.system("wget -c -P %s ftp://ftp.mozilla.org/pub/mozilla.org/thunderbird/releases/%s/linux-%s/xpi/%s.xpi" % (xpidir, ver, arch, locale))
        shelltools.makedirs("langpack-tb/langpack-%s@thunderbird.mozilla.org" % locale)
        shelltools.system("unzip -uo %s/%s.xpi -d langpack-tb/langpack-%s@thunderbird.mozilla.org" % (xpidir, locale, locale))

    pisitools.dosed(".pisilinux-default-prefs.js", "DISTRIB_ID", get.lsbINFO()["DISTRIB_ID"])
    pisitools.dosed(".pisilinux-default-prefs.js", "DISTRIB_RELEASE", get.lsbINFO()["DISTRIB_RELEASE"])

def build():
    autotools.make("-f client.mk build")

def install():
    autotools.rawInstall("-f client.mk DESTDIR=%s" % get.installDIR())

    # Install fix language packs
    pisitools.insinto("/usr/lib/thunderbird/extensions", "./langpack-tb/*")

   # Install default-prefs.js
    pisitools.insinto("%s/defaults/pref" % MOZAPPDIR, ".pisilinux-default-prefs.js", "all-pisilinux.js")

    # Empty fake files to get Turkish spell check support working
    pisitools.dodir("%s/extensions/langpack-tr@thunderbird.mozilla.org/dictionaries" % MOZAPPDIR)
    shelltools.touch("%s/%s/%s/dictionaries/tr-TR.aff" % (get.installDIR(), MOZAPPDIR, "extensions/langpack-tr@thunderbird.mozilla.org"))
    shelltools.touch("%s/%s/%s/dictionaries/tr-TR.dic" % (get.installDIR(), MOZAPPDIR, "extensions/langpack-tr@thunderbird.mozilla.org"))

    # Install icons
    pisitools.insinto("/usr/share/pixmaps", "other-licenses/branding/thunderbird/mailicon256.png", "thunderbird.png")
    pisitools.insinto("%s/icons" % MOZAPPDIR, "other-licenses/branding/thunderbird/mailicon16.png")

    for s in (16, 22, 24, 32, 48, 256):
        pisitools.insinto("/usr/share/icons/hicolor/%dx%d/apps" % (s,s), "other-licenses/branding/thunderbird/mailicon%d.png" % s, "thunderbird.png")

    # We don't want the development stuff
    pisitools.removeDir("/usr/lib/thunderbird-devel*")
    pisitools.removeDir("/usr/share/idl")
    pisitools.removeDir("/usr/include")

    # Install docs
    pisitools.dodoc("mozilla/LEGAL", "mozilla/LICENSE")