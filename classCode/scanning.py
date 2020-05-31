import datetime

class Scanning():
    def __init__(self, scanningnum, scanningdate):
        self.scanningnum=scanningnum
        self.scanningdate=datetime.datetime.now()
       
    
    def getscanningnum(self):
        return self.scanningnum

    def getScandate(self):
        return self.scanningdate

    def __str__(self):
        return self.




