#!/bin/sh

# NVIDIA Graphics Driver bug reporting shell script.  This shell
# script will generate a log file named "nvidia-bug-report.log", which
# should be attached when emailing bug reports to NVIDIA.



LOG_FILENAME=nvidia-bug-report.log


PATH="/sbin:/usr/sbin:$PATH"


NVIDIA_BUG_REPORT_CHANGE="$Change: 2074027 $"
NVIDIA_BUG_REPORT_VERSION=`echo $NVIDIA_BUG_REPORT_CHANGE | tr -c -d [:digit:]`

#
# append() - append the contents of the specified file to the log
#

append() {
    echo "____________________________________________" >> $LOG_FILENAME
    echo ""                                             >> $LOG_FILENAME

    if [ ! -f "$1" ]; then
        echo "$1 does not exist"                        >> $LOG_FILENAME
    elif [ ! -r "$1" ]; then
        echo "$1 is not readable"                       >> $LOG_FILENAME
    else
        echo "$1"                                       >> $LOG_FILENAME
        cat  "$1"                                       >> $LOG_FILENAME
    fi
    echo ""                                             >> $LOG_FILENAME
}

#
# append_silent() - same as append(), but don't print anything
# if the file does not exist
#

append_silent() {
    if [ -f "$1" -a -r "$1" ]; then
        echo "____________________________________________" >> $LOG_FILENAME
        echo ""                                             >> $LOG_FILENAME
        echo "$1"                                           >> $LOG_FILENAME
        cat  "$1"                                           >> $LOG_FILENAME
        echo ""                                             >> $LOG_FILENAME
    fi
}

#
# append_glob() - use the shell to expand a list of files, and invoke
# append() for each of them
#

append_glob() {
    for i in `ls $1 2> /dev/null;`; do
        append "$i"
    done
}



#
# Start of script
#


# check that we are root (needed for `lspci -vxxx` and potentially for
# accessing kernel log files)

if [ `id -u` -ne 0 ]; then
    echo "ERROR: Please run $(basename $0) as root."
    exit 1
fi


# move any old log file out of the way

if [ -f $LOG_FILENAME ]; then
    mv $LOG_FILENAME ${LOG_FILENAME}.old
fi


# make sure what we can write to the log file

touch $LOG_FILENAME 2> /dev/null

if [ $? -ne 0 ]; then
    echo
    echo "ERROR: Working directory is not writable; please cd to a directory"
    echo "       where you have write permission so that the $LOG_FILENAME"
    echo "       file can be written."
    echo
    exit 1
fi


# print a start message to stdout

echo ""
echo -n "Running $(basename $0)...";


# print prologue to the log file

echo "____________________________________________"                    >> $LOG_FILENAME
echo ""                                                                >> $LOG_FILENAME
echo "Start of NVIDIA bug report log file.  Please send this report,"  >> $LOG_FILENAME
echo "along with a description of your bug, to linux-bugs@nvidia.com." >> $LOG_FILENAME  
echo ""                                                                >> $LOG_FILENAME
echo "nvidia-bug-report.sh Version: $NVIDIA_BUG_REPORT_VERSION"        >> $LOG_FILENAME
echo ""                                                                >> $LOG_FILENAME
echo "Date: `date`"                                                    >> $LOG_FILENAME
echo "uname: `uname -a`"                                               >> $LOG_FILENAME
echo ""                                                                >> $LOG_FILENAME


# append useful files

append "/proc/driver/nvidia/version"

append_glob "/proc/driver/nvidia/cards/*"
append_glob "/proc/driver/nvidia/agp/*"

append_glob "/proc/driver/nvidia/warnings/*"
append "/proc/driver/nvidia/registry"

append "/proc/cmdline"
append "/proc/cpuinfo"
append "/proc/interrupts"
append "/proc/meminfo"
append "/proc/modules"
append "/proc/version"
append "/proc/pci"
append "/proc/iomem"
append "/proc/mtrr"

append "/etc/issue"

append_silent "/etc/redhat-release"
append_silent "/etc/redhat_version"
append_silent "/etc/fedora-release"
append_silent "/etc/slackware-release"
append_silent "/etc/slackware-version"
append_silent "/etc/debian_release"
append_silent "/etc/debian_version"
append_silent "/etc/mandrake-release"
append_silent "/etc/yellowdog-release"
append_silent "/etc/sun-release"
append_silent "/etc/release"
append_silent "/etc/gentoo-release"

append "/var/log/nvidia-installer.log"

# append the X log; also, extract the config file named in the X log
# and append it

for i in /var/log/XFree86.0.log /var/log/Xorg.0.log ; do
    append "$i"
    if [ -f $i -a -r $i ]; then
        j=`grep "Using config file" $i | cut -f 2 -d \"`
        append "$j"
    fi
done

# append ldd info

glxinfo=`which glxinfo 2> /dev/null | head -n 1`

echo "____________________________________________"                    >> $LOG_FILENAME
echo ""                                                                >> $LOG_FILENAME

if [ $? -eq 0 -a "$glxinfo" ]; then
    echo "ldd $glxinfo"                                                >> $LOG_FILENAME
    echo ""                                                            >> $LOG_FILENAME
    ( ldd $glxinfo >> $LOG_FILENAME ; exit 0 ) > /dev/null 2>&1
    echo ""                                                            >> $LOG_FILENAME
else
    echo "Skipping ldd output (glxinfo not found)"                     >> $LOG_FILENAME
    echo ""                                                            >> $LOG_FILENAME
fi

# lspci information

