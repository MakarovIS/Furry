import unittest
from rev import revolut

class TestRevolution(unittest.TestCase):
    def test(self):
        self.assertEqual(revolut("1234"),"4321")

if __name__ == '__main__':
    unittest.main()
