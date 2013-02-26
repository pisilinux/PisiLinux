#!/bin/bash

/sbin/ldconfig -n libpam/.libs
for module in modules/*/.libs/*.so  ; do
if  ! env LD_LIBRARY_PATH=libpam/.libs \
    ./dlopen.sh -ldl -lpam -Llibpam/.libs ${module} ; then
echo ERROR module: ${module} cannot be loaded.
exit 1
fi
done
