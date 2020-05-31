import datetime

class Scanning():
    def __init__(self, scanningnum, scanningdate):
        self.scanningnum=scanningnum
        self.scanningdate=datetime.datetime.now()
       
    
    def getScanningnum(self):
        return self.scanningnum

    def getScanningdate(self):
        return self.scanningdate






