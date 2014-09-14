#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import shutil
import cPickle
import subprocess
from hashlib import sha1

from pardus import csapi

# real script

tz_file = "/etc/localtime"
tz_info = "/etc/timezone"
tz_zones = "/usr/share/zoneinfo/"
tz_dict = "/usr/share/zoneinfo/zoneinfo.dict"

def getTimeZone():
    if os.path.exists(tz_dict) and os.path.exists(tz_file):
        tzdb = cPickle.Unpickler(open(tz_dict, "rb")).load()
        tz = tzdb.get(sha1(open(tz_file, "r").read()).hexdigest(), "/etc/localtime doesn't exist.")
        return tz

def setTimeZone(zone=None):
    if zone:
        # Check if zone is a valid one, if not skip this call
        if not os.path.exists(os.path.join(tz_zones, zone)):
            return 1

        ret = subprocess.call(["/usr/sbin/zic", "-l", zone])
        return ret

    """
    if zone:
        try:
            if os.path.exists(tz_file):
                os.unlink(tz_file)
        except:
            pass

        # Copy the new TZ file to /etc/localtime
        shutil.copy(os.path.join(tz_zones, zone), tz_file)
    """

def setDate(year=None, month=None, day=None, hour=None, minute=None, second=None):
    new = list(time.localtime())
    if year: new[0] = int(year)
    if month: new[1] = int(month)
    if day: new[2] = int(day)
    if hour: new[3] = int(hour)
    if minute: new[4] = int(minute)
    if second: new[5] = int(second)
    csapi.settimeofday(time.mktime(new))

def getDate():
    return time.strftime("%Y %m %d %H %M %S %Z")

def saveToHW():
    subprocess.call(["/sbin/hwclock", "--systohc"])

def loadFromHW():
    subprocess.call(["/sbin/hwclock", "--hctosys"])

