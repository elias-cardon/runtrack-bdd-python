import mysql.connector

# Connexion à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Jobbax_La_Menace",
  database="LaPlateforme"
)

# Exécution de la requête SQL
mycursor = mydb.cursor()
mycursor.execute("SELECT SUM(superficie) FROM etage")

# Récupération du résultat
result = mycursor.fetchone()[0]

# Affichage du résultat
print("La superficie de La Plateforme est de", result, "m2")

# Fermeture de la connexion
mydb.close()
