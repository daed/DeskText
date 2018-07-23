'''
    test.py

TODO: Need more unittesting

'''

import unittest
import externs
from configParser import ConfigParser
from ruleConf import Config, ConfigRule
import saneConf
import subprocess



class TestExterns(unittest.TestCase):
    def test_popen(self):
        p = externs.labelAndComposite("test.jpg", "blah.txt", "+10", "+50", "output.jpg")
        self.assertTrue(isinstance(p, subprocess.Popen))

        p = externs.shell("ps -ef | grep python")
        out = p.stdout.readlines()
        self.assertTrue(isinstance(p, subprocess.Popen))
    
class TestConfig(unittest.TestCase):
    def setUp(self):
        # Creating the test config by hand for comparison.
        self.goodConf = Config()
        self.goodConf.add('Uptime:', 'uptime | awk \'{print $2 " " $3 " " $4 " " $5}\' | cut -d "," -f1-2')
        self.goodConf.add('Version:', 'echo $BGVERSION')
        self.goodConf.add('Username:', 'echo $USER X TESTING ANOTHER X')
        self.goodConf.add('bad rule', 'echo this is borken')
        self.goodConf.remove('bad rule')

    def test_config_header(self):
        config = ConfigParser("conf/client/test.cfg").get()
        self.assertEqual("Test Header", config.header)

    def test_config_rules(self):
        config = ConfigParser("conf/client/test.cfg").get()
        for x in range(len(config.rules)):
            self.assertEqual(config.rules[x].name, self.goodConf.rules[x].name)
            self.assertEqual(config.rules[x].rule, self.goodConf.rules[x].rule)
        

if __name__ == "__main__":
    unittest.main()