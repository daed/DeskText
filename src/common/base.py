import saneConf

class baseClass:
    def __init__(self):
        pass

def dprint(text):
    if saneConf.debug:
        print(text)
    return