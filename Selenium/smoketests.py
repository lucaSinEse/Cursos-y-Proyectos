from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from searchtests_1 import HomePageTest


assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_tests = TestLoader().loadTestsFromTestCase(HomePageTest)

#Construccion de suite de pruebas
smoke_test = TestSuite([assertions_test, search_tests])

#Respecto a los reportes

kwargs = {
    "output": 'smoke-report'
    }

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)