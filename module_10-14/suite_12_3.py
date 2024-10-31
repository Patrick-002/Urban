import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создаем тестовый набор
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(RunnerTest))
suite.addTest(unittest.makeSuite(TournamentTest))

# Создаем тестовый прогон
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
