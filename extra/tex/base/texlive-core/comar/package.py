#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import glob
import shutil
import subprocess

def postInstall(fromVersion, fromRelease, toVersion, toRelease):

    updmap_file = "/etc/texmf/web2c/updmap.cfg"
    updmap_local_file = "/etc/texmf/web2c/updmap-local.cfg"
    updmap_share_file = "/usr/share/texmf-dist/web2c/updmap-hdr.cfg"
    temp_file = "/tmp/updmap.cfg.temp"
    texmf_file="/etc/texmf/web2c/texmf.cnf"
    texmf_symfile="/usr/share/texmf-dist/web2c/texmf.cnf"


    print "texlive: saving updmap.cfg as %s" % temp_file
    shutil.copy2(updmap_file, temp_file)

    print "texlive: regenerating updmap.cfg (custom additions should go"
    print "         into /etc/texmf/web2c/updmap-local.cfg"

    shutil.copy2(updmap_share_file, updmap_file)
    shutil.copy2(texmf_file, texmf_symfile)


    # In bash: cat *.maps >> updmap.cfg
    # In python:ugly lines below ...
    for map_file in glob.glob("/var/lib/texmf/pisilinux/*.maps"):
        print "texlive: adding %s to updmap.cfg" % map_file
        fin = open(map_file, "r")
        updmap_hdr = fin.read()
        fin.close()

        fout = open(updmap_file, "a")
        fout.write(updmap_hdr)
        fout.close()

    # Look for custom additions, if available add them too
    if os.path.exists(updmap_local_file):
        fin = open(updmaplocal_file, "r")
        updmap_local = fin.read()
        fin.close()

        fout = open(updmap_file, "a")
        fout.write(updmap_local)
        fout.close()

    print "texlive: updating the filename database..."
    subprocess.call(["/usr/bin/mktexlsr"])

    print "texlive: updating the fontmap files with updmap..."
    subprocess.call(["/usr/bin/updmap-sys", "--quiet" ,"--nohash"])

    print "texlive: creating all formats..."
    fnull = open(os.devnull, 'w')
    subprocess.call(["/usr/bin/fmtutil-sys", "--all"], stdout=fnull, stderr=fnull)

    print "done ..."
    print "texlive: logs are under /var/lib/texmf/web2c/<engine>/<formatname>.log)"
