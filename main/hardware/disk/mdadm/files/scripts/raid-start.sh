[[ -f /proc/mdstat ]] || exit 0

# Try to make sure the devices exist before we use them
create_devs() {
	local node dir minor
	for node in $@ ; do
		[[ ${node} != /dev/* ]] && node=/dev/${node}
		[[ -e ${node} ]] && continue

		dir=${node%/*}
		[[ ! -d ${dir} ]] && mkdir -p "${dir}"

		minor=${node##*/}
		mknod "${node}" b ${MAJOR} ${minor##*md} &> /dev/null
	done
}

[[ -e /etc/mdadm.conf ]] && mdadm_conf="/etc/mdadm.conf"
if [[ -x /sbin/mdadm && -f ${mdadm_conf} ]] ; then
	devs=$(awk '/^[[:space:]]*ARRAY/ { print $2 }' ${mdadm_conf})
	if [[ -n ${devs} ]] ; then
		create_devs ${devs}
		ebegin "Starting up RAID devices (mdadm)"
		output=$(mdadm -As 2>&1)
		ret=$?
		[[ ${ret} -ne 0 ]] && echo "${output}"
		eend ${ret}
	fi
fi
