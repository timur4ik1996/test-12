from unittest import runner

import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        one = runner.Runner(name = "R1")
        for i in range(10):
            one.walk()
        self.assertEqual(one.distance, 50)

    def test_run(self):
        two = runner.Runner(name ="R2")
        for i in range(10):
            two.run()
        self.assertEqual(two.distance, 100)

    def test_chellenge(self):
        three = runner.Runner(name="R3")
        four = runner.Runner(name="R4")
        for i in range(10):
            three.walk()
            four.run()
        self.assertNotEquals(three.distance, four.distance)


if __name__ == "__mail__":
    unittest.main()
