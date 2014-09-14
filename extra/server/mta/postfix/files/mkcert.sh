#!/bin/sh

# Accept one parameter as output file names
# Generates a self-signed certificate.
# Edit EOF section before running

if [ $# -ne 1 ]
then
    echo -e "\nUse with a single name paramater for output files will be generated into current folder.\nAnd don't forget to edit [ req_dn ] section in script.\n"
    echo -e "Example:\n\n./mkcert.sh foo\n\n"
    exit 1
fi

OPENSSL=openssl
DIR=`pwd`
CONFIG=$1-ssl.config

CERTDIR=$SSLDIR
KEYDIR=$SSLDIR

CERTFILE=$DIR/$1.cert
KEYFILE=$DIR/$1.key
REQFILE=$DIR/$1.req

KEYBITS=1024
DAYS=3650

if [ ! -f $CONFIG ]; then
  cat > $CONFIG << EOF
[ req ]
default_bits = 1024
encrypt_key = yes
distinguished_name = req_dn
x509_extensions = cert_type
prompt = no

[ req_dn ]
# country (2 letter code)
C=XY

# State or Province Name (full name)
ST=SomeState

# Locality Name (eg. city)
L=SomeCity

# Organization (eg. company)
O=SomeCompany

# Organizational Unit Name (eg. section)
OU=PisiLinux

# Common Name (*.example.com is also possible)
CN=mail.example.com

# E-mail contact
#emailAddress=admin@example.com

[ cert_type ]
nsCertType = server
EOF
fi

if [ -f $CERTFILE ]; then
  echo "$CERTFILE already exists, won't overwrite"
  exit 1
fi

if [ -f $KEYFILE ]; then
  echo "$KEYFILE already exists, won't overwrite"
  exit 1
fi

#Generate key. Use -des3 for password protected key.
$OPENSSL genrsa -out $KEYFILE $KEYBITS
chmod 0600 $KEYFILE

#Unmask password protected key
#mv $KEYFILE $KEYFILE.orig
#$OPENSSL rsa -in $KEYFILE.orig -out $KEYFILE

#Generate request file
$OPENSSL req -new -key $KEYFILE -out $REQFILE -config $CONFIG

#Generate self signed certificate
$OPENSSL x509 -req -days $DAYS -in $REQFILE  -signkey $KEYFILE -out $CERTFILE

#Verify
$OPENSSL x509 -subject -fingerprint -noout -in $CERTFILE || exit 2
