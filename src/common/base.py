from saneConf import SaneConf

def dprint(text):
    if SaneConf.debug:
        print(text)
    return