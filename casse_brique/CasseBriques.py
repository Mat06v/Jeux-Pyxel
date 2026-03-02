#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 16:26:45 2023

@author: frindel
"""
from Brique import Brique

class CasseBriques:
    """
    Classe représentant le jeu de casse-briques.
    """

    def __init__(self):
        """
        Initialise une instance de CasseBriques avec une liste vide de briques et un score initialisé à zéro.
        """
        self.score = 0
        self.briques = []

    def ajouter_brique(self, brique):
        """
        Ajoute une brique à la liste des briques du jeu.

        Args:
            brique (Brique): La brique à ajouter.
        """
        self.briques.append(brique)

    def afficher_briques(self):
        """
        Affiche les caractéristiques de chaque brique dans la liste des briques.
        """
        for b in self.briques:
            print(b)
            print()


    def impact_brique(self, ball_x, ball_y):
        """
        Retourne la brique touchée (objet) ou None.
        """
        for i in range(len(self.briques)):
            b = self.briques[i]
            pts = b.is_hit(ball_x, ball_y)
            self.score += pts
            if b.solidite == 0:
                print("Brique détruite")
                return self.briques.pop(i)
            if pts != 0:
                return b
        return None        

    def afficher_score(self):
        """
        Affiche le score actuel du jeu.
        """
        print(f"Score: {self.score}")

    def construire_rangee_briques(self, l, h, solidite, points, nombre_briques, espace_entre_briques=5, numero_ligne=1):
        """
        Construit une rangée de briques avec les caractéristiques spécifiées et les ajoute au jeu.

        Args:
            couleur (str): La couleur des briques.
            solidite (int): La solidité des briques.
            points (int): Le nombre de points attribués lorsque la balle détruit la brique.
            nombre_briques (int): Le nombre de briques dans la rangée.
            espace_entre_briques (int, optional): L'espace horizontal entre les briques. Par défaut, 5.
            numero_ligne (int, optional): Le numéro de la ligne où placer les briques. Par défaut, 1.
        """
        # Ajoute une rangée de briques horizontalement
        largeur_brique = l  # Remplacez par la largeur souhaitée
        hauteur_brique = h  # Remplacez par la hauteur souhaitée
        position_y = espace_entre_briques + (hauteur_brique + espace_entre_briques) * (numero_ligne-1)  # Ajuste la position en y de la rangée
        position_x = espace_entre_briques

        for _ in range(1, nombre_briques - 1):
            position_x += largeur_brique + espace_entre_briques
            brique = Brique("", solidite, points, position_x, position_y, largeur_brique, hauteur_brique)
            self.ajouter_brique(brique)
