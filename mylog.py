import ConfigParser
import time
import os

class mylog:
    def __init__(self):
        self.cf = ConfigParser.ConfigParser()
        self.cwd = os.getcwd()
        self.cf.read(self.cwd+"/config.conf")
        self.log_path = self.cf.get('log','path')
        file_name = time.strftime("%Y%m%d",time.localtime())
        self.log = open(self.log_path + "/log/" + file_name + ".log","a")

    def fwrite(self,msg):
        curTime = time.strftime('%Y-%m-%d %H:%M:%S')
        self.log.write(curTime+"\t"+str(msg)+"\n")

