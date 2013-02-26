#!/usr/bin/python
# -*- coding: utf-8 -*-

import dbus

class DnsMasq:
    bus = None
    obj = None
    iface = None

    def __init__(self):
        self.bus = dbus.SystemBus()
        self.obj = self.bus.get_object("uk.org.thekelleys.dnsmasq", "/uk/org/thekelleys/dnsmasq", introspect=False)
        self.iface = dbus.Interface(self.obj, "uk.org.thekelleys")

    def __iptodecimal(self, ip):
        hexn = ''.join(["%02X" % long(i) for i in ip.split('.')])
        return long(hexn, 16)

    def getVersion(self):
        return self.iface.GetVersion(ignore_reply=False)

    def registerNameServer(self, iface, server):
        decimalIP = dbus.UInt32(self.__iptodecimal(server))
        self.iface.RegisterServer(iface, decimalIP, ignore_reply=True)

    def unregisterNameServers(self, iface):
        self.iface.UnregisterServers(iface, ignore_reply=True)

    def clearCache(self):
        self.iface.ClearCache(ignore_reply=True)
