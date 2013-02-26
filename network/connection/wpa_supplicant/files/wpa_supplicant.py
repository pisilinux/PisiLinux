#!/usr/bin/python
# -*- coding: utf-8 -*-

import dbus

WPAS_DBUS_OPATH = "/fi/epitest/hostap/WPASupplicant"
WPAS_DBUS_INTERFACES_OPATH = "/fi/epitest/hostap/WPASupplicant/Interfaces"

WPAS_DBUS_SERVICE = "fi.epitest.hostap.WPASupplicant"
WPAS_DBUS_INTERFACE = "fi.epitest.hostap.WPASupplicant"
WPAS_DBUS_INTERFACES_INTERFACE = "fi.epitest.hostap.WPASupplicant.Interface"
WPAS_DBUS_NETWORK_INTERFACE = "fi.epitest.hostap.WPASupplicant.Network"
WPAS_DBUS_BSSID_INTERFACE = "fi.epitest.hostap.WPASupplicant.BSSID"

TIMEOUT = 60

class PasswordLengthError(Exception):
    pass

class WPA_Supplicant_Network:
    def __init__(self, bus, path):
        self.bus = bus
        self.path = path
        self.net_obj = self.bus.get_object(WPAS_DBUS_SERVICE, path)
        self.net = dbus.Interface(self.net_obj, WPAS_DBUS_NETWORK_INTERFACE)

    # dict keys: ssid, bssid, key_mgmt, psk, scan_ssid, pairwise, group, eap, identity,
    # anonymous_identity, ca_cert, ca_cert2, client_cert, client_cert2, private_key, private_key2,
    # private_key_passwd, private_key2_passwd, phase1, phase2, eapol_flags
    #
    # Example: setNetwork({"ssid":dbus.String("MySSID", variant_level=1)),
    # "psk":dbus.String("MyPassword", variant_level=1))})
    def setNetwork(self, options):
        self.net.set(options)

    def enableNetwork(self):
        self.net.enable()

    def disableNetwork(self):
        self.net.disable()

class WPA_Supplicant_Interface:
    def __init__(self, bus, ifname, path):
        self.bus = bus
        self.ifname = ifname
        self.path = path
        self.if_obj = self.bus.get_object(WPAS_DBUS_SERVICE, path)
        self.iface = dbus.Interface(self. if_obj, WPAS_DBUS_INTERFACES_INTERFACE)

    def scan(self):
        self.iface.scan()

    def scanResults(self):
        return self.iface.scanResults()

    def addNetwork(self):
        path = self.iface.addNetwork()
        return self.getNetwork(path)

    def removeNetwork(self, network):
        self.iface.removeNetwork(network)

    def selectNetwork(self, network):
        self.iface.selectNetwork(network)

    def getNetworkPath(self, network_id):
        return "%s/Networks/%d" % (self.path, network_id)

    def getNetworkById(self, network_id):
        return WPA_Supplicant_Network(self.bus, self.getNetworkPath(network_id))

    def getNetwork(self, network):
        return WPA_Supplicant_Network(self.bus, network)

    # mode should be between 0 and 2
    def setAPScan(self, mode):
        self.iface.setAPScan(dbus.UInt32(mode))

    def disconnect(self):
        self.iface.disconnect()

    def getState(self):
        return self.iface.state()

    def getCapabilities(self):
        return self.iface.capabilities()

class WPA_Supplicant:
    def __init__(self):
        self.bus = dbus.SystemBus()
        self.wpas_obj = self.bus.get_object(WPAS_DBUS_SERVICE, WPAS_DBUS_OPATH)
        self.wpas = dbus.Interface(self.wpas_obj, WPAS_DBUS_INTERFACE)

    def getInterface(self, ifname):
        path = self.wpas.getInterface(ifname)
        return WPA_Supplicant_Interface(self.bus, ifname, path)

    # driver=wext, hostap, prism54, madwifi, atmel, ndiswrapper, ipw, wired
    def addInterface(self, ifname, driver):
        self.wpas.addInterface(ifname, {'driver': dbus.String(driver, variant_level=1)})
        return self.getInterface(ifname)

    def removeInterface(self, ifname):
        try:
            iface_path = self.wpas.getInterface(ifname)
        except dbus.DBusException:
            iface_path = None
        if iface_path:
            self.wpas.removeInterface(dbus.ObjectPath(iface_path))

def detectWpaDriver(ifname):
    import os
    import sys
    import pardus.netutils
    # if device is an ethernet device, driver is "wired"
    device = pardus.netutils.IF(ifname)
    if (device.isEthernet()) and (not device.isWireless()):
        return "wired"
    path = os.path.join("/sys/class/net/", ifname, "device/driver/module")
    modname = None
    if os.path.exists(path):
        modname = os.readlink(path).split("/")[-1]
        if "hostap" in modname:
            return "hostap"
        if "prism54" in modname:
            return "prism54"
        if "atmel" in modname:
            return "atmel"
    # we fallback to wext
    # wext is the generic driver for ipw2100, ipw2200, ndiswrapper > 1.12, madwifi etc...
    return "wext"

