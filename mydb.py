import sys
import os
from mylog import mylog
from pornhub import pornhub

class mydb:
    def __init__(self,section):
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(self.cwd+"/config.conf")
        conf = self.getConf(section) 
        self.db = MySQLdb.connect(host=conf[0],port=int(conf[1]),user=conf[2],passwd=conf[3],db=conf[4],charset="utf8") 

    def getConfig(self,section):
        return (cf.get(section,'host'), \
                cf.get(section,'port'), \
                cf.get(section,'user'), \
                cf.get(section,'passwd'), \
                cf.get(section,'db'))


    def close():
        self.db.close())

