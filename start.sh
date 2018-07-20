#
#  - check prereqs for os
#  - read configs for os
#  - start responsible script for os
#
#
#
#

DISTRO=`uname -a`

echo "Starting bgInfosane"
if [[ $DISTRO == *Darwin* ]]; then
    echo -e "Darwin detected, assuming OSX/MacOS"
    os/osx/prereqs.sh
    if [ $? -eq 0 ]; then
        # do darwin stuff here
        echo "I do osx stuff now"
    else
        exit 1
    fi
fi