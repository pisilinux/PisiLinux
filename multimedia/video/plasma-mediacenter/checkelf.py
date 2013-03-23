#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009-2010 TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.

# For more information execute run with '--help'
#
# A detailed documentation about checkelf can be found on:
# http://developer.pardus.org.tr/guides/packaging/checkelf.html

import os
import re
import sys
import glob
import pisi
import magic
import shutil
import fnmatch
import tempfile
import optparse
import itertools
import subprocess

INSTALLDB = pisi.db.installdb.InstallDB()
CONSTANTS = pisi.constants.Constants()

def process_ldd(objdump_needed, ldd_output, ldd_unused, ldd_undefined):
    '''Process the ldd outputs. And return a simple path only lists'''
    result_unused = []
    result_undefined = []
    result_broken = []
    result_main_ldd = {}
    result_needed = []

    for line in ldd_unused.replace("\t", "").split("\n"):
        if not line == "" and not "Unused" in line:
            result_unused.append(line.strip())

    for line in ldd_undefined.replace("\t", "").split("\n"):
        if line.startswith("undefined symbol:"):
            result_undefined.append(re.sub("^undefined symbol: (.*)\((.*)\)$", "\\1", line))

    for line in ldd_output:
        if "=>" in line:
            # Filter these special objects
            if "linux-gate" in line or \
                    "ld-linux" in line or "linux-vdso" in line:
                continue

            so_name, so_path = line.split("=>")
            if "not found" in so_path:
                # One of the dynamic dependencies is missing
                result_broken.append(so_name.strip())
            else:
                result_main_ldd[so_name.strip()] = so_path.split(" (")[0].strip()

    for obj in objdump_needed:
        # Find the absolute path of libraries from their SONAME's
        if result_main_ldd.has_key(obj):
            result_needed.append(os.popen("readlink -f %s" % result_main_ldd[obj]).read().strip())
        else:
            result_needed.append(obj)

    # result_needed = (all shared libary dependencies) - (needed shared library gathered from objdump)
    # result_broken = broken libraries that are not available at their place
    # result_unused = unused direct dependencies
    # result_undefined = undefined symbol errors
    return (result_needed, result_broken, result_unused, result_undefined)

def check_objdump(processed_needed, package_elf_files, package_name):
    '''check the objdump needed libraries with the ldd libraries
       the libraries that are needed can be used for dependencies'''
    result_needed = []
    # check  if the libraries are shipped with the package
    # then associate each library(with his package_name)  with the given elf_file
    for objdump_needed in processed_needed:
        if objdump_needed in package_elf_files:
            # file is shipped within this package
            dependency_name = package_name
        else:
            # search for the package name (i.e: pisi sf /usr/lib/*.so )
            # the library may not exist, thus adding an exception is welcome
            try:
                dependency_name = pisi.api.search_file(objdump_needed)[0][0]
            except IndexError:
                dependency_name = "broken"
                #print "%s (probably broken dependency)" % needed
        result_needed.append((objdump_needed, dependency_name))
    return result_needed

def check_pc_files(pc_file):
    '''check for .pc files created by pkgconfig and shipped with the package
       these .pc files have requirements tags that can be used for dependencies'''
    result_needed = []
    requires = set(os.popen("pkg-config --print-requires --print-requires-private %s | gawk '{ print $1 }'" % \
            os.path.basename(pc_file).replace(".pc", "")).read().split("\n")[:-1])

    for require in requires:
        require_file = "/usr/share/pkgconfig/%s.pc" % require

        if not os.path.exists(require_file):
            require_file = "/usr/lib/pkgconfig/%s.pc" % require
        try:
            dependency_name = pisi.api.search_file(require_file)[0][0]
        except IndexError:
            dependency_name = "broken"

        result_needed.append((require_file, dependency_name))

    return result_needed

