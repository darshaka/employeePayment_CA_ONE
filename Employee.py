class Employee:

    employInfo = {}

    def __init__(self, staffID, lastName, firstName, regHours, hourlyRate, oTMultiple, taxCredit, standardBand):
        self.staffId = staffID
        self.lastName = lastName
        self.firstName = firstName
        self.regHours = regHours
        self.hourlyRate = hourlyRate
        self.oTMultiple = oTMultiple
        self.taxCredit = taxCredit
        self.standardBand = standardBand


    def computePayment(self, totalWorkHours, date):
        self.employInfo['name'] = self.getName()
        self.employInfo['date'] = date
        self.employInfo['Regular Hours Worked'] = self.regHours
        self.employInfo['Overtime Hours Worked'] = self.getOverTimeHours(totalWorkHours)
        self.employInfo['Regular Rate'] = self.hourlyRate
        self.employInfo['Overtime Rate'] = self.getOverTimeRate()
        self.employInfo['Regular Pay'] = self.getRegularPay(totalWorkHours)
        self.employInfo['Overtime Pay'] = self.getOverTimePay(self.employInfo['Overtime Hours Worked'])
        return self.employInfo


    def getName(self):
        return self.firstName + " " + self.lastName


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

    def getOverTimePay(self, overTimeHours):
        return self.getOverTimeRate() * overTimeHours