#
#  - check prereqs for os
#  - read configs for os
#  - start responsible script for os
#
#
#
#

DISTRO=`uname -a`
#TESTNAMES='testConfigParser.py testExterns.py'

echo "Starting bgInfosane"
if [[ $DISTRO == *Darwin* ]]; then
    echo -e "Darwin detected, assuming OSX/MacOS"
    src/osx/prereqs.sh
    if [ $? -eq 0 ]; then
        # do darwin stuff here
        echo "I do osx stuff now"
        export PYTHONPATH="src/common:src/osx:src"
        echo "Running tests..."
        python src/test/tests.py
        python src/bgInfosane.py
        #echo "------------------------------------"
        #for test in $TESTNAMES; do
        #    python src/test/$test
        #    
        #    echo "------------------------------------"
        #done
    else
        exit 1
    fi
elif [[ $DISTRO == *linux* ]]; then
    echo -e "Linux detected"
elif [[ $DISTRO == *windows ]]; then
    echo -e "I'm not even sure this can happen"
fi