def getWpaInterface(ifname):
    wpa = WPA_Supplicant()
    try:
        iface = wpa.getInterface(ifname)
    except dbus.DBusException:
        driver = detectWpaDriver(ifname)
        iface = wpa.addInterface(ifname, driver)
    return iface

def waitForAuthenticationComplete(iface, timeout, wait = 0.1):
    import time
    while timeout > 0:
        if iface.getState() == "COMPLETED":
            return True
        else:
            timeout -= wait
        time.sleep(wait)
    return False

def checkServiceState(serviceName):
    bus = dbus.SystemBus()
    obj = bus.get_object("tr.org.pardus.comar", "/package/%s" % serviceName)
    state = obj.info(dbus_interface="tr.org.pardus.comar.System.Service")[2]
    return state in ("on", "started")

def isDBusServiceActive():
    return True

def isWpaServiceActive():
    return checkServiceState("wpa_supplicant")

def isWpaServiceUsable():
    return isDBusServiceActive() and isWpaServiceActive()

def startWpaService():
    if not isWpaServiceActive():
        bus = dbus.SystemBus()
        obj = bus.get_object("tr.org.pardus.comar", "/package/wpa_supplicant")
        obj.start(dbus_interface="tr.org.pardus.comar.System.Service")
    import time
    timeout = 10
    while timeout > 0:
        try:
            bus = dbus.SystemBus()
            net_obj = bus.get_object(WPAS_DBUS_SERVICE, WPAS_DBUS_OPATH)
            net = dbus.Interface(net_obj, WPAS_DBUS_NETWORK_INTERFACE)
        except dbus.DBusException:
            time.sleep(0.1)
            timeout -= 0.2
            continue
        return True
    return False

def setWpaAuthentication(ifname, ssid, password, timeout = TIMEOUT):
    password_length = len(password)
    if (password_length < 8) or (password_length > 63):
        raise PasswordLengthError("Password length should be between 8 and 63")
    iface = getWpaInterface(ifname)
    network = iface.addNetwork()
    network.setNetwork({"ssid": dbus.String(ssid, variant_level=1), "psk": dbus.String(password, variant_level=1)})
    iface.selectNetwork(network.path)
    authentication = waitForAuthenticationComplete(iface, timeout)
    if not authentication:
        disableAuthentication(ifname)
    return authentication

def disableAuthentication(ifname):
    wpa = WPA_Supplicant()
    wpa.removeInterface(ifname)
    bus = dbus.SystemBus()
    obj = bus.get_object("tr.org.pardus.comar", "/package/wpa_supplicant")
    obj.stop(dbus_interface="tr.org.pardus.comar.System.Service")

class Wpa_EAP:
    ssid = ""
    phase1 = ""
    phase2 = ""
    key_mgmt = "IEEE8021X"
    eap = "PEAP"
    anonymous_identity = ""
    ca_cert = ""
    client_cert = ""
    private_key = ""
    private_key_passwd = ""

    def __init__(self, ifname):
        self.ifname = ifname
        self.iface = getWpaInterface(ifname)
        self.network = self.iface.addNetwork()

    def authenticate(self, username, password, timeout = TIMEOUT):
        basic = {"ssid": dbus.String(self.ssid, variant_level=1),
                 "key_mgmt": dbus.String(self.key_mgmt, variant_level=1),
                 "eap": dbus.String(self.eap, variant_level=1),
                 "identity": dbus.String(username, variant_level=1)}

        if self.client_cert:
            basic["client_cert"] = dbus.String(self.client_cert, variant_level=1)
        if self.ca_cert:
            basic["ca_cert"] = dbus.String(self.ca_cert, variant_level=1)
        if self.private_key:
            basic["private_key"] = dbus.String(self.private_key, variant_level=1)
        if self.private_key_passwd:
            basic["private_key_passwd"] = dbus.String(self.private_key_passwd, variant_level=1)
        if self.phase2:
            basic["phase2"] = dbus.String("auth=%s"%self.phase2, variant_level=1)
        if password:
            basic["password"] = dbus.String(password, variant_level=1)
        if self.anonymous_identity:
            basic["anonymous_identity"] = dbus.String(self.anonymous_identity, variant_level=1)

        self.network.setNetwork(basic)

        self.iface.selectNetwork(self.network.path)
        authentication = waitForAuthenticationComplete(self.iface, timeout)
        if not authentication:
            disableAuthentication(self.ifname)
        return authentication
