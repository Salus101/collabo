# test_main.py
from main import main
import unittest

class TestMain(unittest.TestCase):

    def test_main(self):
        self.assertEqual(main(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
