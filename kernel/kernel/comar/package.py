#!/usr/bin/python

import os.path
import subprocess

def read_file(path):
    with open(path) as f:
        return f.read().strip()

def write_file(path, content):
    open(path, "w").write(content)
    open(path, "a").write("\n")

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    gcf = "/boot/grub2/grub.cfg"
    if not os.path.exists(gcf): return
    cfg = read_file(gcf)
    fix = False
    buf = []
    new = []
    okv = "0.0.0"
    nkv = open("/etc/kernel/kernel").read().strip()
    for line in cfg.split("\n"):
        if fix:
            buf.append(line)
            if line.startswith("\tinitrd"): okv = line.split("-")[1]
        else: new.append(line)
        if fix and line.startswith("submenu"):
            fix = False
            for l in buf:
                new.append(l.replace(okv, nkv))
            buf.pop()
            for l in buf:
                new.append("\t" + l.replace(okv, nkv))
        if line == "### BEGIN /etc/grub.d/10_linux ###": fix = True
    write_file(gcf, "\n".join(new))
    write_file("%s.bak" % gcf, cfg)

    # Update GRUB entry
    #if os.path.exists("/boot/grub/grub.conf"):
    #    call("grub", "Boot.Loader", "updateKernelEntry", (KVER, ""))

def preRemove():
    pass
