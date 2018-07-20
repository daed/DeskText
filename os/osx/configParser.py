#!/usr/bin/env python
f = open("conf/client/osx.cfg")

for line in f.readlines():
    # discard comments and blank lines
    if line.startswith("#") or line.strip() == "":
        continue
    
    if "HEADER=" in line:
        print("header found: " + line.split("=")[1].strip())
    else:
        try:
            print(line.split(" X ")[0].strip())
        except IndexError:
            continue
f.close()

