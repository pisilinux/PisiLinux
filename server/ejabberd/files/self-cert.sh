#! /bin/sh
#
# self-cert.sh for ejabberd, stolen from:
# mkimapdcert,v 1.1 2001/01/02 03:54:25 drobbins Exp
#
# Copyright 2000 Double Precision, Inc.  See COPYING for
# distribution information.
#
# This is a short script to quickly generate a self-signed X.509 key for
# eJabberd.  Normally this script would get called by an automatic
# package installation routine.

pemfile="/etc/ejabberd/ejabberd.pem"
randfile="/etc/ejabberd/ssl.rand"
conffile="/etc/ejabberd/ssl.cnf"

cleanup() {
        rm -f $pemfile $randfile
        exit 1
}

test -x /usr/bin/openssl || exit 0

if [ ! -f $pemfile ];
then
    HOSTNAME=`hostname -s 2>/dev/null || echo "localhost"`
    DOMAINNAME=`hostname -d 2>/dev/null || echo "localdomain"`

    dd if=/dev/urandom of=$randfile count=1 2>/dev/null

    /usr/bin/openssl req -new -x509 -days 365 -nodes \
            -config $conffile -out $pemfile -keyout $pemfile || cleanup

    /usr/bin/openssl gendh -rand $randfile 512 >> $pemfile || cleanup

    /usr/bin/openssl x509 -subject -dates -fingerprint -noout -in $pemfile || cleanup

    chown ejabberd:ejabberd $pemfile
    chmod 600 $pemfile

    rm -f $randfile
fi
