import mysql.connector

# se connecter à la base de données
cnx = mysql.connector.connect(user='root', password='Jobbax_La_Menace', host='localhost', database='LaPlateforme')

# récupérer tous les étudiants
cursor = cnx.cursor()
query = "SELECT * FROM etudiants"
cursor.execute(query)
etudiants = cursor.fetchall()

# afficher les étudiants en console
for etudiant in etudiants:
    print(etudiant)

# fermer la connexion
cursor.close()
cnx.close()