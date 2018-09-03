import anagram
import unittest


class TestAnagram(unittest.TestCase):
    def test_anagram_single_character(self):
        self.assertEqual("a", anagram.find_all("a"))
