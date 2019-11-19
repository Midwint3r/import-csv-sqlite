import sqlite3
import logging
import csv
import os



path_csv=("./data.csv")
path_db=("./database.sqlite3")
path_log=("./logs.log")

def verifcsv(fichier_csv):   
    if not os.path.exists(fichier_csv):
        logging.error('Fichier CSV inexistant, fermeture du programme')
        exit(1)
    else:
        logging.debug('Fichier CSV valide')


def verifdb(fichier_sqlite):
    if not os.path.exists(fichier_sqlite):
        logging.debug('La base de données %s est inexistante, création d''une nouvelle base de données' % fichier_sqlite)
    else:
        logging.debug('Base de données deja existant, Mise à jour de celle-ci')
        

def veriflog(fichier_log):
    if os.path.exists(fichier_log):
        logging.debug('le fichier de log deja existant')
    else:
        logging.debug('le fichier de log inexistant, creation de celui-ci')

   
def createtab(cursor):
    logging.info("Creation de la table") 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS automobile(
            adresse_titulaire text,
            nom text,
            prenom text,
            immatriculation text,
            date_immatriculation text,
            vin int,                    
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
            )
        ''')
    connection.commit()


def insertion_bdd(cursor,path_csv):
    with open(path_csv) as csvfile:
        lecteur = csv.DictReader(csvfile, delimiter=';')
        import_db =         [(row['adresse_titulaire'],row['nom'],row['prenom'],row['immatriculation'],row['date_immatriculation'],row['vin'] ,row['marque'] ,row['denomination_commerciale'] ,row['couleur'] ,row['carroserie'],row['categorie'] ,row['cylindree'] ,row['energie'] ,row['places'],row['poids'],row['puissance'],row['type'] ,row['variante'] ,row['version'] ) for row in lecteur]
    insert = False
    try:
        cursor.executemany("INSERT INTO automobile (adresse_titulaire,nom,prenom,immatriculation,date_immatriculation,vin,marque,denomination_commerciale,couleur,carroserie,categorie,cylindree,energie,places,poids,puissance,type,variante,version) VALUES (?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", import_db)
        insert = True
    finally:
        if insert == False:
            cursor.executemany("UPDATE automobile SET adresse_titulaire = ?,nom = ?,prenom = ?,immatriculation = ?,date_immatriculation = ?,vin = ?,marque = ?,denomination_commerciale = ?,couleur = ?,carroserie = ?,categorie = ?,cylindree = ?,energie = ?,places = ?,poids = ?,puissance = ?,type = ?,variante = ?,version = ? WHERE immatriculation = ?", import_db)
    







if __name__ =='__main__':
    
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='logs.log', level=logging.DEBUG)
    logging.debug('Debut programme')
    verifcsv(path_csv)
    verifdb(path_db)
    veriflog(path_log)
    
    logging.debug('Connection a la base de données')
    connection=sqlite3.connect(path_db)
    cursor=connection.cursor()
    
    createtab(cursor)
    insertion_bdd(cursor,path_csv)
    
    



connection.commit()
cursor.close()
 


