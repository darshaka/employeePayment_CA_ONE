import unittest
import decimal
from decimal import Decimal

from Employee import Employee

class EmployeeTest(unittest.TestCase):
    def test_employee(self):
        employee = Employee('12345', 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        self.assertEqual('12345', employee.staffId)
        self.assertEqual('Green', employee.lastName)
        self.assertEqual('Joe', employee.firstName)
        self.assertEqual(37, employee.regHours)
        self.assertEqual(16, employee.hourlyRate)
        self.assertEqual(1.5, employee.oTMultiple)
        self.assertEqual(72, employee.taxCredit)
        self.assertEqual(710, employee.standardBand)


    def test_getName(self):
        employee = Employee('12345', 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        result = employee.computePayment(42, '31/10/2021')
        self.assertEqual('Joe Green', result['name'])


    def test_validateOverTimeHours(self):
        employee = Employee('12345', 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        self.assertEqual(5, employee.getOverTimeHours(42))
        self.assertEqual(0, employee.getOverTimeHours(37))
        self.assertEqual(0, employee.getOverTimeHours(20))


    def test_calculateOverTimeRate(self):
        employee1 = Employee('12345', 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        self.assertEqual(24, employee1.getOverTimeRate())

        employee2 = Employee('12345', 'Green', 'Joe', 37, 21, 1.5, 72, 710)
        self.assertEqual(31.5, employee2.getOverTimeRate())


    def test_calculateRegularPay(self):
        employee = Employee('12345', 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        self.assertEqual(592, employee.getRegularPay(42))
        self.assertEqual(592, employee.getRegularPay(37))
        self.assertEqual(432, employee.getRegularPay(27))


    def test_calculateOverTimePay(self):
        employee = Employee('12345', 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        self.assertEqual(120, employee.getOverTimePay(5))
        self.assertEqual(0, employee.getOverTimePay(0))


    def test_calculateGrossPay(self):
        employee = Employee('12345', 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        self.assertEqual(20, employee.getGrossPay(15, 5))


    def test_calculateHigherRatePay(self):
        employee = Employee('12345', 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        self.assertEqual(10, employee.getHigherRatePay(720, 710))
        self.assertEqual(0, employee.getHigherRatePay(700, 710))


    def test_calculateStandardTax(self):
        employee = Employee('12345', 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        self.assertEqual(100, employee.getStandardTax(500))


    def test_calculateHigherTax(self):
        employee = Employee('12345', 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        self.assertEqual(.8, employee.getHigherTax(2))


    def test_calculateTotalTax(self):
        employee = Employee('12345', 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        self.assertEqual(142.8, employee.getTotalTax(142, .8))


    def test_calculateNetTax(self):
        employee = Employee('12345', 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        self.assertEqual(float(f'{70.8:g}'), employee.getNetTax(142.8, 72))


    def test_calculatePRSI(self):
        employee = Employee('12345', 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        self.assertEqual(28.48, employee.getPRSI(712))


    def test_netDeduction(self):
        employee = Employee('12345', 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        self.assertEqual(99.28, employee.getNetDeductions(70.8, 28.48))


    def test_calculateNetPay(self):
        employee = Employee('12345', 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        self.assertEqual(612.72, employee.getNetPay(712, 99.28))


if __name__ == '__main__':
    unittest.main()
