#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
	autotools.configure()

def build():
	autotools.make()

def install():
	pisitools.dodoc('AUTHORS', 'ChangeLog', 'ChangeLog.pre-0-17',
	                'COPYING', 'HACKING', 'INSTALL', 'NEWS', 'README',
	                'README.I18N', 'README.Packagers', 'THANKS', 'TODO')
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

