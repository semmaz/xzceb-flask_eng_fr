import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench(None), "")

    def test2(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

    def test3(self):
        self.assertNotEqual(englishToFrench("Hello"), "Hello")


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish(None), "")

    def test2(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

    def test3(self):
        self.assertNotEqual(frenchToEnglish("Bonjour"), "Bonjour")

unittest.main()
