# -*- coding: utf-8 -*-

from pisi.version import Version

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if fromVersion and Version("0.90") <= Version(fromVersion) <= Version("0.96"):
        from zorg import config

        busId = call("zorg", "Xorg.Display", "activeDeviceID")
        device = config.getDeviceInfo(busId)

        if device:
            config.saveDeviceInfo(device)
            config.saveXorgConfig(device)

    if fromRelease and int(fromRelease) < 81:
        from zorg import config

        layout, variant = config.getKeymapOld()
        config.saveKeymap(layout, variant)
