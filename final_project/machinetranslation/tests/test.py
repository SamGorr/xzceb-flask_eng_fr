import unittest

from translator import *

class Testf2e(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish(None), None)

    def test2(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') 

class Teste2f(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench(None), None) 

    def test2(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') 


if  __name__ == '__main__':
    unittest.main()