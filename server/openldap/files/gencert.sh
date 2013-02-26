#!/bin/sh
# Last update 20050401 - Christian Zoffoli <xmerlin@gentoo.org>

VERSION="0.3"
openssl="/usr/bin/openssl"
opensslopts=""
ldapconfdir="/etc/openldap/ssl"
pemfile="${ldapconfdir}/ldap.pem"
randfile="${ldapconfdir}/ldap.rand"
cfgfile="${ldapconfdir}/ldap.cfg"

function fixperms {
	chown root:ldap ${ldapconfdir} -R
	find ${ldapconfdir} -type f -exec chmod 640 \{\} \;
	chmod 750 ${ldapconfdir}
}


if [ ! -x ${openssl} ]; then
	exit 0
fi

if [ ! -d ${ldapconfdir} ]; then
	mkdir -p ${ldapconfdir}
fi

fixperms

if [ -f ${pemfile} ]; then
	echo "${pemfile} already exist, dying"
	exit 0
fi


dd if=/dev/urandom of=$randfile count=1 2>/dev/null

echo ""
echo "______________________________________________________________________${T_ME}"
echo ""
echo "Creating self-signed certificate -- Version ${VERSION}"
echo ""
echo "______________________________________________________________________${T_ME}"
echo ""


COMMONNAME=`hostname`
if [ ! -n "$COMMONNAME" ]; then
	COMMONNAME="www.openldap.org"
fi


if [ -f ${cfgfile} ]; then
	echo "${cfgfile} found, would you like to use it ? (y/n)"
	read answer
	
	case "$answer" in
		y|Y)
			opensslopts="-batch"
		;;
		n|N)
			cat >${cfgfile} <<EOT
			[ req ]
			default_bits                    = 1024
			distinguished_name              = req_DN
			RANDFILE                        = ${randfile}
			[ req_DN ]
			countryName                     = "1. Country Name             (2 letter code)"
			countryName_default             = "US"
			countryName_min			= 2
			countryName_max			= 2
			stateOrProvinceName		= "2. State or Province Name   (full name)    "
			stateOrProvinceName_default	= ""
			localityName                    = "3. Locality Name            (eg, city)     "
			localityName_default		= ""
			0.organizationName		= "4. Organization Name        (eg, company)  "
			0.organizationName_default	= "LDAP Server"
			organizationalUnitName		= "5. Organizational Unit Name (eg, section)  "
			organizationalUnitName_default	= "For testing purposes only"
			commonName			= "6. Common Name              (eg, CA name)  "
			commonName_max			= 64
			commonName_default		= "${COMMONNAME}"
			emailAddress			= "7. Email Address            (eg, name@FQDN)"
			emailAddress_max		= 40
			emailAddress_default		= ""
EOT
		;;
		*)
			echo "Wrong answer, retry!"
			exit 1
		;;
	esac 
fi

echo ""

${openssl} req -config ${cfgfile} ${opensslopts} -new -rand ${randfile} -x509 -nodes -out ${pemfile} -keyout ${pemfile} -days 999999  

if [ $? -ne 0 ]; then
	echo "cca:Error: Failed to generate certificate " 1>&2
	exit 1
else
	echo -e "\nCertificate creation done!"
fi

if [ -f ${randfile} ]; then
	rm -f ${randfile}
fi

if [ -f ${pemfile} ]; then
	fixperms
fi
