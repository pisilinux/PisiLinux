#!/bin/sh
export GEODB_DIR="/usr/share/GeoDB"
export DL_FILE="webalizer-geodb-latest.tgz"

wget -P $GEODB_DIR ftp://ftp.mrunix.net/pub/webalizer/$DL_FILE

if [ -f $GEODB_DIR/$DL_FILE ] ; then
   cd $GEODB_DIR
   tar zxf $DL_FILE
   chown root: GeoDB.dat GEODB.README
   rm -f $GEODB_DIR/$DL_FILE
   echo '** You must uncomment and set to "yes" GeoDB option in /etc/webalizer.conf to activate GeoDB lookup support **'
fi