def check_intersections(result_dependencies, package_deps, package_name, systembase, systemdevel):
    '''eliminate system base and system devel packages and self written deps'''

    # get system.base and system.devel packages
    systembase_packages = []
    systemdevel_packages= []
    cdb = pisi.db.componentdb.ComponentDB()
    for repo in pisi.db.repodb.RepoDB().list_repos():
        for component in cdb.list_components(repo):
            if component == "system.base":
                systembase_packages.extend(cdb.get_packages('system.base', repo))
            if component == "system.devel":
                systemdevel_packages.extend(cdb.get_packages('system.devel', repo))

    # look for packages that are system.base but are written as dependency
    # mark them with "*"
    result_must_removed = list(set(package_deps) & set(systembase_packages))
    for deps in package_deps:
        if deps in result_must_removed:
            package_deps[package_deps.index(deps)] = "%s (base)" % deps

    # look for packages that are system.devel but are written as dependency
    # mark them with "*"
    result_must_removed = list(set(package_deps) & set(systemdevel_packages))
    for deps in package_deps:
        if deps in result_must_removed:
            package_deps[package_deps.index(deps)] = "%s (devel)" % deps

    # extract the dependency package names and store them in result_deps
    # dependencies tagged as broken or given itself are eliminated
    dependencies = set()
    result_deps = []
    for elf_files, paths_and_deps in result_dependencies.items():
        for data in paths_and_deps:
            if not data[1] == "broken" and not data[1] == package_name:
                result_deps.append(data[1])

    # remove packages that belong to system.base component
    # when -s is used, systembase is set to true
    # using set removes also duplicates in result_deps
    # mark packages that are common to system.base and result_deps with *
    if not systembase:
        result_deps = list(set(result_deps) - set(systembase_packages))
    if not systemdevel and package_name.endswith('-devel'):
        result_deps = list(set(result_deps) - set(systemdevel_packages))
    if systemdevel or systembase:
        result_must_removed = list(set(result_deps) & set(systembase_packages))
        for deps in result_deps:
            if deps in result_must_removed:
                result_deps[result_deps.index(deps)] = "%s (base)" % deps
        result_must_removed = list(set(result_deps) & set(systemdevel_packages))
        for deps in result_deps:
            if deps in result_must_removed:
                result_deps[result_deps.index(deps)] = "%s (devel)" % deps
        result_deps = list(set(result_deps))

    # remove packages that already are written in metadata.xml (runtime dependencies written in pspec.xml)
    result_section = list(set(result_deps) -  set(package_deps))

    # create a sorted iteration object of the final results variables
    # the lists may have variable lengths, thus we fill the smallers one with empty strings.
    # at the end all the lists are in the same length. This makes it easy to print it like a table
    cmp_func = lambda x, y: len(x) - len(y)
    result_lists = itertools.izip_longest(sorted(list(set(package_deps)), cmp=cmp_func),
                                          sorted(result_deps, cmp=cmp_func),
                                          sorted(result_section, cmp=cmp_func),
                                          fillvalue="")
    return result_lists

