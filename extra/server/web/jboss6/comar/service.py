#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from comar.service import *

serviceDefault = "off"
serviceType = "server"
serviceDesc = _({"en": "JBoss Application Server",
                 "tr": "JBoss Uygulama Sunucusu"
                 })

BASEDIR = "/opt/jboss6"
PIDFILE = "/var/run/jboss6.pid"

os.environ["LC_ALL"] = "C"
os.environ["LANG"] = "C"
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-7-openjdk"
os.environ["JBOSS_HOME"] = BASEDIR

@synchronized
def start():
    startService(command="%s/bin/run.sh" % BASEDIR,
                 detach=True,
                 donotify=True)

@synchronized
def stop():
    stopService(command = "%s/bin/shutdown.sh" % BASEDIR,
                args="-o localhost --shutdown",
                donotify = True)

def status():
    return isServiceRunning(PIDFILE)
