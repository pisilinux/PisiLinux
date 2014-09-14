#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os


def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)


def mark_plugins_exe(d):
    for root, dirs, files in os.walk(d):
        files[:] = [f for f in files if not f.endswith(".svg") and \
                                        not f.endswith(".png")]
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0755)


def setup():
    fixperms(".")
    shelltools.unlinkDir("share/shutter/resources/po/")

    mark_plugins_exe("share/shutter/resources/system/plugins/")

    # These Perl Modules come with shutter package:
    # perl-Sort-Naturally perl-Proc-Simple perl-Net-DBus-Skype
    # perl-File-BaseDir perl-File-DesktopEntry perl-MimeInfo
    #
    # These exist in Pardus 2011 Repositories:
    # perl-X11-Protocol perl-File-Which perl-File-Spec(in perl package)
    #
    # Uncomment these lines when they hit the repositories:
    #
    #for module in ["File", "Net", "Proc", "Sort", "X11"]:
    #    shelltools.unlinkDir("share/shutter/resources/modules/%s" % module)


def install():
    pisitools.dobin("bin/shutter")
    shelltools.copytree("share", "%s/usr" % get.installDIR())
