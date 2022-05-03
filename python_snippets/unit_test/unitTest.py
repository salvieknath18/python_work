import unittest


class TestMyprogram(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('FOO', 'FOO')
        print('hello')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        print('hello')

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(" ")
            print('hello')

if __name__ == '__main__':
    unittest.main()
