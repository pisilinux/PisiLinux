#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "chromium-%s" % get.srcVERSION()

shelltools.export("HOME", get.workDIR())

ARCH = "x64" if get.ARCH() == "x86_64" else "ia32"

def setup():
    # use_system_ssl is disabled -->  https://bugzilla.mozilla.org/show_bug.cgi?id=547312
    # use_system_icu is disabled --> http://crbug.com/103360
    # use_system_hunspell has build problems, upstream changes needed
    # use_system_sqlite is disabled --> http://crbug.com/22208
    # use_system_ffmpeg has build problems, system libraries might be outdated

    # We add -fno-ipa-cp to CFLAGS. See: http://crbug.com/41887
    shelltools.system("build/gyp_chromium -f make build/all.gyp --depth=. \
                        -Dgcc_version=45 \
                        -Dno_strict_aliasing=1 \
                        -Dwerror= \
                        -Dlinux_strip_binary=1 \
                        -Dlinux_sandbox_path=/usr/lib/chromium-browser/chromium-sandbox \
                        -Dlinux_sandbox_chrome_path=/usr/lib/chromium-browser/chromium-browser \
                        -Drelease_extra_cflags=-fno-ipa-cp \
                        -Dproprietary_codecs=1 \
                        -Dinclude_pulse_audio=1 \
                        -Duse_system_bzip2=1 \
                        -Duse_system_libpng=1 \
                        -Duse_system_libevent=1 \
                        -Duse_system_libjpeg=1 \
                        -Duse_system_libxslt=1 \
                        -Duse_system_libexpat=1 \
                        -Duse_system_libxml=1 \
                        -Duse_system_libwebp=0 \
                        -Duse_system_speex=1 \
                        -Duse_system_zlib=0 \
                        -Duse_system_flac=1 \
                        -Duse_system_vpx=0 \
                        -Duse_system_xdg_utils=1 \
                        -Duse_system_yasm=1 \
                        -Duse_system_ssl=0 \
                        -Duse_system_icu=0 \
                        -Ddisable_sse2=1 \
                        -Ddisable_nacl=1 \
                        -Dtarget_arch=%s" % ARCH)

def build():
    autotools.make("chrome chrome_sandbox BUILDTYPE=Release V=1")

def install():
    shelltools.cd("out/Release")

    shelltools.makedirs("%s/usr/lib/chromium-browser" % get.installDIR())

    pisitools.insinto("/usr/lib/chromium-browser", "chrome.pak")
    pisitools.insinto("/usr/lib/chromium-browser", "resources.pak")
    pisitools.insinto("/usr/lib/chromium-browser", "chrome_100_percent.pak")
    pisitools.insinto("/usr/lib/chromium-browser", "content_resources.pak")
    pisitools.insinto("/usr/lib/chromium-browser", "chrome_remote_desktop.pak")
    pisitools.insinto("/usr/lib/chromium-browser", "chrome", "chromium-browser")
    pisitools.insinto("/usr/lib/chromium-browser", "chrome_sandbox", "chromium-sandbox")
    
    # We need to set SUID otherwise it will not run
    shelltools.chmod("%s/usr/lib/chromium-browser/chromium-sandbox" % get.installDIR(), 04755)

    pisitools.insinto("/usr/lib/chromium-browser", "locales")
    pisitools.insinto("/usr/lib/chromium-browser", "resources")

    # Internal ffmpeg libraries
    pisitools.insinto("/usr/lib/chromium-browser", "libffmpegsumo.so")

    # Nacl plugin
    # pisitools.insinto("/usr/lib/chromium-browser", "libppGoogleNaClPluginChrome.so")

    pisitools.newman("chrome.1", "chromium-browser.1")

    # Chromium looks for these in its folder
    # See media_posix.cc and base_paths_linux.cc
    #for lib in ["libavcodec.so.52" , "libavformat.so.52", "libavutil.so.50"]:
    #    shelltools.sym("/usr/lib/%s" % lib, "%s/usr/lib/chromium-browser/%s" % (get.installDIR(), lib))


    shelltools.cd("../..")
    for size in ["22", "24", "48", "64", "128", "256"]:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" %(size, size), "chrome/app/theme/chromium/product_logo_%s.png" % size, "chromium-browser.png")

    pisitools.dosym("/usr/share/icons/hicolor/256x256/apps/chromium-browser.png", "/usr/share/pixmaps/chromium-browser.png")

