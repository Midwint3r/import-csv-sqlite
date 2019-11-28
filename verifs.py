import sqlite3
import logging
import csv
import os

def verif_file(file_name):
    if not os.path.exists(file_name):
        res=False
    else:
        res=True
    return res


def veriftable(nom_table, path_bdd):
    res = False
    cursor = path_bdd.cursor()
    cursor.execute('''SELECT name FROM sqlite_master''')
    path_bdd.commit()
    data = cursor.fetchall()
    for result in data:
        for details in result:
            if details == nom_table:
                res = True
    return res  
