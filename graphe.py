
import os
import re
# import networkx as nx
# import numpy as np
from typing import List

import matplotlib.pyplot as plt
import math


# import sommet
# import arc

class Sommet:
    """Sommet d'un graph
    2 arguments:
        - type="0" ou "1" ("0" si il n'y a pas de borne elec sur ce noeud, ou type="1" si il y en a une)
        - id (type int) identifiant du noeud
    """

    id_sommet = 0
    presence_borne = 'None'
    color = 'b'

    def __init__(self, id_sommet, presence_borne):
        """Constructeur
                entree: id, Type:
                    id
                        - int [0-9]+
                    type:
                        - "1" si le sommet comporte une borne elec
                        - "0" si le sommet ne comporte pas de borne elec
                    return: objet Sommet avec le type, et l'id specifies en entree
                """
        self.id_sommet = id_sommet
        if (presence_borne != '0' and presence_borne != '1'):
            print(presence_borne)
            raise Exception(
                'le type (2eme parametre) doit etre egale a 0 (pas de borne elec) ou a 1 (borne elec). Ici, type = {}'.format(
                    presence_borne))

    def get_id(self):
        return (self.id_sommet)

    def get_presence_borne(self):
        return (self.presence_borne)

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color

    def set_presence_borne(self, presence_borne):
        if (presence_borne != '0' and presence_borne != '1'):
            raise Exception(
                'le type (2eme parametre) doit etre egale a 0 (pas de borne elec) ou a 1 (borne elec). Ici, type = {}'.format(
                    type))
        else:
            self.presence_borne = presence_borne


class Arc:
    """Segement du graphe
    comportent un id compose des 2 id des sommets correspondant, et une distance
    """
    id_arc = []
    distance = "0"
    color = 'r'

    def __init__(self, point_1, point_2, distance):
        """Constructeur
        :param point_1:
        :param point_2:
        :param distance:
        """

        if re.match(r"[0-9]+", point_1) and re.match(r"[0-9]", point_2):
            self.id_arc = [point_1, point_2]
        else:
            raise Exception('les deux premier parametres doivent etre des entier. Ici, [{}]'.format([point_1, point_2]))
        if re.match(r"[0-9]+", point_1):
            self.distance = distance
        else:
            raise Exception('distance doit etre un entier. Ici, distance = {}'.format(distance))

    def get_id(self):
        return (self.id_arc)

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color

    def get_distance(self):
        return (self.distance)

    def set_distance(self, entier):
        if (isinstance(entier, int)):
            self.distance = entier
        else:
            raise Exception('distance doit etre un entier. Ici, distance = {}'.format(self.distance))


