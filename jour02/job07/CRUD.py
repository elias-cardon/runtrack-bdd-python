import mysql.connector

class Employes:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Jobbax_La_Menace",
            database="LaPlateforme"
        )
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def create(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.connection.commit()
        print(self.cursor.rowcount, "enregistrement ajouté")

    def read(self):
        query = "SELECT * FROM employes"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for row in result:
            print(row)

    def update(self, id, nom, prenom, salaire, id_service):
        query = "UPDATE employes SET nom=%s, prenom=%s, salaire=%s, id_service=%s WHERE id=%s"
        values = (nom, prenom, salaire, id_service, id)
        self.cursor.execute(query, values)
        self.connection.commit()
        print(f"{self.cursor.rowcount} enregistrement modifié")

    def delete(self, id):
        query = "DELETE FROM employes WHERE id=%s"
        values = (id,)
        self.cursor.execute(query, values)
        self.connection.commit()
        print(f"{self.cursor.rowcount} enregistrement supprimé")

    def __del__(self):
        if hasattr(self, 'connection') and self.connection.is_connected():
            self.connection.close()


if __name__ == "__main__":
    employes = Employes()

    employes.create("Doe", "John", 3000, 1)

    employes.read()

    employes.update(1, "Dupont", "Jean", 2500, 2)

    employes.read()

    employes.delete(1)

    employes.read()
