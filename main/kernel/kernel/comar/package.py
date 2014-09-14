#!/usr/bin/python

import os

def read_file(path):
    with open(path) as f:
        return f.read().strip()

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    gcf = "/boot/grub2/grub.cfg"
    if not os.path.isfile(gcf): return

    if os.path.isfile("/etc/mudur/locale"): os.environ["LANG"] = read_file("/etc/mudur/locale").split("\n")[0]
    os.environ["PATH"] = "/usr/sbin:/usr/bin:/sbin:/bin"
    os.system("grub2-mkconfig -o %s" % gcf)

    # Update GRUB entry
    #if os.path.exists("/boot/grub/grub.conf"):
    #    call("grub", "Boot.Loader", "updateKernelEntry", (KVER, ""))

def preRemove():
    pass
