# TIMIDITY_OPTS
# Command line arguements to be passed to timidity. -iA is always used
# Common options:
# -Os : Output to ALSA pcm device
# -Oe : Output to esd
# -On : Output to NAS
# -Oj : Output to JACK
#
# -B<n>,<m> :  Set number of buffer fragments(n), and buffer size(2^m)
#
# -EFreverb=0         : Disable MIDI reverb effect control
# -EFreverb=1[,level] : Enable MIDI reverb effect control
#                       "level" is optional to specify reverb level [0..127]
#                       This effect is only available in stereo
#                       (default)
# -EFreverb=2         : Global reverb effect

TIMIDITY_OPTS="-B2,8 -Os -EFreverb=0 -EFchorus=0"

# USE_ESOUND
# if you want to use esound, make this option yes and set the correct TIMIDITY_OPTS

USE_ESOUND="no"

# PATCHSET
# Define the sound patch set that timidity will use. Default is shompatches.
PATCHSET="shompatches"


# TIMIDITY_PCM_NAME
# This option can be used to choose an alternate ALSA pcm device.  This will
# be most useful for users of the dmix alsa plugin or those with multiple
# cards.  If you don't know what this is, chances are you want the default.

# default alsa device fails to work as a service, since pulseaudio is not reachable
# from the service scripts' environment. Workaround with using hw:0
#TIMIDITY_PCM_NAME="default"
TIMIDITY_PCM_NAME="hw:0"

