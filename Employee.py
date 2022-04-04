class Employee:

    employInfo = {}
    taxRates = {'standardRate': 20, 'higherRate': 40, 'PRSI': 4}

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
        self.employInfo['Date'] = date
        self.employInfo['Regular Hours Worked'] = self.regHours
        self.employInfo['Overtime Hours Worked'] = self.getOverTimeHours(totalWorkHours)
        self.employInfo['Regular Rate'] = self.hourlyRate
        self.employInfo['Overtime Rate'] = self.getOverTimeRate()
        self.employInfo['Regular Pay'] = self.getRegularPay(totalWorkHours)
        self.employInfo['Overtime Pay'] = self.getOverTimePay(self.employInfo['Overtime Hours Worked'])
        self.employInfo['Gross Pay'] = self.getGrossPay(self.employInfo['Regular Pay'], self.employInfo['Overtime Pay'])
        self.employInfo['Standard Rate Pay'] = self.getStandardRatePay(self.standardBand, self.employInfo['Gross Pay'])
        self.employInfo['Higher Rate Pay'] = self.getHigherRatePay(self.employInfo['Gross Pay'], self.employInfo['Standard Rate Pay'])
        self.employInfo['Standard Tax'] = self.getStandardTax(self.employInfo['Standard Rate Pay'])
        self.employInfo['Higher Tax'] = self.getHigherTax(self.employInfo['Higher Rate Pay'])
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


    def getGrossPay(self, regularPay, overTimePay):
        return regularPay + overTimePay


    def getHigherRatePay(self, grossPay, standardPay):
        if(grossPay < standardPay):
            return 0
        return grossPay - standardPay


    def getStandardRatePay(self, standardBand, grossPay):
        if(grossPay > standardBand):
            return standardBand
        return grossPay


    def getStandardTax(self, standardPay):
        return standardPay * self.taxRates['standardRate'] / 100


    def getHigherTax(self, higherPay):
        return higherPay * self.taxRates['higherRate'] / 100
