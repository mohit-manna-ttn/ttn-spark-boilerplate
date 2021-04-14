import unittest
from jobs.reconciliation import say_hello
from dependencies.spark import start_spark
#python -m unittest tests/test_*.py
class SparkReconciliationTests(unittest.TestCase):
    def setUp(self):
        self.spark,self.log,self.config=start_spark()
    def tearDown(self):
        self.spark.stop()

    def test_say_hello(self):
        self.assertTrue(say_hello(self.spark))


if __name__ == '__main__':
    unittest.main()