import unittest

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


    def test_validateOverTimeHours(self):
        employee = Employee('12345', 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        self.assertEqual(5, employee.getOverTimeHours(42))
        self.assertEqual(0, employee.getOverTimeHours(37))
        self.assertEqual(0, employee.getOverTimeHours(20))


if __name__ == '__main__':
    unittest.main()
