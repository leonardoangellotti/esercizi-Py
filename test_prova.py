import unittest
from lezione7 import somma, somma_err

class Testsomma(unittest.TestCase):

  def testsomma(self):
    self.assertEqual(somma(5,5), 10)
    self.assertEqual(somma_err(5,5),10)
    self.assertEqual(somma(5,5), 12)
    self.assertEqual(somma_err(5,6),12)