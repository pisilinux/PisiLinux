# -*- coding: utf-8 -*-
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.

# ActionsAPI Modules
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

basename = "kde5"

prefix = "/%s" % get.defaultprefixDIR()
libdir = "%s/lib" % prefix
bindir = "%s/bin" % prefix
libexecdir = "%s/lib" % prefix
iconsdir = "%s/share/icons" % prefix
applicationsdir = "%s/share/applications/%s" % (prefix, basename)
mandir = "/%s" % get.manDIR()
sharedir = "%s/share/kf5" % prefix
localedir = "%s/share/locale" % prefix
qmldir = "%s/lib/qt5/qml" % prefix
plugindir = "%s/lib/qt5/plugins" % prefix
moduledir = "%s/lib/qt5/mkspecs/modules" % prefix
pythondir = "%s/bin/python3" % prefix
appsdir = "%s/apps" % sharedir
configdir = "%s/config" % sharedir
sysconfdir= "/etc"
servicesdir = "%s/services" % sharedir
servicetypesdir = "%s/servicetypes" % sharedir
includedir = "%s/include/KF5" % prefix
docdir = "/%s/%s" % (get.docDIR(), basename)
htmldir = "%s/html" % docdir
wallpapersdir = "%s/share/wallpapers" % prefix

def configure(parameters = '', installPrefix = prefix, sourceDir = '..'):
    ''' parameters -DLIB_INSTALL_DIR="hede" -DSOMETHING_USEFUL=1'''

    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DDATA_INSTALL_DIR:PATH=%s \
            -DINCLUDE_INSTALL_DIR:PATH=%s \
            -DCONFIG_INSTALL_DIR:PATH=%s \
            -DLIBEXEC_INSTALL_DIR:PATH=%s \
            -DLOCALE_INSTALL_DIR:PATH=%s \
            -DQML_INSTALL_DIR:PATH=%s \
            -DPLUGIN_INSTALL_DIR:PATH=%s \
            -DECM_MKSPECS_INSTALL_DIR:PATH=%s \
            -DPYTHON_EXECUTABLE:PATH=%s \
            -DSYSCONF_INSTALL_DIR:PATH=%s \
            -DHTML_INSTALL_DIR:PATH=%s \
            -DMAN_INSTALL_DIR:PATH=%s \
            -DCMAKE_SKIP_RPATH:BOOL=ON \
            -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
            -DBUILD_TESTING=OFF \
            -DCMAKE_BUILD_TYPE=Release \
            -DLIB_INSTALL_DIR:PATH=%s %s" % (appsdir, includedir, configdir, libexecdir, localedir, qmldir, plugindir, moduledir, pythondir, sysconfdir, htmldir, mandir, libdir, parameters), installPrefix, sourceDir)

    shelltools.cd("..")

def make(parameters = ''):
    cmaketools.make('-C build %s' % parameters)

def install(parameters = '', argument = 'install'):
    cmaketools.install('-C build %s' % parameters, argument)

