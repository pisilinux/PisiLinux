#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "comm-esr17"
MOZAPPDIR= "/usr/lib/MozillaThunderbird"

#locales = ["da", "de", "es-AR", "es-ES", "fr", "hu", "it", "nl", "pl", "pt-BR", "ru",]

def setup():
    # Use autoconf 2.13, pff
    shelltools.chmod("autoconf-213/autoconf-2.13", 0755)

    # Set job count for make
    pisitools.dosed(".mozconfig", "%%JOBS%%", get.makeJOBS())

    pisitools.dosed(".pardus-default-prefs.js", "DISTRIB_ID", get.lsbINFO()["DISTRIB_ID"])
    pisitools.dosed(".pardus-default-prefs.js", "DISTRIB_RELEASE", get.lsbINFO()["DISTRIB_RELEASE"])

def build():
    autotools.make("-f client.mk build")

    #for locale in locales:
        #autotools.make("-C mail/locales langpack-%s" % locale)
        #pisitools.copy("mozilla/dist/xpi-stage/locale-%s/chrome/%s.manifest" % (locale, locale), "mozilla/dist/bin/chrome/")

    # Build enigmail
    """
    shelltools.cd("mailnews/extensions/enigmail")
    shelltools.system("./makemake -r")
    autotools.make()
    autotools.make("xpi")
    """

def install_enigmail():
    # Install enigmail
    pisitools.insinto(MOZAPPDIR, "mozilla/dist/bin/enigmail-*.xpi")

    enigmail_dir = "mozilla/extensions/{3550f703-e582-4d05-9a08-453d09bdfdc6}/{847b3a00-7ab1-11d4-8f02-006008948af5}"
    pisitools.dodir("%s/%s" % (MOZAPPDIR, enigmail_dir))

    old_dir = get.curDIR()

    shelltools.cd("%s/%s/%s" % (get.installDIR(), MOZAPPDIR, enigmail_dir))
    shelltools.system("unzip %s/%s/enigmail-*.xpi" % (get.installDIR(), MOZAPPDIR))
    shelltools.cd(old_dir)

    # Remove unwanted build artifacts from enigmail
    for f in ("enigmail.jar", "enigmail-locale.jar", "enigmail-en-US.jar", "enigmail-skin.jar", "installed-chrome.txt", "enigmime.jar"):
        pisitools.remove("%s/chrome/%s" % (MOZAPPDIR, f))

    for f in ("libenigmime.so", "ipc.xpt", "enig*"):
        pisitools.remove("%s/components/%s" % (MOZAPPDIR, f))

    pisitools.removeDir("%s/defaults/preferences" % MOZAPPDIR)
    pisitools.removeDir("%s/platform" % MOZAPPDIR)
    pisitools.removeDir("%s/wrappers" % MOZAPPDIR)
    pisitools.removeDir("%s/enigmail*.xpi" % MOZAPPDIR)


def install():
    pisitools.insinto("/usr/lib/", "mozilla/dist/bin", "MozillaThunderbird", sym=False)

    # Install language packs
    #for locale in locales:
        #pisitools.insinto("/usr/lib/MozillaThunderbird/extensions/langpack-%s@thunderbird.mozilla.org" % locale, "mozilla/dist/xpi-stage/locale-%s/*" % locale, sym=False)
        
    # Install fix language packs
    pisitools.insinto("/usr/lib/MozillaThunderbird/extensions", "./langpack-tb/*")
   
   # Install default-prefs.js
    pisitools.insinto("%s/defaults/pref" % MOZAPPDIR, ".pardus-default-prefs.js", "all-pardus.js")
    
    # Empty fake files to get Turkish spell check support working
    #pisitools.dodir("%s/extensions/langpack-tr@thunderbird.mozilla.org/dictionaries" % MOZAPPDIR)
    #shelltools.touch("%s/%s/%s/dictionaries/tr-TR.aff" % (get.installDIR(), MOZAPPDIR, "extensions/langpack-tr@thunderbird.mozilla.org"))
    #shelltools.touch("%s/%s/%s/dictionaries/tr-TR.dic" % (get.installDIR(), MOZAPPDIR, "extensions/langpack-tr@thunderbird.mozilla.org"))
    
    pisitools.removeDir("%s/dictionaries" % MOZAPPDIR)
    pisitools.dosym("/usr/share/hunspell", "%s/dictionaries" % MOZAPPDIR)

    # Remove useless file
    pisitools.remove("/usr/lib/MozillaThunderbird/.purgecaches")

    # Remove this to avoid spellchecking dictionary detection problems
    #pisitools.remove("/usr/lib/MozillaThunderbird/defaults/pref/all-l10n.js")

    # Install icons
    pisitools.insinto("/usr/share/pixmaps", "other-licenses/branding/thunderbird/mailicon256.png", "thunderbird.png")
    pisitools.insinto("%s/icons" % MOZAPPDIR, "other-licenses/branding/thunderbird/mailicon16.png")

    for s in (16, 22, 24, 32, 48, 256):
        pisitools.insinto("/usr/share/icons/hicolor/%dx%d/apps" % (s,s), "other-licenses/branding/thunderbird/mailicon%d.png" % s, "thunderbird.png")

    # Install docs
    pisitools.dodoc("mozilla/LEGAL", "mozilla/LICENSE")
