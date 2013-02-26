#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for d in ["/var/lib/mpd", "/var/lib/mpd/playlists", "/var/log/mpd", "/var/run/mpd", "/var/db/mpd", "/var/state/mpd"]:
        if not os.path.exists(d):
            os.mkdir(d)
            # $ id nobody
            # uid=250(mpd) gid=18(audio)
            os.chown(d, 250, 18)
            os.chmod(d, 0750)

