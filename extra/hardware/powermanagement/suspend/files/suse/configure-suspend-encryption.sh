#!/bin/bash
#
# configuration script for encrypted suspend
#
# (C) 2008 Stefan Seyfried <seife@suse.de> SUSE Linux Products GmbH
#     released under the GPL V2

CONF=/etc/suspend.conf

if [ $UID != 0 ]; then
	echo "Sorry, this configuration script needs root privileges."
	echo "Exiting now..."
	echo
	exit 1
fi

cat <<EOF
We are going to create the key for encrypted suspend now. There are some
questions we need to ask for:
- Key size.
  The longer the key, the harder it will be to break the encryption.
  On the other hand, the longer the key, the more computational power is
  needed, which means that the suspend and resume will be slightly slower.
  Nowadays, 1024 bits of key length might be too insecure for some users,
  the default of 2048 bits should be fine.
- Your passphrase. This passphrase protects the generated key. It should
  be sufficiently long and not easy to guess.
  This is the password you need to enter to resume from encrypted suspend.
  To make sure that you did not mistype the passphrase, you need to confirm
  it by entering it a second time.

The program will create the key and copy it to /etc/suspend.key, then it
will modify /etc/suspend.conf that from now on your suspend to disk image
will be encrypted. Note that creating the key might take some time,
depending on your machine. You can probably speed it up by using the mouse
and generating I/O, e.g. by starting other programs.

If you do not want to continue, press CTRL-C now.

EOF
# -q suppresses asking for the key file and makes it default
# to /etc/suspend.key
suspend-keygen -q

if [ $? != 0 ]; then
	echo
	echo "Something went wrong. Please check above for error messages."
	echo "/etc/suspend.conf is not modified."
	echo
	exit 1
fi

echo "We successfully generated /etc/suspend.key. Modifying suspend.conf now."

# backup...
cp -a $CONF ${CONF}.backup
# remove the encrypt and keyfile entries from the config file.
# the key file will default to /etc/suspend.key anyway
sed -i '/^encrypt /d;/^RSA key file /d;' $CONF
echo "encrypt = y" >> $CONF

# if we have more than one CPU / core, enabling threads will speed up
# suspend.
NUMCPU=$(grep -c ^processor /proc/cpuinfo)
if [ $NUMCPU -gt 1 ]; then
	# remove the threads setting...
	sed -i '/^threads /d; ' $CONF
	# ..and add it back.
	echo "threads = y" >> $CONF
fi

echo
echo "/etc/suspend.conf written, you can find the original file as /etc/suspend.conf.backup"
echo

