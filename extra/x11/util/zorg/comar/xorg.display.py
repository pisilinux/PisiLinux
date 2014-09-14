# -*- coding: utf-8 -*-

import os

import comar
from pardus.sysutils import *

from zorg.config import *
from zorg.consts import *
from zorg.probe import *
from zorg.utils import *

kernel_module_file = os.path.join(config_dir, "kernel_module")

def getDevice():
    bus = configuredBus()
    if not bus:
        return None

    return getDeviceInfo(bus)

def getDeviceOutput(output):
    dev = getDevice()
    if not dev:
        return None, None

    if output not in dev.outputs:
        dev.outputs[output] = Output(output)

    return dev, dev.outputs[output]

# Model methods

def ready(boot):
    opts = {}

    if boot:
        opts = get_kernel_option("xorg")

    if "keymap" in opts:
        keymap = opts["keymap"].split("/", 1)
        setKeymap(*keymap)

    if "safe" in opts:
        return False

    driver = opts.get("driver")

    if driver or "probe" in opts:
        return initialConfig(driver)

    busId = configuredBus()
    if not busId:
        return initialConfig()

    if boot:
        # Check if the active card is changed
        try:
            device = getDeviceInfo(busId)
        except IOError:
            # Device is not present on specified bus.
            # Check if the new device is configured before.
            newBus = getPrimaryCard()
            if newBus:
                device = getDeviceInfo(VideoDevice(newBus).bus_id)
                if device and not device.isChanged():
                    # Yes, it is configured before.
                    # Reenable driver and write xorg.conf.
                    device.enableDriver()
                    saveXorgConfig(device)
                else:
                    # This is a different card.
                    return initialConfig()
            else:
                # No card is present. Return True in order to
                # start with a manually edited xorg.conf.
                return True
        else:
            if not device or device.isChanged():
                return initialConfig()

    # Check kernel module. Later, this should be done
    # with Xorg.Driver.ready method.
    if os.path.exists(kernel_module_file):
        kernelModule = file(kernel_module_file).read()
        if run("/sbin/modprobe", "-i", kernelModule) and kernelModule != "fglrx":
            return False

    return True

def initialConfig(preferredDriver=None):
    bus = getPrimaryCard()

    if bus:
        device = VideoDevice(bus)
    else:
        # This machine might be a terminal server with no video cards.
        # We start X and leave the decision to the user.
        log_debug("No video card found.")
        return True

    if preferredDriver is None:
        preferredDriver = device.preferredDriver()

    device.setDriver(preferredDriver)

    saveDeviceInfo(device)
    saveXorgConfig(device)

    return True

def safeConfig():
    bus = getPrimaryCard()

    if bus:
        device = VideoDevice(bus)
    else:
        # See the comment in initialConfig
        return True

    device.setDriver("vesa")
    device.depth = 16
    device.outputs["default"] = Output("default")
    device.monitors["default"] = Monitor()

    saveDeviceInfo(device)
    saveXorgConfig(device)

    return True

# FIXME Confusing method name
def activeDeviceID():
    return configuredBus()

def listDrivers():
    drivers = listAvailableDrivers()

    link = comar.Link()
    packages = list(link.Xorg.Driver)
    for package in packages:
        try:
            info = link.Xorg.Driver[package].getInfo()
        except dbus.DBusException:
            continue
        alias = str(info["alias"])
        driver = str(info["xorg-module"])
        drivers.append(alias)
        if driver in drivers:
            drivers.remove(driver)

    return sorted(drivers)

def setDriver(driver):
    dev = getDevice()
    if dev:
        dev.setDriver(driver)
        saveDeviceInfo(dev)

def setDepth(depth):
    dev = getDevice()
    if dev:
        dev.depth = depth
        saveDeviceInfo(dev)

def setOutput(output, enabled, ignored):
    dev, out = getDeviceOutput(output)

    if dev:
        out.setEnabled(enabled)
        out.setIgnored(ignored)

        saveDeviceInfo(dev)

def setMode(output, resolution, rate):
    dev, out = getDeviceOutput(output)

    if dev:
        out.setMode(resolution, rate)

        saveDeviceInfo(dev)

def setOrientation(output, rotation, reflection):
    dev, out = getDeviceOutput(output)

    if dev:
        out.setOrientation(rotation, reflection)

        saveDeviceInfo(dev)

def setPosition(output, position, arg):
    dev, out = getDeviceOutput(output)

    if dev:
        out.setPosition(position, arg)

        saveDeviceInfo(dev)

def setMonitor(output, vendor, model, horizSync, vertRefresh):
    dev, out = getDeviceOutput(output)

    if dev:
        if model:
            mon = Monitor()
            mon.vendor  = vendor
            mon.model   = model
            mon.hsync   = horizSync
            mon.vref    = vertRefresh
            dev.monitors[output] = mon
        elif output in dev.monitors:
            del dev.monitors[output]
        else:
            return

        saveDeviceInfo(dev)

def syncConfigs():
    dev = getDevice()
    if dev:
        saveXorgConfig(dev)

def setKeymap(layout, variant=""):
    saveKeymap(layout, variant)
