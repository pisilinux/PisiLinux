# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDefault = "off"

serviceDesc = _({"en": "Network UPS Tools",
                 "tr": "Ağ Kesintisiz Güç Kaynağı Araçları"})

MSG_ERR_STRTMODL = _({"en": "Could not start model %s.",
                      "tr": "Model %s başlatılamadı.",
                      })
MSG_ERR_STRTUPSD = _({"en": "Could not start UPSD server.",
                      "tr": "UPSD sunucu başlatılamadı.",
                      })
MSG_ERR_STOPUPSM = _({"en": "Could not stop upsmon.",
                      "tr": "Upsmon durdurulamadı.",
                      })

piddir = "/run/nut"
model = config.get("MODEL", "upsdrvctl")
server = config.get("SERVER", "no")


@synchronized
def start():
    startDependencies("hal")

    error = 0
    if server == "yes":
        if model == "upsdrvctl":
            error = run("/usr/sbin/upsdrvctl start")
        else:
            error = run("/lib/nut/%s %s %s" % (model, \
                                              config.get("MODEL_OPTIONS", ""), \
                                              config.get("DEVICE", "")))

        if error:
            fail(MSG_ERR_STRTMODL % model)
        else:
            error = startService(command="/usr/sbin/upsd",
                                  args=config.get("UPSD_OPTIONS", ""),
                                  pidfile="%s/upsd.pid" % piddir,
                                  donotify=False)

    if error:
        fail(MSG_ERR_STRTUPSD)
    else:
        startService(command="/usr/sbin/upsmon",
                     pidfile="%s/upsmon.pid" % piddir,
                     donotify=True)

@synchronized
def stop():
    error = stopService(command="/usr/sbin/upsmon",
                        donotify=False)

    if server == "yes":
        if error:
            fail(MSG_ERR_STOPUPSM)
        else:
            error = stopService(command="/usr/sbin/upsd",
                                  pidfile="%s/upsd.pid" % piddir,
                                  donotify=False)

        if not error and server == "yes":
            if model == "upsdrvctl":
                error = run("/usr/sbin/upsdrvctl stop")
            else:
                error = stopService(command="/lib/nut/%s" % model)

    if not error:
        notify("System.Service.changed", "stopped")
    else:
        fail()


def status():
    return isServiceRunning(command="/usr/sbin/upsmon")

