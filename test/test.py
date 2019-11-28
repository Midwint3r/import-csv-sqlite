import unittest
import sqlite3
from verifs import *


class test (unittest.TestCase):
    
    def test_file_exist(self):
        file_db = "tests/test.sqlite3"
        file_csv = "tests/test.csv"
        self.assertEqual(True, verif_file(file_db))
        self.assertEqual(True, verif_file(file_csv))

    def test_bdd_exist(self):
        path = "tests/test.sqlite3"
        table1 = "automobile"
        table2 = "voidtable"
        bdd=sqlite3.connect(path)
        self.assertEqual(True, veriftable(table1, bdd))
        self.assertEqual(False, veriftable(table2, bdd))
 
 
 
 
    




