import sqlite3
import logging
import csv
import sys
import os
from datetime import datetime



path_csv=("./data.csv")
path_db=("./batabase.sqlite3")
path_log=("./logs.log")

def verifcsv(fichier_csv):   
    if not os.path.exists(fichier_csv):
        logging.debug("Fichier CSV inexistant, fermeture du programme")
        print("Erreur, le fichier CSV nommé ""%s"" inexistant, verifiez le repertoire courant "% fichier_csv)
        exit(1)
    else:
        logging.debug("Fichier CSV valide")


def verifdb(fichier_sqlite):
    if not os.path.exists(fichier_sqlite):
        logging.debug("La base de sonnées %s n'existe pas, création d'une nouvelle base de données" % fichier_sqlite)
    else:
        logging.debug("Fichier de base de données deja existant, fermeture du programme")
        print("Erreur, le fichier portant le nom ""%s"" existe deja "% fichier_sqlite)
        exit(1)
        
        

def veriflog(fichier_log):
    if os.path.exists(fichier_log):
        logging.debug("le fichier de log deja existant")
    else:
        logging.debug("le fichier de log n'existe pas, creation de celui ci")


logging.debug("Creating table")
def createtab(cursor):
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


def insertion_bdd(cursor,path_csv):
    with open(path_csv) as csvfile:
        lecteur = csv.DictReader(csvfile, delimiter=';')
        to_db =         [(row['adresse_titulaire'],row['nom'],row['prenom'],row['immatriculation'],row['date_immatriculation'],row['vin'] ,row['marque'] ,row['denomination_commerciale'] ,row['couleur'] ,row['carroserie'],row['categorie'] ,row['cylindree'] ,row['energie'] ,row['places'],row['poids'],row['puissance'],row['type'] ,row['variante'] ,row['version'] ) for row in lecteur]
    cursor.executemany("INSERT INTO automobile (adresse_titulaire,nom,prenom,immatriculation,date_immatriculation,vin,marque,denomination_commerciale,couleur,carroserie,categorie,cylindree,energie,places,poids,puissance,type,variante,version) VALUES (?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", to_db)




logging.basicConfig(format ='%(asctime)s : %(levelname)s : import.py : %(message)s',filename='logs.log',level=logging.DEBUG) #configuration du module logging
logging.debug("Debut programme")


if __name__ =='__main__':


    
    verifcsv(path_csv)
    verifdb(path_db)
    veriflog(path_log)
    
    logging.debug("Connection a la base de données")
    connection=sqlite3.connect(path_db)
    cursor=connection.cursor()
    
    createtab(cursor)
    insertion_bdd(cursor,path_csv)
    
    



connection.commit()
cursor.close()
 


