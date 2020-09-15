class Talking():
    def __init__(self,TalkCode,StartDate,EndDate,FromPhone,ToPhone):
        self.__TalkCode=TalkCode
        self.__StartDate=StartDate
        self.__EndDate=EndDate
        self.__FromPhone=FromPhone
        self.__ToPhone=ToPhone
    @property
    def TalkCode(self):
        return self.__TalkCode

    @TalkCode.setter
    def TalkCode(self, value):
           self.__TalkCode=value

    @property
    def StartDate(self):
        return self.__StartDate

    @StartDate.setter
    def StartDate(self, value):
           self.__StartDate=value

    @property
    def EndDate(self):
        return self.__EndDate

    @EndDate.setter
    def EndDate(self, value):
        self.__EndDate = value

    @property
    def FromPhone(self):
        return self.__FromPhone

    @FromPhone.setter
    def FromPhone(self, value):
        if(len(value)<=10):
            self.__FromPhone = value
    @property
    def ToPhone(self):
        return self.__ToPhone

    @ToPhone.setter
    def ToPhone(self, value):
        if(len(value)<=10):
            self.__ToPhone = value

    def __str__(self):
        return "TalkCode: " + str(self.TalkCode) + "  StartDate : " + str(self.StartDate) + "  EndDate: " + str(self.EndDate) + " FromPhone: " + str(self.FromPhone) + "  ToPhone: " + str(self.ToPhone)