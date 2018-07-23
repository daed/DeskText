# 
#  We check for prereqs before trying and failing.
#
# Need:
# - brew install wallpaper
# - brew install imagemagick
# - brew install ghostscript
#
#

# check for wallpaper

YES="[ \xE2\x9C\x94 ]"
NOPE="[ \xE2\x9D\x8C ]"
ERR=0

### Function declarations
# checkExists(command, packageName)
function checkExists()
{
    if [ -z `which $1` ]
    then
        echo -e "$NOPE $1 is not installed or not in path.  Please run 'brew install $2' and make sure it is in your path"
        ERR=1
    else
        echo -e "$YES $1 at `which $1`"
    fi
}

### Main program starts here

echo -e "Checking prerequities for bgInfosane"

if [ -z `which brew` ]
then
    echo -e "$NOPE brew isn't installed so we're not going to try to continue.  Please install brew from https://brew.sh"
    exit 1
else
    echo -e "$YES Brew is installed at `which brew`"
fi

checkExists "python" "python@2"
checkExists "wallpaper" "wallpaper"
checkExists "convert" "imagemagick"
checkExists "gs" "ghostscript"

if [ $ERR -eq 0 ]
then
    echo -e "$YES All prerequesites were met."
else
    echo -e "$NOPE One or more prerequsites are not met.  Please review output.\n"
fi
