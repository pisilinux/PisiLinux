#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import os

#NoStrip = ["%s/lib/libreoffice/basis-link/share" % AppDir, "%s/lib/libreoffice/share" % AppDir]

shelltools.export("HOME", get.workDIR())
shelltools.export("LDFLAGS", "%s -L/usr/lib/nss" % get.LDFLAGS())
shelltools.export("CXXFLAGS", get.CXXFLAGS().replace("-ggdb3", "-g"))
shelltools.export("ARCH_FLAGS", get.CXXFLAGS())
shelltools.export("LINKFLAGSOPTIMIZE", get.LDFLAGS())
shelltools.export("PYTHON", get.curPYTHON())

langpackdir = "%s-langpack-%s" % (get.srcNAME(), get.srcVERSION())
langpackpath = os.path.normpath("%s/../%s" % (get.installDIR(), langpackdir))
langs = "en-US af ar as bg bn br ca cs cy da de dz el es et eu fa fi fr ga gl gu he hr hu it ja ko kn lt lv mai ml mr nb nl nn nr nso or pa-IN pl pt pt-BR ro ru sh si sk sl sr ss st sv ta te th tn tr ts uk ve xh zh-CN zh-TW zu"
ldirs = ("/usr/lib/libreoffice/help/%s",
         "/usr/lib/libreoffice/share/autotext/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/cui/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/sfx/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/svt/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/svx/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/vcl/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/desktop/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/modules/scalc/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/modules/sdraw/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/modules/smath/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/modules/simpress/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/modules/swriter/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/modules/BasicIDE/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/filter/ui/res/%s",
         "/usr/lib/libreoffice/share/extensions/nlpsolver/help/%s",
         "/usr/lib/libreoffice/share/extensions/wiki-publisher/help/%s")

def setup():
    vars = {"lang": langs,
            "jobs": "1",
            "etar": get.workDIR()}
#            "jobs": get.makeJOBS().replace("-j", ""),

    autotools.aclocal("-I m4")
    autotools.autoconf()
    shelltools.touch("autogen.lastrun")
    autotools.rawConfigure('--with-vendor="Pardus Anka" \
                       --with-unix-wrapper="libreoffice" \
                       --with-ant-home="/usr/share/ant" \
                       --with-jdk-home="/opt/sun-jdk" \
                       --prefix=/usr --exec-prefix=/usr --sysconfdir=/etc \
                       --libdir=/usr/lib --mandir=/usr/share/man \
                       --enable-release-build \
                       --enable-verbose \
                       --disable-dependency-tracking \
                       --disable-rpath \
                       --disable-crashdump \
                       --disable-ccache \
                       --disable-epm \
                       --disable-online-update \
                       --disable-pch \
                       --with-system-jars \
                       --with-system-libs \
                       --with-system-mythes \
                       --with-system-headers \
                       --with-lang="%(lang)s" \
                       --enable-graphite \
                       --enable-cups \
                       --enable-dbus \
                       --enable-evolution2 \
                       --enable-gio \
                       --disable-gnome-vfs \
                       --disable-kde \
                       --enable-kde4 \
                       --enable-gtk3 \
                       --enable-largefile \
                       --enable-lockdown \
                       --enable-mergelibs \
                       --enable-opengl \
                       --enable-odk \
                       --enable-randr \
                       --enable-randr-link \
                       --enable-extension-integration \
                       --enable-scripting-beanshell \
                       --enable-scripting-javascript \
                       --enable-ext-wiki-publisher \
                       --enable-ext-nlpsolver \
                       --disable-ext-report-builder \
                       --disable-ext-mysql-connector \
                       --with-system-mysql \
                       --enable-python=system \
                       --enable-cairo-canvas \
                       --with-system-cairo \
                       --without-fonts \
                       --without-afms \
                       --without-ppds \
                       --with-system-libexttextcat \
                       --without-system-jfreereport \
                       --without-system-apache-commons \
                       --with-helppack-integration \
                       --with-system-beanshell \
                       --with-system-clucene \
                       --with-system-cppunit \
                       --with-system-graphite \
                       --with-system-libcmis \
                       --with-system-libwpg \
                       --with-system-libwps \
                       --with-system-libvisio \
                       --with-system-mdds \
                       --with-system-redland \
                       --with-system-ucpp \
                       --with-system-dicts \
                       --with-system-libexttextcat \
                       --with-system-nss \
                       --without-system-hsqldb \
                       --without-system-mozilla \
                       --without-myspell-dicts \
                       --without-system-npapi-headers \
                       --with-external-dict-dir=/usr/share/hunspell \
                       --with-external-hyph-dir=/usr/share/hyphen \
                       --with-external-thes-dir=/usr/share/mythes \
                       --with-alloc=system \
                       --without-system-sane \
                       --without-system-servlet-api \
                       --without-system-vigra \
                       --without-sun-templates \
                       --disable-fetch-external \
                       --with-parallelism=%(jobs)s \
                       --with-external-tar="%(etar)s"' % vars)
        
