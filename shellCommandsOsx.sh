convert darkblue.jpg -pointsize 20 -font Verdana -background none -gravity SouthEast -density 120 \
    -fill white label:@bgout.out -geometry +100+100 -composite darkblue-comp.jpg
WINDOWS_GET="regtool.exe -w -v get \"/HKEY_CURRENT_USER/Control Panel/Desktop/Wallpaper\""
WINDOWS_SET="WallpaperChanger.exe \"${WALLPAPER}\" 2 \"${OUTUSERFOLDERWIN}/\" ; regtool.exe -w -v set \"/HKEY_CURRENT_USER/Control Panel/Desktop/Wallpaper\" \"${WALLPAPER}\""
CYGWIN_GET="regtool.exe -w -v get \"/HKEY_CURRENT_USER/Control Panel/Desktop/Wallpaper\""
CYGWIN_SET="WallpaperChanger.exe \"${WALLPAPER}\" 2 \"${OUTUSERFOLDERWIN}/\" ; regtool.exe -w -v set \"/HKEY_CURRENT_USER/Control Panel/Desktop/Wallpaper\" \"${WALLPAPER}\""
LINUX_GET="gsettings get org.gnome.desktop.background picture-uri"
LINUX_SET="gsettings set org.gnome.desktop.background picture-uri file://\"${WALLPAPER}\""
MACOSX_GET="osascript /usr/local/bin/BGINFO4X/CUSTOM/CONF/getOsxBackground.osa"
MACOSX_SET="wallpaper \"${WALLPAPER}\""
