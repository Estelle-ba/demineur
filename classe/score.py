import csv
import os

SCORE_FILES = '../data/scores.csv'

class Score :

    def __init__ (self, name, difficulty, score) :
        self.__name = name
        self.__difficulty = difficulty
        self.__score = score



    # Créé un fichier score si il n'éxiste pas et rajoute les scores du joueur dedans
    def register_score(self):

        # Vérifie si le fichier existe
        files_exist = os.path.isfile(SCORE_FILES)

        # Ouvre le fichier en mode ajout
        with open(SCORE_FILES, mode='a', newline='') as scvfile:
            writer = csv.writer(scvfile)

            # Si le fichier est vide, écrire les en-têtes
            if not files_exist:
                writer.writerow(['Name', 'Difficulty', 'Score'])

            # Ajouter les données
            writer.writerow([self.__name, self.__difficulty, self.__score])
            print(f"Score de {self.__name} enregistré avec succès !")

    def get_score(self):
        return self.__score


# Création de score
Alice = Score("Alice", "Facile", 1200)
Bob = Score("Bob", "Difficile", 309)
Charlie = Score("Charlie", "Moyen", 203)

Alice.register_score()
Bob.register_score()
Charlie.register_score()