class Graphe:
    """
    Objet Graphe
    """

    l_arc = []
    l_sommet = []
    matrice_graph = []

    def __init__(self, chemin_fichier):
        """Constructeur du Graph
        :param chemin_fichier:
        lit le fichier source et construit 2 listes comportant les objets sommets et les objets arc
        """
        global fichier_source
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
                if re.match(r"^[0-9]+,[0-1]$", i):
                    id_sommet = re.findall(r"^([0-9]+),", i)
                    presence_borne = re.findall(r",([0-9]+)$", i)
                    sommet = Sommet(id_sommet[0], presence_borne[0])
                    l_sommet.append(sommet)

                elif re.match(r"^[0-9]+,[0-9]+,[0-9]+$", i):
                    point_1 = re.findall(r"^([0-9]+),", i)
                    point_2 = re.findall(r",([0-9]+),", i)
                    distance = re.findall(r",([0-9]+)$", i)
                    arc = Arc(point_1[0], point_2[0], distance[0])
                    l_arc.append(arc)

                elif i == '':
                    pass

                else:
                    raise Exception(
                        'le fichier text est corrompu, la ligne {} n\'a pas le bon format'.format(i))

                self.l_arc = l_arc
                self.l_sommet = l_sommet

    def __str__(self):
        print("la liste des chemins est: " + str(self.l_arc))
        print("la liste des sommets est: " + str(self.l_sommet))

    def creerGraphe(self):
        """creer une matrice 2x2 du graph avec les distances entre les points
        renvoie une matrice representant le graph. Les valeurs de la matrice representent les distances entre les points
        ex: si on veut la distance entre le sommet 4 et le sommet 12, on appelera:
        distance = matrice_graph[4][12]
        :return:exemple pour un graph a 5 sommets:
                [   [12,12,52,42,""]
                    ["",45,12,"",13]
                    ["","",45,56,""]
                    ["","","",36,45]
                    ["","","","",25]    ]
        """
        # on construit une matrice vide n x n avec n le nombre de sommets
        max_id_sommet = 0
        for sommet in self.l_sommet:
            if sommet.get_id() > max_id_sommet:
                max_id_sommet = sommet.get_id()

        while len(self.matrice_graph) <= max_id_sommet:
            line = []

            while len(line) <= max_id_sommet:
                line.append("")

            self.matrice_graph.append(line)

        # on rempli la matrice avec les distances (on fait attention, la matrice doit etre symetrique)
        for arc in self.l_arc:
            if arc.get_id()[0] < arc.get_id()[1]:
                n_line = arc.get_id()[0]
                n_colmun = arc.get_id()[1]
            else:
                n_line = arc.get_id()[1]
                n_colmun = arc.get_id()[0]
            self.matrice_graph[n_line][n_colmun] = arc.get_distance()



    def lireGraphe(self, sommet_init=None, dict_sommet_coord=None, angle_arc_presc=0):
        """
        fonction d'affichage du graph recursif
        :return: dictionnaire des points : { id_sommet: (x, y), ... }
        """
        # initialisation:
        global log
        if sommet_init == None:
            sommet_init = self.l_sommet[0]
            dict_sommet_coord = {sommet_init.get_id(): (0,0)}
            log = open('log_affichage.txt', 'a')
            log.write(" nouveau affichage de graph \n")


        # recurence:
        if len(dict_sommet_coord) != len(self.l_sommet):

            #liste des id des sommets a afficher
            l_id_sommet_linked: List[int] = []

            # on parour les arcs pour trouver les sommets relie au sommet init
            for arc in self.l_arc:
                # si l'arc comporte le sommet init, alors on doit afficher le sommet oppose
                if sommet_init.get_id() == arc.get_id()[0]:
                    l_id_sommet_linked.append(arc.get_id()[1])

                elif sommet_init.get_id() == arc.get_id()[1]:
                    l_id_sommet_linked.append(arc.get_id()[0])

            # on détermine l'angle entre chaque arc partant du sommet affiche (pour faciliter l affichage)
            angle_iter_arc = (2 * math.pi) / (len(l_id_sommet_linked) + 1)

            l_sommet_a_aff = {}

            # on selectionne un sommet lie au point init (attention le compt commence a 1 !)
            for compteur_sommet, id_sommet_linked in enumerate(l_id_sommet_linked, 1):

                sommet_linked_est_dans_dico = False

                # on test si le sommet lie est deja prensent dans le dico
                for id_sommet_dico, coord in dict_sommet_coord.items():

                    if id_sommet_linked == id_sommet_dico:
                        sommet_linked_est_dans_dico = True

                # si il n'est pas present dans le dictionnaire, on lui donne des coordonnees
                if sommet_linked_est_dans_dico == False:

                    # on trouve l instance de sommet qui correspond a l id du sommet lie test
                    for sommet in self.l_sommet:

                        if sommet.get_id() == id_sommet_linked:

                            # on calcule l angle du sommet a afficher (en fct de sa position dans la liste)
                            angle_arc = ((angle_arc_presc + math.pi) + compteur_sommet * angle_iter_arc) % (2 * math.pi)

                            x = float(dict_sommet_coord[sommet_init.get_id()][0]) + math.cos(angle_arc)
                            y = float(dict_sommet_coord[sommet_init.get_id()][0]) + math.sin(angle_arc)

                            # on l ajout a la liste des sommets a afficher
                            l_sommet_a_aff[id_sommet_linked] = { 'instance': sommet,
                                                    'angle': angle_arc,
                                                    'x': x,
                                                    'y': y  }
                            # on l ajoute au dictionnaire des points qui ont un coordonnee
                            dict_sommet_coord[id_sommet_linked] = (x, y)

            # affichage dans le log
            if len(l_sommet_a_aff) != 0:
                log.write("du sommet:" + sommet_init.get_id() + "\n")
                log.write("vers les sommets: " + "\n")
                for id_sommet, donnee in l_sommet_a_aff.items():
                    log.write("     id: " + id_sommet + "\n")
                    log.write("         instance: " + str(donnee['instance']) + "\n")
                    log.write("         x: " + str(donnee['x']) + "\n")
                    log.write("         y: " + str(donnee['y']) + "\n")

            for id_sommet, donnee in l_sommet_a_aff.items():
                print(str(donnee['angle']))
                self.lireGraphe(donnee['instance'], dict_sommet_coord, donnee['angle'])

        # condition d'arret
        if len(dict_sommet_coord) == len(self.l_sommet):
            return dict_sommet_coord


    def affichageGraph(self):
        dico = self.lireGraphe()

        # on affiche d'abord les sommets
        for sommet_id, coord in dico.items():

            plt.scatter(coord[0], coord[1], c='b')
            plt.text(coord[0] + 0.1, coord[1] + 0.1, sommet_id)

        # on affiche tout axes
        for arc in self.l_arc:
            x_1, x_2, y_1, y_2 = 0, 0, 0, 0
            for sommet_id, coord in dico.items():

                if str(sommet_id) == str(arc.get_id()[0]):
                    x_1 = coord[0]
                    y_1 = coord[1]
                elif str(sommet_id) == str(arc.get_id()[1]):
                    x_2 = coord[0]
                    y_2 = coord[1]

            plt.plot([x_1, x_2], [y_1, y_2], c = 'r', linewidth= 1)

        plt.show()
