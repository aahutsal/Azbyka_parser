import unittest

class TestStringMethods(unittest.TestCase):

  def test_title_type(self):
      self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()