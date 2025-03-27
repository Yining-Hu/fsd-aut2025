import os
import sys

class Controller:
    
    @staticmethod
    def filepath():
        scriptpath = os.path.abspath(sys.argv[0])
        scriptdir = os.path.dirname(scriptpath)
        return scriptdir+"\\"
    
    @staticmethod
    def save(user):
        path = Controller.filepath()
        handler = open(path+"log.txt","a")
        handler.write(str(user))
        handler.write("\n")
        handler.close()
        
    @staticmethod
    def read():
        path = Controller.filepath()
        handler = open(path+"log.txt","r")
        data = handler.readlines()
        lines = []
        for line in data:
            if not(line.isspace()):
                filtered = line.replace('\n','')
                lines.append(filtered)
        return lines
    
 
    