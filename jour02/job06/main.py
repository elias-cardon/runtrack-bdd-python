import mysql.connector

# Se connecter à la base de données
cnx = mysql.connector.connect(user='root', password='Jobbax_La_Menace',
                              host='localhost',
                              database='LaPlateforme')

# Créer un curseur pour exécuter des requêtes SQL
cursor = cnx.cursor()

# Exécuter la requête
query = "SELECT SUM(capacite) FROM salles"
cursor.execute(query)

# Récupérer le résultat
result = cursor.fetchone()[0]
print("La somme des capacités des salles est de", result)

# Fermer le curseur et la connexion à la base de données
cursor.close()
cnx.close()
