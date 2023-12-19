import unittest

def search_last_occurrence(pat, txt):
    last_index = txt.rfind(pat)  # Використовуємо метод rfind для пошуку останнього входження
    return last_index

class TestSearchLastOccurrence(unittest.TestCase):
    def test_last_occurrence(self):
        txt = "Hello World"
        pat = "World"
        index = search_last_occurrence(pat, txt)
        self.assertEqual(index, 6)  # Останнє входження підстрічки "World" у тексті "Hello World"

if __name__ == '__main__':
    unittest.main()
