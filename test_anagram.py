import anagram
import unittest


class TestAnagram(unittest.TestCase):
    def test_anagram_single_character(self):
        result = ["a"]
        self.assertEqual(result, anagram.find_all("a"))

    # def test_anagram_two_different_characters(self):
    #     self.assertEqual("ab", anagram.find_all("ab"))
