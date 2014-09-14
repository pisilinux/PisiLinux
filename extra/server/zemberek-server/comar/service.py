# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "Zemberek Spell Checker",
                 "tr": "Zemberek Yazım Denetleyicisi"})
serviceDefault = "conditional"

MSG_ERR_JAVAHOMENOTSET = _({"en": "JAVA_HOME is not set.",
                            "tr": "JAVA_HOME atanmamış.",
                            })
@synchronized
def start():
    loadEnvironment()

    if not os.environ.has_key("JAVA_HOME"):
        fail(MSG_ERR_JAVAHOMENOTSET)
    javapath = os.environ["JAVA_HOME"]

    os.environ["LC_ALL"] = "tr_TR.UTF-8"

    startService(command="%s/bin/java" % javapath,
                 args="-classpath /usr/share/java/mina-core.jar:/usr/share/java/slf4j-api.jar:/usr/share/java/slf4j-nop.jar:/usr/share/java/zemberek-server.jar:/usr/share/java/zemberek-cekirdek.jar:/usr/share/java/zemberek-tr.jar:/usr/share/java/unix.jar:/usr/share/java/debug-disable.jar:/usr/share/java/dbus.jar -Djava.library.path=/usr/lib/jni/:/lib:/usr/lib -Xverify:none -Xms12m -Xmx14m -DConfigFile=/etc/zemberek-server.ini net.zemberekserver.server.ZemberekServer",
                 detach=True,
                 pidfile="/run/zemberek.pid",
                 makepid=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/run/zemberek.pid",
                donotify=True)

def ready():
    loadEnvironment()

    state = is_on()
    if state == "on" or \
        (state == "conditional" and os.environ["LC_ALL"] == "tr_TR.UTF-8"):
        start()

def status():
    return isServiceRunning("/run/zemberek.pid")
