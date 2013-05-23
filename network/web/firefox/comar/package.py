#!/usr/bin/python

import os
import re

def symlink(src, dest):
    try:
        os.symlink(src, dest)
    except OSError:
        pass

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.environ["HOME"] = "/root"
    os.system("/bin/touch /usr/lib/MozillaFirefox/components/compreg.dat")
    os.system("/bin/touch /usr/lib/MozillaFirefox/components/xpti.dat")
    os.system("/usr/lib/MozillaFirefox/firefox -register")
    os.system("/bin/touch /usr/lib/MozillaFirefox/.autoreg")

    lang = None

    if os.path.exists("/etc/mudur/language"):
        lang = open("/etc/mudur/language").read().strip()
    elif os.path.exists("/etc/env.d/03locale"):
        fileContent = open("/etc/env.d/03locale").read()
        lang = re.search("^LANG=(.*)$", fileContent, flags=re.M)
        if lang:
            lang = lang.group(1).split(".")[0]

    if lang:
        # Bookmarks & Search plugins
        if lang.startswith("tr"):
            symlink("/usr/lib/MozillaFirefox/pisilinux/bookmarks-tr.html", "/usr/lib/MozillaFirefox/browser/defaults/profile/bookmarks.html")
            symlink("/usr/lib/MozillaFirefox/pisilinux/pisilinux-wiki_tr.xml", "/usr/lib/MozillaFirefox/browser/searchplugins/pisilinux-wiki.xml")
        elif lang.startswith("nl"):
            symlink("/usr/lib/MozillaFirefox/pisilinux/bookmarks-nl.html", "/usr/lib/MozillaFirefox/browser/defaults/profile/bookmarks.html")
            symlink("/usr/lib/MozillaFirefox/pisilinux/pisilinux-wiki_nl.xml", "/usr/lib/MozillaFirefox/browser/searchplugins/pisilinux-wiki.xml")
        elif lang.startswith("pt"):
            symlink("/usr/lib/MozillaFirefox/pisilinux/pisilinux-wiki_pt.xml", "/usr/lib/MozillaFirefox/browser/searchplugins/pisilinux-wiki.xml")
            #TODO: translate bookmarks to pt also.
            symlink("/usr/lib/MozillaFirefox/pisilinux/bookmarks-en.html", "/usr/lib/MozillaFirefox/browser/defaults/profile/bookmarks.html")
        elif lang.startswith("de"):
            symlink("/usr/lib/MozillaFirefox/pisilinux/bookmarks-de.html", "/usr/lib/MozillaFirefox/browser/defaults/profile/bookmarks.html")
            symlink("/usr/lib/MozillaFirefox/pisilinux/pisilinux-wiki_en.xml", "/usr/lib/MozillaFirefox/browser/searchplugins/pisilinux-wiki.xml")
        elif lang.startswith("es"):
            symlink("/usr/lib/MozillaFirefox/pisilinux/pisilinux-wiki_es.xml", "/usr/lib/MozillaFirefox/browser/searchplugins/pisilinux-wiki.xml")
        else:
            symlink("/usr/lib/MozillaFirefox/pisilinux/bookmarks-en.html", "/usr/lib/MozillaFirefox/browser/defaults/profile/bookmarks.html")
            symlink("/usr/lib/MozillaFirefox/pisilinux/pisilinux-wiki_en.xml", "/usr/lib/MozillaFirefox/browser/searchplugins/pisilinux-wiki.xml")

def preRemove():
    for f in  ("/usr/lib/MozillaFirefox/.autoreg", "/usr/lib/MozillaFirefox/browser/defaults/profile/bookmarks.html", "/usr/lib/MozillaFirefox/browser/searchplugins/pisilinux-wiki.xml"):
        try:
            os.unlink(f)
        except:
            pass
