#!/usr/bin/python
# -*- coding: utf-8 -*-

desc = open("/usr/share/iscan-data/epkowa.desc", "r").read().strip().split("\n")

vid = "0x04b8"

pids = {}

for line in desc:
    if line.startswith(":usbid"):
        vid, pid = line.split()[1:]
    elif "esci-interpreter" in line or "iscan-plugin" in line:
        nline = line.replace("<br>", " ").replace('"', '').split()
        plugin = nline[nline.index("requires")+3]
        if pids.has_key(pid):
            pids[pid].add(plugin)
        else:
            pids[pid] = set((plugin,))


for k,v in pids.items():
    print "%s:%s needs %s" % (vid, k, ",".join(v))
