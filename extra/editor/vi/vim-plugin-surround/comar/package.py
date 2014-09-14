#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # Generate helptags
    os.system("vim --noplugins -u NONE -U NONE --cmd ':helptags /usr/share/vim/vimfiles/doc' --cmd ':q'")
