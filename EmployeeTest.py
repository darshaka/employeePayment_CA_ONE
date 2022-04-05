import unittest

from Employee import Employee

class EmployeeTest(unittest.TestCase):
    def test_employee1(self):
        employee = Employee('12345', 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        result = employee.computePayment(42, '31/10/2021')
        self.assertEqual('Joe Green', result['name'])
        self.assertEqual('31/10/2021', result['Date'])
        self.assertEqual(37, result['Regular Hours Worked'])
        self.assertEqual(5, result['Overtime Hours Worked'])
        self.assertEqual(16, result['Regular Rate'])
        self.assertEqual(24, result['Overtime Rate'])
        self.assertEqual(592, result['Regular Pay'])
        self.assertEqual(120, result['Overtime Pay'])
        self.assertEqual(712, result['Gross Pay'])
        self.assertEqual(710, result['Standard Rate Pay'])
        self.assertEqual(2, result['Higher Rate Pay'])
        self.assertEqual(142, result['Standard Tax'])
        self.assertEqual(0.8, result['Higher Tax'])
        self.assertEqual(142.8, result['Total Tax'])
        self.assertEqual(72, result['Tax Credit'])
        self.assertEqual(70.8, result['Net Tax'])
        self.assertEqual(28.48, result['PRSI'])
        self.assertEqual(99.28, result['Net Deductions'])
        self.assertEqual(612.72, result['Net Pay'])


    def test_employee2(self):
        employee = Employee('12345', 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        result = employee.computePayment(1, '31/10/2021')
        self.assertLessEqual(result['Net Pay'], result['Gross Pay'])


    def test_employee3(self):
        employee = Employee('12345', 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        result = employee.computePayment(0, '31/10/2021')
        self.assertLessEqual(result['Net Pay'], result['Gross Pay'])
        self.assertGreaterEqual(result['Overtime Hours Worked'], 0)
        self.assertGreaterEqual(result['Overtime Pay'], 0)
        self.assertGreaterEqual(result['Higher Tax'], 0)
        self.assertGreaterEqual(result['Net Pay'], 0)


    def test_employee4(self):
        employee = Employee('12345', 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        with self.assertRaises(ValueError):
            employee.computePayment(-1, '31/10/2021')


    def test_getName(self):
        employee = Employee('12345', 'One', 'Two', 37, 16, 1.5, 72, 710)
        result = employee.computePayment(42, '31/10/2021')
        self.assertEqual('Two One', result['name'])


if __name__ == '__main__':
    unittest.main()
