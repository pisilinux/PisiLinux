#!/usr/bin/python
# -*- coding: utf-8 -*-

import bz2
import sys
import pisi
import urllib2
import os
import piksemel

REPO_URL = "http://farm.pisilinux.org/.nofarm-repo/x86_64/"

def log(msg):
    print "%s: %s" % (sys.argv[0], msg)

if __name__ == "__main__":
    log("Requested debug packages for these binaries:")
    for arg in sys.argv[1:]:
        log("  %s" % arg)

    log("Fetching repository info...")
    url = urllib2.urlopen("%s/pisi-index.xml.bz2" % REPO_URL)
    xml_content = bz2.decompress(url.read())
    doc = piksemel.parseString(xml_content)

    files_db = pisi.db.filesdb.FilesDB()

    def get_filenames(packages):
        for package_tag in doc.tags("Package"):
            name = package_tag.getTagData("Name")
            if name in packages:
                yield package_tag.getTagData("PackageURI")

    def get_package_name(path):
        try:
            package, path = files_db.get_file(path.lstrip("/"))
        except KeyError:
            sys.exit(2)

        return package

    idb = pisi.db.installdb.InstallDB()
    source_packages = []
    releases = {}

    for path in sys.argv[1:]:
        name = get_package_name(path)
        package = idb.get_package(name)
        dbg_name = "%s-dbginfo" % package.source.name
        source_packages.append(dbg_name)
        releases[dbg_name] = package.release

    package_urls = []

    log("Following debug packages will be installed:")
    for filename in get_filenames(source_packages):
        name, ver = pisi.util.parse_package_name(pisi.util.remove_suffix(".pisi", filename))
        release = ver.split("-")[1]

        if idb.has_package(name):
            continue

        if release != releases[name]:
            sys.exit(2)

        log("  %s" % name)
        package_urls.append("/".join((REPO_URL, filename)))

    sys.exit(os.system("pm-install %s" % " ".join(package_urls)))
