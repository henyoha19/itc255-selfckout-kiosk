class Customer():
    def __init__(self, customerId, customerLname,customerFname,customerAddress):
        self.customerId=customerId
        self.customerLname=customerLname
        self.customerFname=customerFname
        self.customerAddress=customerAddress


    def getcustomerId(self):
        return self.customerId

    def getcustomerLname(self):
        return self.customerLname

    def getcustomerFname(self):
        return self.customerFname

    def getcustomerAddress(self):
        return self.customerAddress

    def __str__(self):
        return str(self.customerAddress) + " " + self.customerAddress
