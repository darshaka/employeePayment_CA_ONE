class Employee:

    employInfo = {}  # response dictionary
    taxRates = {'standardRate': 20, 'higherRate': 40, 'PRSI': 4}  # tax and PRSI values

    def __init__(self, staffID, lastName, firstName, regHours, hourlyRate, oTMultiple, taxCredit, standardBand):
        self.staffId = staffID
        self.lastName = lastName
        self.firstName = firstName
        self.regHours = regHours
        self.hourlyRate = hourlyRate
        self.oTMultiple = oTMultiple
        self.taxCredit = taxCredit
        self.standardBand = standardBand


    """
        computePayment is a public method and it required totalWorkHours (int) and the date (string)
        
        Validation: this validate the totalWorkHours. totalWorkHours is less than 0, then it will throw a ValueError
    """
    def computePayment(self, totalWorkHours, date):
        if(totalWorkHours < 0) :
            raise ValueError('Invalid workHours count')

        self.employInfo['name'] = self.__getName()
        self.employInfo['Date'] = date
        self.employInfo['Regular Hours Worked'] = self.regHours
        self.employInfo['Overtime Hours Worked'] = self.__getOverTimeHours(totalWorkHours)
        self.employInfo['Regular Rate'] = self.hourlyRate
        self.employInfo['Overtime Rate'] = self.__getOverTimeRate()
        self.employInfo['Regular Pay'] = self.__getRegularPay(totalWorkHours)
        self.employInfo['Overtime Pay'] = self.__getOverTimePay(self.employInfo['Overtime Hours Worked'])
        self.employInfo['Gross Pay'] = self.__getGrossPay(self.employInfo['Regular Pay'], self.employInfo['Overtime Pay'])
        self.employInfo['Standard Rate Pay'] = self.__getStandardRatePay(self.standardBand, self.employInfo['Gross Pay'])
        self.employInfo['Higher Rate Pay'] = self.__getHigherRatePay(self.employInfo['Gross Pay'], self.employInfo['Standard Rate Pay'])
        self.employInfo['Standard Tax'] = self.__getStandardTax(self.employInfo['Standard Rate Pay'])
        self.employInfo['Higher Tax'] = self.__getHigherTax(self.employInfo['Higher Rate Pay'])
        self.employInfo['Total Tax'] = self.__getTotalTax(self.employInfo['Standard Tax'], self.employInfo['Higher Tax'])
        self.employInfo['Tax Credit'] = self.taxCredit
        self.employInfo['Net Tax'] = self.__getNetTax(self.employInfo['Total Tax'], self.employInfo['Tax Credit'])
        self.employInfo['PRSI'] = self.__getPRSI(self.employInfo['Gross Pay'])
        self.employInfo['Net Deductions'] = self.__getNetDeductions(self.employInfo['Net Tax'], self.employInfo['PRSI'])
        self.employInfo['Net Pay'] = self.__getNetPay(self.employInfo['Gross Pay'], self.employInfo['Net Deductions'])
        return self.employInfo

    """
        Get the name with combining the first and last name
        return: name, if cannot find at least one name this will return AssertionError
    """
    def __getName(self):
        if (self.firstName != None and self.lastName != None):
            return (self.firstName + " " + self.lastName)
        elif (self.firstName != None):
            return self.firstName
        elif(self.lastName != None):
            return self.lastName
        else:
            raise AssertionError('Both names cannot be null')


    """
        Calculate over time hours
        Note: This method, never return negative values
    """
    def __getOverTimeHours(self, totalWorkHours):
        if(self.regHours > totalWorkHours):
            return 0
        return totalWorkHours - self.regHours


    """
        Calculate over time rate
    """
    def __getOverTimeRate(self):
        if (self.hourlyRate >= 0 and self.oTMultiple >= 1):
            return self.hourlyRate * self.oTMultiple
        raise ValueError('Invalid over time rate')


    """
        Calculate regular pay mount.
    """
    def __getRegularPay(self, totalWorkHours):
        if(self.regHours > totalWorkHours):
            return totalWorkHours * self.hourlyRate
        return self.regHours * self.hourlyRate


    """
        Calculate over time pay
    """
    def __getOverTimePay(self, overTimeHours):
        return self.__getOverTimeRate() * overTimeHours


    """
        Calculate gross pay
    """
    def __getGrossPay(self, regularPay, overTimePay):
        return regularPay + overTimePay


    """
        Calculate higher rate pay
        Note: never return negative amount
    """
    def __getHigherRatePay(self, grossPay, standardPay):
        if(grossPay < standardPay):
            return 0
        return grossPay - standardPay


    #  Calculate standard rate pay
    def __getStandardRatePay(self, standardBand, grossPay):
        if(grossPay > standardBand):
            return standardBand
        return grossPay

    #  Calculate standard tax
    def __getStandardTax(self, standardPay):
        return standardPay * self.taxRates['standardRate'] / 100


    #  Calculate higher tax
    def __getHigherTax(self, higherPay):
        return higherPay * self.taxRates['higherRate'] / 100


    #  Calculate total tax
    def __getTotalTax(self, standardTax, higherTax):
        return standardTax + higherTax


    #  Calculate net tax
    def __getNetTax(self, taxTotal, taxCredit):
        netTax = float(f'{(taxTotal - taxCredit):g}')
        if(netTax < 0):
            return 0
        return netTax


    #  Calculate the PRSI
    def __getPRSI(self, grossPay):
        return grossPay * self.taxRates['PRSI'] / 100


    #  Calculate the net deductions
    def __getNetDeductions(self, netTax, pRSI):
        return netTax + pRSI


    #  Calculate the net pay
    def __getNetPay(self, grossPay, netDecution):
        return grossPay - netDecution