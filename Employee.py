class Employee:

    def __init__(self, staffID, lastName, firstName, regHours, hourlyRate, oTMultiple, taxCredit, standardBand):
        self.staffId = staffID
        self.lastName = lastName
        self.firstName = firstName
        self.regHours = regHours
        self.hourlyRate = hourlyRate
        self.oTMultiple = oTMultiple
        self.taxCredit = taxCredit
        self.standardBand = standardBand


    def computePayment(self):
        return {}


    def getOverTimeHours(self, totalWorkHours):
        if(self.regHours > totalWorkHours):
            return 0
        return totalWorkHours - self.regHours


    def getOverTimeRate(self):
        return self.hourlyRate * self.oTMultiple


    def getRegularPay(self, totalWorkHours):
        if(self.regHours > totalWorkHours):
            return totalWorkHours * self.hourlyRate
        return self.regHours * self.hourlyRate

    def getOverTimePay(self, totalWorkHours):
        return self.getOverTimeRate() * self.getOverTimeHours(totalWorkHours)