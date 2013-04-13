#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pisi.actionsapi import pisitools

WorkDir = "."

def install():
	pisitools.dobin('pisilinux-dnsmasq')