def output_result(package_name, package_dir):
    '''execute ldd on elf files and returns them'''
    #Initialize magic for using "file" in python
    magic_db = magic.open(magic.MAGIC_NONE)
    magic_db.load()

    package_elf_files = []

    # Two options are available. Checking for a pisi file or an installed package in the database
    if package_dir:
        package_files = os.popen("find %s" % package_dir).read().strip().split("\n")
        package_pc_files = glob.glob("%s/usr/*/pkgconfig/*.pc" % package_dir)
    else:
        package_files = set(["/%s" % file_name.path \
            for file_name in INSTALLDB.get_files(package_name).list])
        package_pc_files = set([os.path.realpath("/%s" % file_name.path) \
                for file_name in INSTALLDB.get_files(package_name).list \
                if fnmatch.fnmatch(file_name.path, "*/pkgconfig/*.pc")])

    for package_file in package_files:
        package_file_info = magic_db.file(package_file) #Return file type
        if "LSB shared object" in package_file_info:
            package_elf_files.append(os.path.realpath(package_file))
        elif "LSB executable" in package_file_info:
            package_elf_files.append(package_file)

    #There maybe more than one elf file, check for each one
    result_dependencies = {}
    result_unused = {}
    result_undefined = {}
    result_broken = None
    result_runpath = {}
    ld_library_paths = set()

    # Add library paths for unpacked pisi files
    if package_dir:
        for elf_file in package_elf_files:
            if elf_file.endswith(".so") or ".so." in elf_file:
                ld_library_paths.add(os.path.dirname(elf_file))
        os.environ.update({'LD_LIBRARY_PATH': ":".join(ld_library_paths)})

    for elf_file in package_elf_files:
        ldd_output = subprocess.Popen(["ldd", elf_file],
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.STDOUT,
                                      env = os.environ).communicate()[0].strip().split("\n")

        ldd_unused, ldd_undefined = subprocess.Popen(["ldd", "-u", "-r", elf_file],
                                                   stdout=subprocess.PIPE,
                                                   stderr=subprocess.PIPE,
                                                   env = os.environ).communicate()

        runpath  = subprocess.Popen(["chrpath", "-l", elf_file],
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.STDOUT,
                                      env = os.environ).communicate()[0].strip().split(": ")

        objdump_needed = [line.strip().split()[1] for line in \
                os.popen("objdump -p \"%s\" | grep 'NEEDED'" % elf_file).readlines()]


        # Process the various ldd and objdump outputs
        processed_needed, processed_broken, processed_unused, processed_undefined = \
        process_ldd(objdump_needed, ldd_output, ldd_unused, ldd_undefined)

        # association with each single elf file
        result_unused.update(dict([(elf_file, processed_unused)]))
        result_undefined.update(dict([(elf_file, processed_undefined)]))
        result_runpath.update(dict([(elf_file, runpath)]))
        result_broken = processed_broken
        result_dependencies[elf_file] =  check_objdump(processed_needed, package_elf_files, package_name)

    # Check for .pc files
    for pc_file in package_pc_files:
        result_dependencies[pc_file] = check_pc_files(pc_file)

    return (result_dependencies, result_broken, result_unused, result_undefined, result_runpath)

def colorize(msg, color, nocolor=False):
    """Colorizes the given message."""
    # The nocolor is added to shut off completely. You may ask the point of this
    # someone want to pipe the output, but the asci characters will also printed
    if nocolor:
        return msg
    else:
        colors = {'green'   : '\x1b[32;01m%s\x1b[0m',
                  'red'     : '\x1b[31;01m%s\x1b[0m',
                  'yellow'  : '\x1b[33;01m%s\x1b[0m',
                  'bold'    : '\x1b[1;01m%s\x1b[0m',
                  'none'    : '\x1b[0m%s\x1b[0m',
                 }
        return colors[color if sys.stdout.isatty() else 'none'] % msg

