import unittest
from anagram import is_anagram


class TestIsAnagram(unittest.TestCase):

    def test_is_anagram(self):
        actual = is_anagram("abc", "bcd")
        expected = False
        self.assertEqual(expected, actual)

        actual = is_anagram("abcd", "bcda")
        expected = True
        self.assertEqual(expected, actual)

        actual = is_anagram("abc", "bcac")
        expected = False
        self.assertEqual(expected, actual)

        actual = is_anagram("abcd", "bac")
        expected = False
        self.assertEqual(expected, actual)

        actual = is_anagram("AbCd", "bcDA")
        expected = False
        self.assertEqual(expected, actual)

        actual = is_anagram("abcdefgh", "gefchabd")
        expected = True
        self.assertEqual(expected, actual)

        self.assertRaises(ValueError, is_anagram, "Some String", 1)
        self.assertRaises(ValueError, is_anagram, 100, 200)


if __name__ == "__main__":
    unittest.main()