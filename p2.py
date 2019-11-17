import sqlite3
import logging
import csv
import sys
import os.path
import os

logging.basicConfig(format ='%(asctime)s : %(levelname)s : import.py : %(message)s',level=logging.DEBUG) #configuration du module logging
logging.debug("Debut programme")
path_csv=("./data.csv")
path_db=("./batabase.sqlite3")
path_log=("./logs.log")

if not os.path.exists(path_csv):
        raise Exception("%s doesn't exist" % path_csv)

if not os.path.exists(path_db):
        logging.debug("La base de sonnées %s n'existe pas, dréation d'une nouvelle base de données" % path_db)
  
logging.debug("Connection a la base de données")
connection=sqlite3.connect(path_db)

cursor=connection.cursor()

logging.debug("Creating table")

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
        carroserie text,
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
connection.commit()



with open(path_csv) as csvfile:
    lecteur = csv.DictReader(csvfile, delimiter=';')
    to_db = [(row['adresse_titulaire'],row['nom'],row['prenom'],row['immatriculation'],row['date_immatriculation'],row['vin'] ,row['marque'] ,row['denomination_commerciale'] ,row['couleur'] ,row['carroserie'],row['categorie'] ,row['cylindree'] ,row['energie'] ,row['places'],row['poids'],row['puissance'],row['type'] ,row['variante'] ,row['version'] ) for row in lecteur]
    
cursor.executemany("INSERT INTO automobile (adresse_titulaire,nom,prenom,immatriculation,date_immatriculation,vin,marque,denomination_commerciale,couleur,carroserie,categorie,cylindree,energie,places,poids,puissance,type,variante,version) VALUES (?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", to_db)


connection.commit()
cursor.close()
 