def main(arg):
    '''Initialize packages and get the results. Prints them out '''
    # This is of type dictionary, it includes all the
    # options from the parser such as option.directory, etc.
    option = arg[0]

    # Arguments are stored here,
    # such as the path of -d, or the pisi file.
    packages = arg[1]

    # checklib is executed plain only, no packages are
    # defined. It will look for pisi files inside that directory
    # where checklib is executed
    if not packages:
        pisi_files = glob.glob("*.pisi")
        if pisi_files:
            packages.extend(pisi_files)

    # If directory is used as option
    if option.directory:
        if option.recursive:
            for root, dirs, files in os.walk(option.directory):
                for data in files:
                    if data.endswith(".pisi"):
                        packages.append(os.path.join(root, data))
        else:
            # No recursion is used, just get the pisi
            # files from directory specified with -d
            pisi_files = glob.glob("%s/*.pisi" % option.directory)
            packages.extend(pisi_files)

    # check for components, like system.base, tex.language, etc.
    if option.component:
        cdb = pisi.db.componentdb.ComponentDB()
        for repo in pisi.db.repodb.RepoDB().list_repos():
            if cdb.has_component(option.component):
                packages.extend(cdb.get_packages(option.component, repo))

    # check for all packages installed on the machine
    if option.installedlist:
        packages.extend(INSTALLDB.list_installed())

    used_pisi = False # Do not check for a pisi binary file and for a package installed on the system
    for package in packages:
        # Check loop for .pisi files
        if package.endswith(".pisi"):
            used_pisi = True
            package_pisi = pisi.package.Package(package)
            package_meta = package_pisi.get_metadata()
            package_name = package_meta.package.name

            # Gather runtime dependencies directly from the metadata.xml
            package_deps = [dep.name() for dep in package_meta.package.runtimeDependencies()]

            # Contains extracted package content
            package_tempdir = tempfile.mkdtemp(prefix=os.path.basename(sys.argv[0]) + '-')
            package_pisi.extract_install(package_tempdir)

            # Get results from objdump,ldd,etc...
            result_dependencies, result_broken, result_unused, result_undefined, result_runpath = \
            output_result(package_name, package_tempdir)

            # Look for intersections of the packages(i.e. do not include system.base packages)
            # result_lists is a iteration object which contains tuples of length 3
            # this tuple makes it easy to print the missing dependencies. look for print_results()
            result_lists = check_intersections(result_dependencies, package_deps, package_name, option.systembase, option.systemdevel)

            # Print the results in a fancy output
            print_results(result_broken, result_unused, result_undefined, result_lists, result_runpath, package_name, option)

            # Delet the created temporary directory
            if package_tempdir.startswith("/tmp/"):
                shutil.rmtree(package_tempdir)

        # Check for a installed package in the system
        elif package in INSTALLDB.list_installed():
            if used_pisi:
                print "You've checked for a pisi file before\nPlease do not check for a installed package and pisi file at the same time"
                sys.exit(1)
            else:
                package_name = package

                # Gather runtime dependencies directly from the database of installed packages
                package_deps = [dep.name() for dep in INSTALLDB.get_package(package).runtimeDependencies()]
                package_tempdir = False # There is no need of temporary directory, hence we look for files that are installed

                # Same functions in the above part. You can read them
                result_dependencies, result_broken, result_unused, result_undefined, result_runpath = \
                output_result(package_name, package_tempdir)

                result_lists = check_intersections(result_dependencies, package_deps, package_name, option.systembase, option.systemdevel)
                print_results(result_broken, result_unused, result_undefined, result_lists, result_runpath, package_name, option)

        else:
            print "Error: '%s' is not a valid .pisi file or an installed package\nPlease use -d <path> option for a directory" % package

def print_results(result_broken, result_unused, result_undefined, result_lists, result_runpath, package_name, option):
    '''Print the final results in fancy colors'''

    def print_header(title, nocolor, color):
        print colorize("\n%s" % title, color , nocolor)
        print colorize("%s" % (len(title) * '-'), color, nocolor)

    def print_unused(result_unused, result_broken):
        header_dumped = False

        # Mark broken libs
        for elf_file, libs in result_unused.items():
            result_unused[elf_file] = map(lambda x: ("%s (broken)" % x) if x in result_broken else x, libs)

        for elf_file, libs in result_unused.items():
            if libs:
                if not header_dumped:
                    print_header("Unused direct dependency analysis", option.nocolor, 'green')
                    header_dumped = True
                print colorize(elf_file, 'red', option.nocolor)
                for data in libs:
                    print "  ", data

    def print_undefined(result_undefined):
        header_dumped = False
        for elf_file, libs in result_undefined.items():
            if libs:
                if not header_dumped:
                    print_header("Undefined symbol analysis", option.nocolor, 'green')
                    header_dumped = True
                print colorize(elf_file, 'red', option.nocolor)
                for data in libs:
                    print "  ", data

    def print_runpath(result_runpath):
        header_dumped = False
        for elf_file, libs in result_runpath.items():
            if libs:
                if "RPATH" in libs[1]:
                    if not header_dumped:
                        print_header("Runpath analysis", option.nocolor, 'green')
                        header_dumped = True
                    print colorize(elf_file, 'red', option.nocolor)
                    print "  ", libs[1]

    def print_dependencies(result_lists):
        print colorize("\nWritten dependencies           Detected dependencies          Missing dependencies", 'green', option.nocolor)
        print colorize("----------------------------------------------------------------------------------", 'green', option.nocolor)

        for tuple_deps in result_lists:
            for deps in tuple_deps:
                if "(base)" in deps:
                    print "%s" % colorize(deps.ljust(30), 'red', option.nocolor),
                elif "(devel)" in deps:
                    print "%s" % colorize(deps.ljust(30), 'yellow', option.nocolor),
                else:
                    print deps.ljust(30),
            print

    def print_missing(result_lists, plain_list):
        if not plain_list:
            print_header("Missing dependencies", option.nocolor, 'green')

        for tuple_deps in result_lists:
            pkg = tuple_deps[2]
            if "(base)" in pkg:
                print "%s" % colorize(pkg, 'red', option.nocolor)
            elif pkg:
                print pkg

    if not option.plain_list:
        print_header("Package: %s" % package_name, option.nocolor, 'bold')

    # This part is for the behavior of checklib argument parsing
    # If no options are used at all, than we show all options
    # If any of the other options is used, only the choosen ones are showed
    if not option.unused and not option.undefined and not option.dependencies \
    and not option.runpath and not option.missing:
        print_unused(result_unused, result_broken)
        print_undefined(result_undefined)
        print_runpath(result_runpath)
        print_dependencies(result_lists)

    else:
        if option.unused:
            print_unused(result_unused, result_broken)
        if option.undefined:
            print_undefined(result_undefined)
        if option.runpath:
            print_runpath(result_runpath)
        if option.dependencies:
            print_dependencies(result_lists)
        if option.missing:
            print_missing(result_lists, option.plain_list)

