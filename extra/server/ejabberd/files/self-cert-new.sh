#! /bin/sh
#
# self-cert.sh for ejabberd

pemfile="ejabberd.pem"

cd /etc/ejabberd

if [ ! -f $pemfile ]
then
    echo "Generating SSL certificate /etc/ejabberd/$pemfile..."
    HOSTNAME=`hostname -s 2>/dev/null || echo "localhost"`
    DOMAINNAME=`hostname -d 2>/dev/null || echo "localdomain"`
    openssl req -new -x509 -days 365 -nodes -out $pemfile \
                -keyout $pemfile > /dev/null 2>&1 <<+++
.
.
.
$DOMAINNAME
$HOSTNAME
ejabberd
root@$HOSTNAME.$DOMAINNAME
+++

chown ejabberd:ejabberd $pemfile
chmod 600 $pemfile
fi

#dd if=/dev/urandom of=$randfile count=1 2>/dev/null
#/usr/bin/openssl req -new -x509 -days 365 -nodes \
#        -config /etc/jabber/ssl.cnf -out $pemfile -keyout $pemfile || cleanup
#/usr/bin/openssl gendh -rand $randfile 512 >> $pemfile || cleanup
#/usr/bin/openssl x509 -subject -dates -fingerprint -noout -in $pemfile || cleanup
#rm -f $randfile