def build():
    autotools.make()

def check():
    autotools.make("unitcheck")
    autotools.make("slowcheck")

def install():
    autotools.rawInstall("DESTDIR=%s distro-pack-install -o build -o check" % get.installDIR())
    
    if not shelltools.isDirectory(langpackpath): shelltools.makedirs(langpackpath)
    else: shelltools.unlinkDir(langpackpath)
    for l in langs.split(" "):
        if l == "en-US": continue
        print("processing: %s" % l)
        for ld in ldirs:
            srcd = "%s%s" % (get.installDIR(), ld % l)
            dstd = "%s%s" % (langpackpath, ld % l)
            if shelltools.isDirectory(srcd):
                if not shelltools.isDirectory(dstd): shelltools.makedirs(dstd)
                shelltools.move(srcd, dstd)

        srcf = "%s/usr/share/doc/libreoffice/README_%s" % (get.installDIR(), l)
        dstd = "%s/usr/share/doc/libreoffice" % langpackpath
        dstf = "%s/README_%s" % (dstd, l)
        if shelltools.isFile(srcf):
            if not shelltools.isDirectory(dstd): shelltools.makedirs(dstd)
            shelltools.move(srcf, dstf)

        srcd = "%s/usr/lib/libreoffice/program/resource" % get.installDIR()
        dstd = "%s/usr/lib/libreoffice/program/resource" % langpackpath
        for f in os.listdir(srcd):
            if l == "id" and f.endswith("s%s.res" % l): continue
            elif l == "st" and f.endswith("a%s.res" % l): continue
            elif f.endswith("%s.res" % l):
                if not shelltools.isDirectory(dstd): shelltools.makedirs(dstd)
                shelltools.move("%s/%s" % (srcd, f), dstd)

        for path in ("/usr/lib/libreoffice/share/registry", "/usr/lib/libreoffice/share/registry/res"):
            srcd = "%s%s" % (get.installDIR(), path)
            dstd = "%s%s" % (langpackpath, path)
            for f in os.listdir(srcd):
                if l == "id" and f.endswith("s%s.xcd" % l): continue
                elif l == "ss" and f == "impress.xcd": continue
                elif l == "st" and f.endswith("a%s.xcd" % l): continue
                elif l == "th" and f == "math.xcd": continue
                elif f.endswith("%s.xcd" % l):
                    if not shelltools.isDirectory(dstd): shelltools.makedirs(dstd)
                    shelltools.move("%s/%s" % (srcd, f), dstd)

    for i in ["readmes/README_*", "CREDITS*", "LICENSE*", "NOTICE*"]:
        pisitools.domove("/usr/lib/libreoffice/%s" % i, "/usr/share/doc/libreoffice")
    pisitools.removeDir("/usr/lib/libreoffice/readmes")

    print("creating: %s.tar.xz" % langpackdir)
    shelltools.cd("%s/../" % get.installDIR())
    shelltools.system("tar c %s | xz -9 > %s.tar.xz" % ((langpackdir, )*2))
