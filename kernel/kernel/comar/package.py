#!/usr/bin/python

import os

def read_file(path):
    with open(path) as f:
        return f.read().strip()

def write_file(path, content):
    open(path, "w").write(content)
    open(path, "a").write("\n")

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    gcf = "/boot/grub2/grub.cfg"
    if not os.path.isfile(gcf): return

    ogp = []
    for line in read_file(gcf).split("\n"):
        if line.startswith("\tlinux"):
            ogp = line.split(" ro ")[1].split()
            break

    gdf = "/etc/default/grub"
    new = []
    gcl = []
    gcld = []
    if os.path.isfile(gdf):
        for line in read_file(gdf).split("\n"):
            if line.startswith("GRUB_CMDLINE_LINUX_DEFAULT"): gcld = line.split("DEFAULT=")[1][1:-1].split()
            elif "GRUB_CMDLINE_LINUX=" in line:
                gcl = line.split("LINUX=")[1][1:-1].split()
                # remove default options
                for p in gcld: 
                    if p in ogp: ogp.remove(p)
                # add options if assigned to GRUB_CMDLINE_LINUX
                if not line.startswith("#"):
                    for p in gcl: 
                        if not p in ogp: ogp.append(p)
                line = 'GRUB_CMDLINE_LINUX="%s"' % " ".join(ogp)
            new.append(line)
    
        write_file(gdf, "\n".join(new))

    if os.path.isfile("/etc/mudur/locale"): os.environ["LANG"] = read_file("/etc/mudur/locale").split("\n")[0]
    os.environ["PATH"] = "/usr/sbin:/usr/bin:/sbin:/bin"
    os.system("grub2-mkconfig -o %s" % gcf)

    # Update GRUB entry
    #if os.path.exists("/boot/grub/grub.conf"):
    #    call("grub", "Boot.Loader", "updateKernelEntry", (KVER, ""))

def preRemove():
    pass
