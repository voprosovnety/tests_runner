import tests_12_3
import unittest

tests=unittest.TestSuite()
tests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
tests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

tests_runner=unittest.TextTestRunner(verbosity=2)
tests_runner.run(tests)