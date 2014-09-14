#!/bin/bash

# Test Crypto:
./openvpn --genkey --secret key
./openvpn --test-crypto --secret key

# Randomize ports for tests to avoid conflicts on the build servers.
cport=$[ 50000 + ($RANDOM % 15534) ]
sport=$[ $cport + 1 ]
sed -e 's/^\(rport\) .*$/\1 '$sport'/' \
-e 's/^\(lport\) .*$/\1 '$cport'/' \
    < sample-config-files/loopback-client \
    > tmp-loopback-client
sed -e 's/^\(rport\) .*$/\1 '$cport'/' \
-e 's/^\(lport\) .*$/\1 '$sport'/' \
< sample-config-files/loopback-server \
> tmp-loopback-server

# Test SSL/TLS negotiations (runs for 2 minutes):
./openvpn --config tmp-loopback-client &

./openvpn --config tmp-loopback-server
wait

rm -f tmp-loopback-client tmp-loopback-server
