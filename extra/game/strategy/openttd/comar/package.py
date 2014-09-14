#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import fileinput
from stat import *

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    cfg_file_path = ['/home', 'user_name', '.openttd', 'openttd.cfg']
    ls = os.listdir(cfg_file_path[0])
    for it in ls:
        cfg_file_path[1] = it
        cfg_file = '/'.join(cfg_file_path)
        if os.path.isfile(cfg_file):
            st = os.stat(cfg_file)
            for line in fileinput.input(cfg_file, inplace=1):
                line = line.strip()
                if line.startswith('small_font') or line.startswith('medium_font') or line.startswith('large_font'):
                    print("%s= Dejavu Sans" % line.split('=')[0])
                elif line.startswith('mono_font'):
                    print("%s= Dejavu Sans Mono" % line.split('=')[0])
                elif line.startswith('small_size') or line.startswith('mono_size'):
                    print("%s= 12" % line.split('=')[0])
                elif line.startswith('medium_size'):
                    print("%s= 14" % line.split('=')[0])
                elif line.startswith('large_size'):
                    print("%s= 16" % line.split('=')[0])
                else: print line
            os.chown(cfg_file, st[ST_UID], st[ST_GID])
