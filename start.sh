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
    src/osx/prereqs.sh
    if [ $? -eq 0 ]; then
        # do darwin stuff here
        echo "I do osx stuff now"
        echo `pwd`
        export PYTHONPATH="src/common:src/osx"
        python src/test/testExterns.py
    else
        exit 1
    fi
elif [[ $DISTRO == *linux* ]]; then
    echo -e "Linux detected"
elif [[ $DISTRO == *windows ]]; then
    echo -e "I'm not even sure this can happen"
fi
