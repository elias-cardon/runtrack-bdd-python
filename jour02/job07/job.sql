CREATE TABLE employes (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nom VARCHAR(255),
  prenom VARCHAR(255),
  salaire DECIMAL(10,2),
  id_service INT
);

INSERT INTO employes (nom, prenom, salaire, id_service)
VALUES
('Dupont', 'Jean', 3500, 1),
('Martin', 'Sophie', 2800, 2),
('Lefebvre', 'Pierre', 4200, 3),
('Dubois', 'Marie', 2500, 1),
('Leclerc', 'Julie', 3200, 2);

SELECT * FROM employes WHERE salaire > 3000;

CREATE TABLE services (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nom VARCHAR(255)
);

INSERT INTO services (nom) VALUES ('Service 1'), ('Service 2'), ('Service 3');

SELECT employes.nom, employes.prenom, services.nom AS service
FROM employes
JOIN services ON employes.id_service = services.id;
