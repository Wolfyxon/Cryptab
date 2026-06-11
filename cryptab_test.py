import unittest
import cryptab

class CryptabTest(unittest.TestCase):
    def test_encrypt_decrypt(self):
        text = "AlaMaKota"
        keys = {
            "A": 2,
            "B": 30,
            "C": 100
        }

        encrypted = cryptab.encrypt(text, keys)
        decrypted = cryptab.decrypt(encrypted, keys)

        assert text == decrypted, f"Decrypted text doesn't match original. Got: {decrypted}"

    def test_is_letter(self):
        assert cryptab.is_letter("a")
        assert cryptab.is_letter("B")
        assert not cryptab.is_letter("?")
        assert not cryptab.is_letter("1")

    def test_random_letter(self):
        for _ in range(10):
            a = cryptab.get_random_letter()
            assert cryptab.is_letter(a)

if __name__ == "__main__":
    unittest.main()
