#!/usr/bin/env python
from base import baseClass, dprint
from ruleConf import Config, ConfigRule
import saneConf

class ConfigParser(baseClass):
    def __init__(self, fileName):
        self.getSaneConfig()
        self.config = self.getConfig(fileName)

    def get(self):
        return self.config

    def getSaneConfig(self):
        f = open("conf/main.cfg")
        for line in f.readlines():
            line = line.rstrip()
            # discard comments and blank lines
            if line.startswith("#") or line.strip() == "":
                continue
            try:
                rule = line.split("=", 1)
                if rule[0] == "debug":
                    saneConf.debug = rule[1]
                elif rule[0] == "timer":
                    saneConf.debug = rule[1]
                elif rule[0] == "temp":
                    saneConf.temp = rule[1]
            except IndexError:
                continue

    def getConfig(self, configFileName):
        f = open(configFileName)
        conf = Config()
        for line in f.readlines():
            line = line.rstrip()
            # discard comments and blank lines
            if line.startswith("#") or line.strip() == "":
                continue
            
            if "HEADER=" in line:
                header = line.split("=")[1].strip()
                conf.header = header
            else:
                try:
                    rule = line.split(" X ", 1)
                    conf.add(rule[0], rule[1])
                except IndexError:
                    continue
        dprint(conf.header)
        dprint(conf.rules)
        f.close()
        return conf

