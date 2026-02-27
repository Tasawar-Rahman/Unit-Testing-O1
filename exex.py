import unittest
import pie
class Teststr(unittest.TestCase):
    def test_count(self):
        self.assertEqual(pie.count("hello world"), 2)
        self.assertEqual(pie.count("nothing"), 1)
        self.assertEqual(pie.count("minus three minus three"), 4)
    def test_vowels(self):
        self.assertEqual(pie.vowels("hello world"), 3)
        self.assertEqual(pie.vowels("foolish"), 3)
        self.assertEqual(pie.vowels("paragraph"), 3)
    def test_reverse(self):
        self.assertEqual(pie.reverse("hello world"), "dlrow olleh")
        self.assertEqual(pie.reverse("minus three"), "eerht sunim")
        self.assertEqual(pie.reverse("noteboos"), "soobeton")
    
if __name__=="__main__":
    unittest.main()

