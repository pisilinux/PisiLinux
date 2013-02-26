#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("CFLAGS", "%s -fvisibility=hidden" % get.CFLAGS())
shelltools.export("LDFLAGS", "%s -fvisibility=hidden" % get.LDFLAGS())

def setup():
    shelltools.export("AUTOPOINT", "/bin/true")

    autotools.autoreconf()
    autotools.configure("--disable-static \
                         --with-internal-maximum-log-level=3 \
                         --enable-glib \
                         --enable-ecore-x-composite \
                         --enable-ecore-x-damage \
                         --enable-ecore-x-dpms \
                         --enable-ecore-x-randr \
                         --enable-ecore-x-render \
                         --enable-ecore-x-screensaver \
                         --enable-ecore-x-shape \
                         --enable-ecore-x-gesture \
                         --enable-ecore-x-sync \
                         --enable-ecore-x-xfixes \
                         --enable-ecore-x-xinerama \
                         --enable-ecore-x-xprint \
                         --enable-ecore-x-xtest \
                         --enable-ecore-x-cursor \
                         --enable-ecore-x-input \
                         --enable-ecore-x-dri \
                         --enable-epoll \
                         --enable-posix-threads \
                         --disable-debug-threads \
                         --enable-thread-safety \
                         --enable-atfile-source \
                         --enable-ecore-con \
                         --enable-curl \
                         --disable-gnutls \
                         --enable-openssl \
                         --enable-poll \
                         --enable-inotify \
                         --enable-ecore-ipc \
                         --enable-ecore-file \
                         --enable-ecore-imf \
                         --enable-ecore-imf-evas \
                         --enable-ecore-input \
                         --enable-ecore-input-evas \
                         --enable-ecore-imf-xim \
                         --disable-ecore-imf-scim \
                         --disable-ecore-imf-ibus \
                         --enable-ecore-x \
                         --disable-ecore-sdl \
                         --enable-ecore-fb \
                         --disable-ecore-directfb \
                         --enable-ecore-evas \
                         --enable-ecore-evas-software-buffer \
                         --enable-ecore-evas-software-x11 \
                         --enable-ecore-evas-opengl-x11 \
                         --enable-ecore-evas-fb \
                         --disable-ecore-evas-ews \
                         --disable-ecore-timer-dump \
                         --disable-ecore-wayland \
                         --disable-ecore-win32 \
                         --disable-ecore-wince \
                         --disable-ecore-evas-software-gdi \
                         --disable-ecore-evas-software-ddraw \
                         --disable-ecore-evas-direct3d \
                         --disable-ecore-evas-opengl-glew \
                         --disable-ecore-evas-software-16-ddraw \
                         --disable-ecore-evas-software-16-wince \
                         --enable-ecore-evas-directfb \
                         --disable-tests \
                         --disable-coverage \
                         --disable-install-examples \
                         --disable-doc \
                         --disable-rpath \
                         --with-x")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/bin")

    pisitools.dodoc("AUTHORS", "COPYING*", "README")
