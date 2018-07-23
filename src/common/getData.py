'''
    getData.py

Executes the rules for gathing data as described in ruleConf.Config().

Concatenates the data onto a single line, and returns it for image creation.

Usage: GetData(Config).run()

If successful:
returns an string of data as described in instance of ruleConf.Config()

Lines are separated with '\n' and should be functional as command line argument
for imagemagick.  Lines will contain the headers specified in the config file.

Example output:
Uptime: up 3 days, 16:40\nUsername: brad\nHostname: pride.home\nTotal Memory: 8GB\n
Free Memory: \nIP Address: 192.168.1.4\nMAC Address: 60:f8:1d:c6:1d:da\n 02:f8:1d:c6:1d:da\n 
be:8e:08:46:f5:2d\n 72:00:07:d3:72:50\n 72:00:07:d3:72:51\n 72:00:07:d3:72:50\n
DNS Server: 192.168.1.1\n 192.168.1.5\n 8.8.8.8\n 71.10.216.1\nGateway: 192.168.1.1\n 
fe80::%utun0\nFree Space: /dev/disk1s1 34758 MB Available\n /dev/disk1s4 34758 MB Available\n 
/dev/disk0s3 6843 MB Available\nOS Version: Darwin 17.7.0 x86_64\n
Help Email: helpdesk@company.com\nHelp Phone: 999 777 999\n'

'''

import base
import externs

class GetData(base.baseClass):
    def __init__(self, config):
        self.conf = config
    
    def run(self):
        data = []
        flatdata = ""
        for rule in self.conf.rules:
            p = externs.shell(rule.rule)
            output = p.stdout.readlines()
            name = rule.name
            flatline = ""
            if isinstance(output, list):
                for line in output:
                    flatline += " " + line
                data.append(name + " " + flatline.strip())            
            else:
                output = name + " " + output
                data.append(output.strip())

        for line in data:
            flatdata += line + '\n'
        return flatdata
        