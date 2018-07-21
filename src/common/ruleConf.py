from base import baseClass, dprint

class ConfigRule(baseClass):
    def __init__(self):
        self.name = ""
        self.rule = ""

class Config(baseClass):
    def __init__(self):
        self.header = ""
        self.rules = []
    
    def add(self, name, rule):
        newRule = ConfigRule()
        newRule.name = name
        newRule.rule = rule
        self.rules.append(newRule)

    def remove(self, name, all=False):
        for r in range(len(self.rules)):
            if self.rules[r].name == name:
                self.rules.remove(self.rules[r])
                if not all:
                    return
