'''

bgInfosane - No capslock edition!



'''

import platform
import base
import ruleConf
import saneConf
from getData import GetData
from configParser import ConfigParser
import os
import time
import signal
import sys

osVer = platform.system()
try:
    os.mkdir(saneConf.temp)
except OSError:
    pass

if   osVer == "Darwin":
    import externs
    conf = ConfigParser("conf/client/osx.cfg").get()
elif osVer == "Windows":
    import externs
    conf = ConfigParser("conf/client/windows.cfg").get()
elif osVer == "Linux":
    import externs
    conf = ConfigParser("conf/client/linux.cfg").get()

def exit(signum, frame):
    externs.setWallpaper(bg)
    sys.exit()

signal.signal(signal.SIGINT, exit)

bg = externs.getWallpaper()
data = GetData(conf)
outFile = bg

while True:
    output = data.run()
    # Need serialize / deserialize methods before this is even an option
    # datFile = open(saneConf.temp + "/datout.txt", "w")
    # datFile.write(str(data))
    # datFile.close()

    if   "wallpaper1.jpg" in outFile:
        outFile = "/wallpaper2.jpg"
        try:
            os.remove(saneConf.temp + "/wallpaper1.jpg")
        except OSError:
            pass
    elif "wallpaper2.jpg" in outFile:
        outFile = "/wallpaper1.jpg"
        try:
            os.remove(saneConf.temp + "/wallpaper2.jpg")
        except OSError:
            pass
    else:
        outFile = "/wallpaper1.jpg"

    p = externs.label(output, "+100", "+100")
    p.wait()
    p = externs.composite(bg, saneConf.temp + outFile)
    p.wait()
    externs.setWallpaper(saneConf.temp + outFile)
    time.sleep(saneConf.timer)

