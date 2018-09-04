import anagram
import unittest


class TestAnagram(unittest.TestCase):
    def test_anagram_single_character(self):
        expected_result = ["a"]
        self.assertEqual(expected_result, anagram.find_all("a"))

    def test_anagram_two_different_characters(self):
        result = anagram.find_all("ab")
        self.assertEqual(2, len(result))
        self.assertTrue("ab" in result)
        self.assertTrue("ba" in result)

    # def test_anagram_three_different_characters(self):
    #     result = anagram.find_all("abc")
    #     self.assertEqual(6, len(result))
    #     expected_results = [ "abc", "acb", "bac", "bca", "cab", "cba"]
    #     [self.assertTrue(word in result) for word in expected_results]

    def test_recurse_one_character(self):
        result = anagram.recurse_append_anagrams("a", "")
        self.assertEqual(1, len(result))
        self.assertTrue("a" in result)

    # def test_recurse_two_different_characters(self):
    #     result = anagram.recurse_append_anagrams("a", "b")
    #     self.assertEqual(1, len(result))
    #     self.assertTrue("ab" in result)

    # def test_recurse_two_remaining_characters(self):
    #     result = anagram.recurse_append_anagrams("a", "bc")
    #     self.assertEqual(2, len(result))
    #     self.assertTrue("abc" in result)
    #     self.assertTrue("acb" in result)