def argument():
    '''Command line argument parsing'''
    # TODO: use argparse() in the future

    parser = optparse.OptionParser(usage="Usage:  %prog [options] foo.pisi foo2.pisi \n \t%prog [options] -d  <path>\n \t%prog [options]\n \t%prog [options] foo",
                                  version="%prog 0.1")

    # Group options
    # check_options = optparse.OptionGroup(parser, "Check Options")

    parser.add_option("-n", "--no-color",
                     action="store_true",
                     dest="nocolor",
                     default=False,
                     help="Do not colorize the output (useful for piping the output)")

    parser.add_option("-l", "--plain-list",
                     action="store_true",
                     dest="plain_list",
                     default=False,
                     help="Don't prettify the outputs, only a list of packages")

    parser.add_option("-u", "--unused",
                     action="store_true",
                     dest="unused",
                     default=False,
                     help="Show only unused direct dependencies")

    parser.add_option("-f", "--undefined",
                     action="store_true",
                     dest="undefined",
                     default=False,
                     help="Show only undefined symbols")

    parser.add_option("-m", "--missing",
                     action="store_true",
                     dest="missing",
                     default=False,
                     help="Show only missing dependencies")

    parser.add_option("-t", "--dependencies",
                     action="store_true",
                     dest="dependencies",
                     default=False,
                     help="Show dependencies in a table")

    parser.add_option("-p", "--runpath",
                     action="store_true",
                     dest="runpath",
                     default=False,
                     help="Show RPATH status")

    parser.add_option("-s", "--systembase",
                     action="store_true",
                     dest="systembase",
                     default=False,
                     help="Don't hide system.base dependencies")

    parser.add_option("-x", "--systemdevel",
                     action="store_true",
                     dest="systemdevel",
                     default=False,
                     help="Show(colorize) system.devel dependencies")

    parser.add_option("-c", "--component",
                     action="store",
                     dest="component",
                     type="string",
                     help="Check a whole component")

    parser.add_option("-a", "--all",
                     action="store_true",
                     dest="installedlist",
                     default=False,
                     help="Check all installed packages")

    parser.add_option("-d", "--directory",
                     action="store",
                     dest="directory",
                     type="string",
                     metavar="<path>",
                     help="Specify a folder to check")

    parser.add_option("-r", "--recursive",
                     action="store_true",
                     dest="recursive",
                     default=False,
                     help="Check recursively in the specified folder")

    return parser.parse_args()

if __name__ == "__main__":
    args = argument()
    sys.exit(main(args))
 
