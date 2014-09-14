# -*- coding: utf-8 -*-
from comar.service import *

import re

serviceType = "local"
serviceDesc = _({"en": "Set the date & time via NTP",
                 "tr": "Tarih & zamanı NTP ile ayarlayın"})
serviceConf = "ntpdate"
serviceDefault = "conditional"

# ntpdate will run if it finds a ticker in any of the configuration files

NTPCONF = "/etc/ntp.conf"
NTPSTEP = "/etc/ntp/step-tickers"
PIDFILE = "/run/ntpdate.pid"

MSG_NOSERVER = _({"en"  : "NTP server not specified in %s or %s." % (NTPSTEP, NTPCONF),
                  "tr"  : "%s veya %s dosyasında hiç NTP sunucu belirtilmemiş." % (NTPSTEP, NTPCONF)})

def parse_tickers():
    tickers = []
    if os.path.exists(NTPSTEP):
        for line in open(NTPSTEP, "r").read().strip().split("\n"):
            if line and not line.startswith("#"):
                tickers.append(line)

    if tickers:
        return tickers

    if os.path.exists(NTPCONF):
        for line in open(NTPCONF, "r").read().strip().split("\n"):
            if line.startswith(("server", "peer")):
                try:
                    peer = line.split()[1]
                    if not re.match("127\.127\.[0-9]+\.[0-9]+", peer):
                        tickers.append(peer)
                except IndexError:
                    pass

    return tickers

@synchronized
def start():
    tickers = parse_tickers()

    if len(tickers) == 0:
        fail(MSG_NOSERVER)

    tickers = " ".join(tickers)

    # Eventhough the ntpdate is a oneshot process, the pidfile hack is used to
    # work around COMAR's silly status() check in startService()
    startService(command="/usr/sbin/ntpdate",
                 args="%s %s" % (config.get("OPTIONS", "-U ntp -s -b"), tickers),
                 makepid=True,
                 pidfile=PIDFILE,
                 donotify=True)

    if os.path.exists(PIDFILE):
        os.unlink(PIDFILE)

    if config.get("SYNC_HWCLOCK", "no") == "yes":
        run("/sbin/hwclock --systohc")

def ready():
    status = is_on()
    tickers = parse_tickers()
    if status == "on" or (status == "conditional" and tickers):
        start()


@synchronized
def stop():
    # There's nothing to do
    pass

def status():
    # No need to supply a status as the service is oneshot
    return
