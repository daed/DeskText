# bgInfosane Design Plan

## Goals
Provide a means of displaying information on the desktop in the form of a wallpaper overlay.
- Information MUST be user configurable
- Configuration MUST allow sourcing information via:
    - commands
    - shell scripts
    - python
- Additional sources in the future MAY include direct database connections, etc.
- Setup scripts MAY be written as batch / bash files, but the program itself MUST be written in python.
- All python should be compatible with both 2.7 and 3.4 if possible.

## Flow
- Check installation prereqs
- Read configuration file
- Gather information per config
- Transform and composite over wallpaper
- Loop as needed.

