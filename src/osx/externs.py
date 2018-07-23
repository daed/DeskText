'''
externs.py

This file contains functions for use with all major external commands to be run.

Probably will be heavily OS specific.

'''
from base import baseClass, dprint
import saneConf
import subprocess

#convert darkblue.jpg -pointsize 20 -font Verdana -background none -gravity SouthEast -density 120 \
#    -fill white label:@bgout.out -geometry +100+100 -composite darkblue-comp.jpg
def label(text, offsetx, offsety):
    cmd=["convert", 
        "-pointsize", "24",
        "-font", "Verdana",
        "-background", "none",
        "-gravity", "West",
        "-density", "120",
        "-fill", "white",
        "label:" + text,
        "-geometry", offsetx + offsety,
        saneConf.temp + "/text.png"]
    dprint(cmd) 
    p = subprocess.Popen(cmd,stdout=subprocess.PIPE)
    return p


def composite(inputFilename, outputFilename):
    cmd = ["composite",
           saneConf.temp + "/text.png",
           inputFilename,  
           "-gravity", "SouthEast", 
           outputFilename ]
    dprint(cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    return p

def getWallpaper():
    cmd = ["osascript", "src/osx/getBg.osa"]
    dprint(cmd)
    p = subprocess.Popen(cmd,stdout=subprocess.PIPE)
    wallFile = p.stdout.read()
    return wallFile.strip()


def setWallpaper(path):
    cmd = ["wallpaper", path]
    dprint(cmd)
    subprocess.Popen(cmd)


def shell(cmd):
    dprint(cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    return p
    