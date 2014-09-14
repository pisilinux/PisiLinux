#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# @author: Gökmen Görgen, <gkmngrgn_gmail.com>
#

import comar

link = comar.Link()
link.setLocale()
link.useAgent()

def startService(service):
    link.System.Service[service].start()

def infoService(service):
    return link.System.Service[service].info()[2]

