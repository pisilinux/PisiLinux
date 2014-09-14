#!/usr/bin/python
# -*- coding: utf-8 -*-

from pardus.fileutils import FileLock
from pardus.localedata import languages as LANGUAGES

# Mudur configuration file

CONF = "/etc/conf.d/mudur"
TTY_DEFAULT = 6

# Required utils

def getConf(key, default=None):
    lock = FileLock(CONF)
    lock.lock(shared=True)
    value = default
    for line in file(CONF):
        line = line.strip()
        try:
            _key, _value = line.split("=", 1)
        except ValueError:
            continue
        _key = _key.strip()
        if key == _key:
            value = _value.strip()
            if value.startswith('"') or value.startswith("'"):
                value = value[1:-1]
            break
    lock.unlock()
    return value

def setConf(key, value=None):
    lock = FileLock(CONF)
    lock.lock(shared=False)
    data = file(CONF).read()
    lines = data.split("\n")
    for index, line in enumerate(lines):
        try:
            _key, _value = line.split("=", 1)
        except ValueError:
            continue
        _key = _key.strip()
        if key == _key or (_key.startswith("#") and _key[1:].strip() == key):
            if value:
                lines[index] = "%s = '%s'" % (key, value)
            elif not line.startswith("#"):
                lines[index] = "# %s" % line
    file(CONF, "w").write("\n".join(lines))
    lock.unlock()

# System.Settings methods

def listLanguages():
    languages = []
    for code, info in LANGUAGES.iteritems():
        languages.append((code, str(info.name)))
    return languages

def getLanguage():
    return getConf("language", "en")

def setLanguage(lang):
    if not len(lang):
        lang = None
    setConf("language", lang)


def listKeymaps(language):
    keymaps = []
    if language and language in LANGUAGES:
        for keymap in LANGUAGES[language].keymaps:
            keymaps.append((keymap.console_layout, str(keymap.name)))
    else:
        for language in LANGUAGES:
            for keymap in LANGUAGES[language].keymaps:
                keymaps.append((keymap.console_layout, str(keymap.name)))
    return keymaps

def getKeymap():
    return getConf("keymap", "us")

def setKeymap(keymap):
    if not len(keymap):
        keymap = None
    setConf("keymap", keymap)


def getHeadStart():
    return getConf("head_start")

def setHeadStart(package):
    if not len(package):
        package = None
    setConf("head_start", package)


def getClock():
    is_utc = getConf("clock", "local") == "UTC"
    adjust = getConf("clock_adjust", "no") == "yes"
    return is_utc, adjust

def setClock(is_utc, adjust):
    if is_utc:
        setConf("clock", "UTC")
    else:
        setConf("clock", "local")
    if adjust:
        setConf("clock_adjust", "yes")
    else:
        setConf("clock_adjust", "no")


def getTTYs():
    count = getConf("tty_number", TTY_DEFAULT)
    try:
        return int(count)
    except (ValueError, TypeError):
        return TypeError

def setTTYs(count):
    setConf("tty_number", count)
