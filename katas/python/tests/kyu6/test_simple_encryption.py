from unittest import TestCase
from katas.python.kyu6.simple_encryption import encrypt, decrypt


class TestSimpleEncryption(TestCase):
    def test_encrypt(self):
        self.assertEqual(encrypt("This is a test!", 0), "This is a test!")
        self.assertEqual(encrypt("This is a test!", 1), "hsi  etTi sats!")
        self.assertEqual(encrypt("This is a test!", 2), "s eT ashi tist!")
        self.assertEqual(encrypt("This is a test!", 3), " Tah itse sits!")
        self.assertEqual(encrypt("This is a test!", 4), "This is a test!")
        self.assertEqual(encrypt("This is a test!", -1), "This is a test!")
        self.assertEqual(encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")

    def test_decrypt(self):
        self.assertEqual(decrypt("This is a test!", 0), "This is a test!")
        self.assertEqual(decrypt("hsi  etTi sats!", 1), "This is a test!")
        self.assertEqual(decrypt("s eT ashi tist!", 2), "This is a test!")
        self.assertEqual(decrypt(" Tah itse sits!", 3), "This is a test!")
        self.assertEqual(decrypt("This is a test!", 4), "This is a test!")
        self.assertEqual(decrypt("This is a test!", -1), "This is a test!")
        self.assertEqual(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")

    def test_edge_cases(self):
        self.assertEqual(encrypt("", 0), "")
        self.assertEqual(decrypt("", 0), "")
        self.assertEqual(encrypt(None, 0), None)
        self.assertEqual(decrypt(None, 0), None)
