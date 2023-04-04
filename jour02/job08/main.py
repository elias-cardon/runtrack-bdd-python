import mysql.connector

class Zoo:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Jobbax_La_Menace",
            database="zoo"
        )
        self.cursor = self.connection.cursor()

    def create_animal(self, name, race, cage_id, birthdate, country):
        query = "INSERT INTO animal (name, race, cage_id, birthdate, country) VALUES (%s, %s, %s, %s, %s)"
        values = (name, race, cage_id, birthdate, country)
        self.cursor.execute(query, values)
        self.connection.commit()
        print(f"{self.cursor.rowcount} animal ajouté")

    def update_animal(self, id, name, race, cage_id, birthdate, country):
        query = "UPDATE animal SET name = %s, race = %s, cage_id = %s, birthdate = %s, country = %s WHERE id = %s"
        values = (name, race, cage_id, birthdate, country, id)
        self.cursor.execute(query, values)
        self.connection.commit()
        print(f"{self.cursor.rowcount} animal modifié")

    def delete_animal(self, id):
        query = "DELETE FROM animal WHERE id = %s"
        values = (id,)
        self.cursor.execute(query, values)
        self.connection.commit()
        print(f"{self.cursor.rowcount} animal supprimé")

    def create_cage(self, superficie, capacite):
        query = "INSERT INTO cage (superficie, capacite) VALUES (%s, %s)"
        values = (superficie, capacite)
        self.cursor.execute(query, values)
        self.connection.commit()
        print(f"{self.cursor.rowcount} cage ajoutée")

    def update_cage(self, id, superficie, capacite):
        query = "UPDATE cage SET superficie = %s, capacite = %s WHERE id = %s"
        values = (superficie, capacite, id)
        self.cursor.execute(query, values)
        self.connection.commit()
        print(f"{self.cursor.rowcount} cage modifiée")

    def delete_cage(self, id):
        query = "DELETE FROM cage WHERE id = %s"
        values = (id,)
        self.cursor.execute(query, values)
        self.connection.commit()
        print(f"{self.cursor.rowcount} cage supprimée")

    def get_all_animals(self):
        query = "SELECT * FROM animal"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for animal in result:
            print(animal)

    def get_animals_in_cages(self):
        query = "SELECT animal.id, animal.name, cage.id FROM animal JOIN cage ON animal.cage_id = cage.id"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for animal in result:
            print(f"{animal[0]} - {animal[1]} - cage {animal[2]}")

    def get_total_cage_area(self):
        query = "SELECT SUM(superficie) FROM cage"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        print(f"La superficie totale de toutes les cages est de {result[0]} m2")

    def close(self):
        self.cursor.close()
        self.connection.close()

zoo = Zoo()

while True:
    print("Que souhaitez-vous faire ?")
    print("1. Ajouter un animal")
    print("2. Modifier un animal")
    print("3. Supprimer un animal")
    print("4. Ajouter une cage")
    print("5. Modifier une cage")
    print("6. Supprimer une cage")
    print("7. Afficher la liste des animaux")
    print("8. Afficher la liste des animaux par cage")
    print("9. Calculer la superficie totale des cages")
    print("10. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        nom = input("Nom de l'animal : ")
        race = input("Race de l'animal : ")
        id_cage = input("ID de la cage : ")
        date_naissance = input("Date de naissance de l'animal (AAAA-MM-JJ) : ")
        pays_origine = input("Pays d'origine de l'animal : ")
        zoo.create_animal(nom, race, id_cage, date_naissance, pays_origine)

    elif choix == "2":
        id_animal = input("ID de l'animal à modifier : ")
        nom = input("Nouveau nom de l'animal : ")
        race = input("Nouvelle race de l'animal : ")
        id_cage = input("Nouvel ID de la cage : ")
        date_naissance = input("Nouvelle date de naissance de l'animal (AAAA-MM-JJ) : ")
        pays_origine = input("Nouveau pays d'origine de l'animal : ")
        zoo.update_animal(id_animal, nom, race, id_cage, date_naissance, pays_origine)

    elif choix == "3":
        id_animal = input("ID de l'animal à supprimer : ")
        zoo.delete_animal(id_animal)

    elif choix == "4":
        superficie = input("Superficie de la cage : ")
        capacite_max = input("Capacité maximale de la cage : ")
        zoo.create_cage(superficie, capacite_max)

    elif choix == "5":
        id_cage = input("ID de la cage à modifier : ")
        superficie = input("Nouvelle superficie de la cage : ")
        capacite_max = input("Nouvelle capacité maximale de la cage : ")
        zoo.update_cage(id_cage, superficie, capacite_max)

    elif choix == "6":
        id_cage = input("ID de la cage à supprimer : ")
        zoo.delete_cage(id_cage)

    elif choix == "7":
        zoo.get_all_animals()

    elif choix == "8":
        zoo.get_animals_in_cages()

    elif choix == "9":
        zoo.get_total_cage_area()

    elif choix == "10":
        break

    else:
        print("Choix invalide.")