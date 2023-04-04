import mysql.connector

# Connexion à la base de données
cnx = mysql.connector.connect(user='root', password='Jobbax_La_Menace',
                              host='localhost', database='LaPlateforme')

# Récupération des employés dont le salaire est supérieur à 3000
cursor = cnx.cursor()
query = "SELECT * FROM employes WHERE salaire > 3000"
cursor.execute(query)

# Affichage des résultats
for (id, nom, prenom, salaire, id_service) in cursor:
    print("{}, {}: {}€ (service {})".format(nom, prenom, salaire, id_service))

# Fermeture de la connexion
cursor.close()
cnx.close()
