import unittest
from src.utils import csvToList


class TestCSV(unittest.TestCase):
    def test_csv_profile_target(self):
        links = csvToList('assets/profile_target.csv')
        print(links)
        self.assertTrue(links)


if __name__ == "__main__":
    unittest.main()
