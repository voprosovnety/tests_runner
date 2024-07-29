import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = runner.Runner('John')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        obj_runner = runner.Runner('Steve')
        for i in range(10):
            obj_runner.run()
        self.assertEqual(obj_runner.distance, 100)

    def test_challenge(self):
        obj_runner_1 = runner.Runner('Max')
        obj_runner_2 = runner.Runner('Paul')
        for i in range(10):
            obj_runner_2.walk()
            obj_runner_1.run()
        self.assertNotEqual(obj_runner_1.distance, obj_runner_2.distance)
