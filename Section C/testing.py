import unittest
from isbn_solution import isbn13


class TestSum(unittest.TestCase):

    def test_isbn13(self):
        self.assertIn(isbn13("9780316066525"), "Valid")
        self.assertIn(isbn13("9780330101820"), "Valid")
        self.assertIn(isbn13("9783161484100"), "Valid")
        self.assertIn(isbn13("9780936385112"), "Valid")
        self.assertIn(isbn13("9781847154569"), "Valid")
        self.assertIn(isbn13("033010182X"), "9780330101820")
        self.assertIn(isbn13("0205080057"), "9780205080052")
        self.assertIn(isbn13("1861972717"), "9781861972712")
        self.assertIn(isbn13("0198526636"), "9780198526636")
        self.assertIn(isbn13("8175257660"), "9788175257665")
        self.assertIn(isbn13("031293033X"), "9780312930332")
        self.assertIn(isbn13("978183715456Y"), "Invalid")
        self.assertIn(isbn13("978186715497X"), "Invalid")
        self.assertIn(isbn13("978184P1545Z9"), "Invalid")
        self.assertIn(isbn13("ZZZZZZ"), "Invalid")
        self.assertIn(isbn13("1235468546235"), "Invalid")
        self.assertIn(isbn13("5241683002"), "Invalid")
        self.assertIn(isbn13("9653214058"), "Invalid")
        self.assertIn(isbn13("64511826X9"), "Invalid")


if __name__ == '__main__':
    unittest.main()
