'''
    saneConf.py

Default program-wide config parameters.

home  - Home directory of the program.  This is used to set where temporary files are kept.
          See also 'temp'
debug - Output verbose debugging information to terminal.
timer - Number of seconds to wait before looping.
temp  - Actual working directory for temporary wallpapers

'''

# happy little defaults

home = "."

debug = True
timer = 60
temp = home + "/.bginfo"