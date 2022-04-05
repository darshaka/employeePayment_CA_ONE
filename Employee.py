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
        if(totalWorkHours < 0) :
            raise ValueError('Invalid workHours count')

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
        self.employInfo['Total Tax'] = self.getTotalTax(self.employInfo['Standard Tax'], self.employInfo['Higher Tax'])
        self.employInfo['Tax Credit'] = self.taxCredit
        self.employInfo['Net Tax'] = self.getNetTax(self.employInfo['Total Tax'], self.employInfo['Tax Credit'])
        self.employInfo['PRSI'] = self.getPRSI(self.employInfo['Gross Pay'])
        self.employInfo['Net Deductions'] = self.getNetDeductions(self.employInfo['Net Tax'], self.employInfo['PRSI'])
        self.employInfo['Net Pay'] = self.getNetPay(self.employInfo['Gross Pay'], self.employInfo['Net Deductions'])
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


    def getTotalTax(self, standardTax, higherTax):
        return standardTax + higherTax


    def getNetTax(self, taxTotal, taxCredit):
        netTax = float(f'{(taxTotal - taxCredit):g}')
        if(netTax < 0):
            return 0
        return netTax


    def getPRSI(self, grossPay):
        return grossPay * self.taxRates['PRSI'] / 100


    def getNetDeductions(self, netTax, pRSI):
        return netTax + pRSI


    def getNetPay(self, grossPay, netDecution):
        return grossPay - netDecution