#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

BASEDIR = "/opt/tomcat7"

def install():
    pisitools.dodir(BASEDIR)
    pisitools.insinto(BASEDIR, "./*")

    docs = ("LICENSE", "NOTICE", "RELEASE-NOTES")
    for i in docs:
        pisitools.dodoc(i)
        pisitools.remove("%s/%s" % (BASEDIR, i))

    # Remove redundant .bat files
    pisitools.remove("%s/bin/*.bat" % BASEDIR)

    # Reach the log files from standard log dir /var/log
    pisitools.dosym("/opt/tomcat7/logs", "/var/log/tomcat7")
