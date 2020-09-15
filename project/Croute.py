class Croute():
    def __init__(self , CrouteCode, WaysName ,Cost,MinuteHere,MinuteAbroad):
        self.__CrouteCode=CrouteCode
        self.__WaysName=WaysName
        self.__Cost=Cost
        self.__MinuteHere=MinuteHere
        self.__MinuteAbroad=MinuteAbroad


    @property
    def CrouteCode(self):
        return self.__CrouteCode

    @CrouteCode.setter
    def CrouteCode(self, value):
           self.__CrouteCode=value

    @property
    def WaysName(self):
        return self.__WaysName

    @WaysName.setter
    def WaysName(self, value):
            self.WaysName = value
    @property
    def Cost(self):
        return self.__Cost

    @Cost.setter
    def Cost(self, value):
            self.__Cost = value

    @property
    def MinuteHere(self):
        return self.__MinuteHere

    @MinuteHere.setter
    def MinuteHere(self, value):
            self.__MinuteHere = value

    @property
    def MinuteAbroad(self):
        return self.__MinuteAbroad

    @MinuteAbroad.setter
    def MinuteAbroad(self, value):
            self.__MinuteAbroad = value
    def __str__(self):
        return "CrouteCode: "+str(self.CrouteCode)+" WaysName: "+self.WaysName+" Cost: "+str(self.Cost) +" MinuteHere: "+str(self.MinuteHere)+" MinuteAbroad: "+str(self.MinuteAbroad)
