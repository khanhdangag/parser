import unittest 
import lexer as lex
import sys
import warnings
import os
import io 

#Test lexer
class LexTests(unittest.TestCase):
    def setUp(self):
        sys.stderr = io.StringIO()
        sys.stdout = io.StringIO()
        if sys.hexversion >= 0x3020000:
            warnings.filterwarnings('ignore',category=ResourceWarning)