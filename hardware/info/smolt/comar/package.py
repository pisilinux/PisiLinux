#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from random import randint

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    UUID = file("/proc/sys/kernel/random/uuid").read().strip()
    file("/etc/hw-uuid", "w").write(UUID)

    minute = randint(0,59)
    hour = randint(0,23)
    day = randint(0,28)

    template = """# Monhly checkin cron script for Smolt.
# Cron script runs if and only if smolt service is started.
# Existance of the script does not prove that auto checkin is enabled.
%s %s %s * * smolt /usr/bin/smoltSendProfile -c > /dev/null 2>&1"""

    file("/etc/cron.d/smolt", "w").write(template % (minute, hour, day))
