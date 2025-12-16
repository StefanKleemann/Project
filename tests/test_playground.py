import unittest
from playground import Playground

class TestPlayground(unittest.TestCase):
    def test_add(self):
        pg = Playground()
        self.assertEqual(pg.add(1,2),3)


if __name__ == '__main__':
    unittest.main()
