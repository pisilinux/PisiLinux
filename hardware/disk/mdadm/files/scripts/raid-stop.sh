[[ -f /proc/mdstat ]] || exit 0

[[ -e /etc/mdadm.conf ]] && mdadm_conf="/etc/mdadm.conf"
if [[ -x /sbin/mdadm && -f ${mdadm_conf} ]] ; then
	ebegin "Shutting down RAID devices (mdadm)"
	output=$(mdadm -Ss 2>&1)
	ret=$?
	[[ ${ret} -ne 0 ]] && echo "${output}"
	eend ${ret}
fi
