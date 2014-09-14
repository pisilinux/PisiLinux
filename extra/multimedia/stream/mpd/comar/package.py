#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for d in ["/var/lib/mpd", "/var/lib/mpd/.mpd", "/var/lib/mpd/.mpd/playlists", "/var/lib/mpd/.mpd/music"]:
        if not os.path.exists(d):
            os.mkdir(d)
            # $ id nobody
            # uid=250(mpd) gid=18(audio)
            os.chown(d, 250, 18)
            os.chmod(d, 0750)

    os.system("/sbin/mudur_tmpfiles.py /usr/lib/tmpfiles.d/mpd.conf")
