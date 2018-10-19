import os
import re
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import Sommet.py
import Arc.py


class Graph:
    """
    Objet Graph
    """

    l_arc = []
    l_sommet = []
    matrice_graph = []

    def __init__(self, chemin_fichier):
        """Constructeur du Graph
        :param chemin_fichier:
        lit le fichier source et construit 2 listes comportant les objets sommets et les objets arc
        """
        if not isinstance(chemin_fichier, str):
            raise Exception('le chemin du fichier doit etre un string, Ici, chemin = {}'.format(chemin_fichier))

        else:
            try:
                fichier_source = open(chemin_fichier, "r")
            except ValueError:
                print("nous n'avons pu ouvrir le chemin du fichier :" + chemin_fichier)
            l_lines = fichier_source.read().splitlines()
            l_sommet = []
            l_arc = []

            # pour chaques lignes on defini
            #    - si il s'agit d'un sommet (de la forme '1,2'; '5,4'; ...)
            #    - si il s'agit d'un arc (de la forme '1,3,21'; '1,6,31;...)
            #    - si il s'agit d'un espace dans ce cas on ne fait rien

            for i in l_lines:
                if re.match(r"^[0-9],[0-1]$", i):
                    id = re.findall(r"^([0-9]+),$", i)
                    type = re.findall(r",([0-9]+)$", i)
                    sommet = Sommet(id, type)
                    l_sommet.append(sommet)

                elif re.match(r"^[0-9],[0-9],[0-9]$", i):
                    point_1 = re.findall(r"^([0-9]+),", i)
                    point_2 = re.findall(r",([0-9]+),")
                    distance = re.findall(r",([0-9]+)$", i)
                    arc = Arc(point_1, point_2, distance)
                    l_arc.append(arc)

                elif re.match(r" ", i):
                    pass

                else:
                    raise Exception(
                        'le fichier text est corrompu, la ligne {} n\'a pas le bon format (\"int,int\"'.format(i))

                self.l_arc = l_arc
                self.l_sommet = l_sommet

    def __str__(self):
        print("la liste des chemins est: " + self.l_arc)
        print("la liste des sommets est: " + self.l_sommet)

    def creerGraphe(self):
        """creer une matrice 2x2 du graph avec les distances entre les points
        renvoie une matrice representant le graph. Les valeurs de la matrice representent les distances entre les points
        ex: si on veut la distance entre le sommet 4 et le sommet 12, on appelera:
        distance = matrice_graph[4][12]
        :return:exemple pour un graph à 5 sommets:
                [   [12,12,52,42,""]
                    ["",45,12,"",13]
                    ["","",45,56,""]
                    ["","","",36,45]
                    ["","","","",25]    ]
        """
        # on construit une matrice vide n x n avec n le nombre de sommets
        max = 0
        for i in self.l_sommet:
            if self.l_sommet.get_id() > max:
                max = self.l_sommet.get_id()

        while len(self.matrice_graph) <= max:
            line = []

            while len(line) <= max:
                line.append("")

            self.matrice_graph.append(line)

        # on rempli la matrice avec les distances (on fait attention, la matrice doit être symetrique)
        for arc in self.l_arc:
            if arc.get_id()[0] < arc.get_id[1]:
                n_line = arc.get_id()[0]
                n_colmun = arc.get_id()[1]
            else:
                n_line = arc.get_id()[1]
                n_colmun = arc.get_id()[0]
            self.matrice_graph[n_line][n_colmun] = arc.get_distance()

    def lireGrapĥe(self):
        """
        fonction d'affichage du graph (recursif)
        :return: ...
        """