lspci=`which lspci 2> /dev/null | head -n 1`

echo "____________________________________________"                    >> $LOG_FILENAME
echo ""                                                                >> $LOG_FILENAME

if [ $? -eq 0 -a "$lspci" ]; then
    echo "$lspci -d \"10de:*\" -v -xxx"                                >> $LOG_FILENAME
    echo ""                                                            >> $LOG_FILENAME
    ( $lspci -d "10de:*" -v -xxx >> $LOG_FILENAME ; exit 0 ) > /dev/null 2>&1
    echo ""                                                            >> $LOG_FILENAME
    echo "____________________________________________"                >> $LOG_FILENAME
    echo ""                                                            >> $LOG_FILENAME
    echo "$lspci -t"                                                   >> $LOG_FILENAME
    echo ""                                                            >> $LOG_FILENAME
    ( $lspci -t >> $LOG_FILENAME ; exit 0 ) > /dev/null 2>&1
    echo ""                                                            >> $LOG_FILENAME
else
    echo "Skipping lspci output (lspci not found)"                     >> $LOG_FILENAME
    echo ""                                                            >> $LOG_FILENAME
fi

# dmidecode

dmidecode=`which dmidecode 2> /dev/null | head -n 1`

echo "____________________________________________"                    >> $LOG_FILENAME
echo ""                                                                >> $LOG_FILENAME

if [ $? -eq 0 -a "$dmidecode" ]; then
    echo "$dmidecode"                                                  >> $LOG_FILENAME
    echo ""                                                            >> $LOG_FILENAME
    ( $dmidecode >> $LOG_FILENAME ; exit 0 ) > /dev/null 2>&1
    echo ""                                                            >> $LOG_FILENAME
else
    echo "Skipping dmidecode output (dmidecode not found)"             >> $LOG_FILENAME
    echo ""                                                            >> $LOG_FILENAME
fi

# module version magic

modinfo=`which modinfo 2> /dev/null | head -n 1`

echo "____________________________________________"                    >> $LOG_FILENAME
echo ""                                                                >> $LOG_FILENAME

if [ $? -eq 0 -a "$modinfo" ]; then
    echo "$modinfo nvidia | grep vermagic"                             >> $LOG_FILENAME
    echo ""                                                            >> $LOG_FILENAME
    ( $modinfo nvidia | grep vermagic >> $LOG_FILENAME ; exit 0 ) > /dev/null 2>&1
    echo ""                                                            >> $LOG_FILENAME
else
    echo "Skipping modinfo output (modinfo not found)"                 >> $LOG_FILENAME
    echo ""                                                            >> $LOG_FILENAME
fi

# get any relevant kernel messages

echo "____________________________________________"                    >> $LOG_FILENAME
echo ""                                                                >> $LOG_FILENAME
echo "Scanning kernel log files for NVRM messages:"                    >> $LOG_FILENAME
echo ""                                                                >> $LOG_FILENAME

for i in /var/log/messages /var/log/kernel.log ; do
    if [ -f $i ]; then
        echo "  $i:"                                                   >> $LOG_FILENAME
        ( cat $i | grep NVRM >> $LOG_FILENAME ; exit 0 ) > /dev/null 2>&1
    fi
done

# append dmesg output

echo ""                                                                >> $LOG_FILENAME
echo "____________________________________________"                    >> $LOG_FILENAME
echo ""                                                                >> $LOG_FILENAME
echo "dmesg:"                                                          >> $LOG_FILENAME
echo ""                                                                >> $LOG_FILENAME
( dmesg >> $LOG_FILENAME ; exit 0 ) > /dev/null 2>&1

which gcc >/dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "____________________________________________"                >> $LOG_FILENAME
    echo ""                                                            >> $LOG_FILENAME
    ( gcc -v 2>> $LOG_FILENAME ; exit 0 ) > /dev/null 2>&1
fi

which g++ >/dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "____________________________________________"                >> $LOG_FILENAME
    echo ""                                                            >> $LOG_FILENAME
    ( g++ -v 2>> $LOG_FILENAME ; exit 0 ) > /dev/null 2>&1
fi

echo "____________________________________________"                    >> $LOG_FILENAME
echo ""                                                                >> $LOG_FILENAME
echo "xset -q:"                                                        >> $LOG_FILENAME
echo ""                                                                >> $LOG_FILENAME

( xset -q >> $LOG_FILENAME & sleep 1 ; kill -9 $! ) > /dev/null 2>&1

if [ $? -eq 0 ]; then
    # The xset process is still there.
    echo "xset could not connect to an X server"                       >> $LOG_FILENAME
fi

echo "____________________________________________"                    >> $LOG_FILENAME
echo ""                                                                >> $LOG_FILENAME
echo "nvidia-settings -q all:"                                         >> $LOG_FILENAME
echo ""                                                                >> $LOG_FILENAME

( nvidia-settings -q all >> $LOG_FILENAME & sleep 1 ; kill -9 $! ) > /dev/null 2>&1

if [ $? -eq 0 ]; then
    # The nvidia-settings process is still there.
    echo "nvidia-settings could not connect to an X server"            >> $LOG_FILENAME
fi
echo "____________________________________________"                    >> $LOG_FILENAME

# print epilogue to log file

echo ""                                                                >> $LOG_FILENAME
echo "End of NVIDIA bug report log file."                              >> $LOG_FILENAME


# Done

echo " complete."
echo ""
echo "The file $LOG_FILENAME has been created; please send this report,"
echo "along with a description of your bug, to linux-bugs@nvidia.com."
echo ""
