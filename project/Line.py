class Line():
    def __init__(self,LineCode,CustomerCode,RouteCode,Phone):
        self.__LineCode=LineCode
        self.__CustomerCode=CustomerCode
        self.__RouteCode=RouteCode
        self.__Phone=Phone
    @property
    def LineCode(self):
        return self.__LineCode

    @LineCode.setter
    def LineCode(self, value):
           self.__LineCode=value

    @property
    def CustomerCode(self):
        return self.__CustomerCode

    @CustomerCode.setter
    def CustomerCode(self, value):
           self.__CustomerCode=value

    @property
    def RouteCode(self):
        return self.__RouteCode

    @RouteCode.setter
    def RouteCode(self, value):
        self.__RouteCode = value

    @property
    def Phone(self):
        return self.__Phone

    @Phone.setter
    def Phone(self, value):
        if(len(value)<=10):
            self.__Phone = value

    def __str__(self):
        return "LineCode: "+str(self.LineCode)+" CustomerCode: "+str(self.CustomerCode)+" RouteCode: "+str(self.RouteCode)+" Phone: "+self.Phone