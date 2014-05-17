from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "RAID monitor daemon",
                 "tr": "RAID izleme servisi"})
serviceConf = "mdadm"

MSG_ERR_STRTSRVC = {"en": "Couldn't start service.Please edit mdadm.conf file.",
                    "tr": "Servis başlatılamadı.Lütfen mdadm.conf dosyasını düzenleyiniz.",
                   }

def check():
    try:
        f = file("/etc/mdadm.conf")
        confLines = [a.lstrip() for a in f]
        confLines = filter(lambda x: not (x.startswith("\#") or x == ""), confLines)
        check = False
        for line in confLines:
            if "MAILADDR" or "PROGRAM" in line.split():
                check = True
        if not check:
            fail(MSG_ERR_STRTSRVC)
    except:
        fail(MSG_ERR_STRTSRVC)
    finally:
        f.close()

@synchronized
def start():
    check()
    startService(command="/sbin/mdadm",
                 args="--monitor --scan --daemonise --pid-file /run/mdadm.pid %s" % config.get("MDADM_OPTS"),
                 pidfile="/run/mdadm.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/run/mdadm.pid",
                donotify=True)

def status():
    return isServiceRunning("/run/mdadm.pid")
