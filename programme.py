import sqlite3
import csv
import logging
import sys

#chemin des documents externes
path_csv=("./data.csv")
path_bdd=("./mybase.sqlite3")
path_log=("./logs.log")

connection=sqlite3.connect(path_bdd)
logging.basicConfig(filename=path_log,level=logging.INFO)
cursor=connection.cursor()
#creation table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS automobile(
        adresse_titulaire text,
        nom text,
        prenom text,
        immatriculation text,
        date_immatriculation text,
        vin text,                    
        marque text,
        denomination_commerciale text,
        couleur text,
        carosserie text,
        categorie text,
        cylindree int,
        energie int, 
        places int,
        poids int,
        puissance int,
        type text,
        variante text,
        version int
    );
''')
path_csv.encode('utf-8')
connection.commit()


with open(path_csv,newline='') as csvfile:
    lecteur = csv.DictReader(csvfile, delimiter=';')
    for line_content in lecteur:
        cursor.execute("SELECT * FROM automobile",line_content)
        cursor.executemany("INSERT INTO automobile VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);",line_content)
        connection.commit()
        
connection.close()
    
        
        #(adresse_titulaire,nom,prenom,immatriculation,date_immatriculation,vin,marque,denomination_commerciale,couleur,carosserie,categorie,cylindree,energie,places,poids,puissance,type,variante,version)




