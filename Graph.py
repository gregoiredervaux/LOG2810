import os
import re

class Graph:

    l_arc = []
    l_sommet = []
    matrice_graph =[]

    def __init__(self, chemin_fichier):
        if not isinstance(chemin_fichier, string):
            raise Exception('le chemin du fichier doit etre un string, Ici, chemin = {}'.format(chemin_fichier))

        else:
            try:
                fichier_source = open(chemin_fichier, "r")
            except ValueError:
                print("nous n'avons pu ouvrir le chemin du fichier :" + chemin_fichier)
            l_line= fichier_source.read().splitlines()
            l_sommet = []
            l_arc = []
            for i in l_lines:
                if re.match(r"^[0-9],[0-1]$", i):
                   id= re.findall(r"^([0-9]+),$", i)
                   type = re.findall(r",([0-9]+)$",i)
                   sommet = new(Sommet(id, type))
                   l_sommet.append(sommet)

                elif re.match(r"^[0-9],[0-9],[0-9]$", i):
                    point_1 = re.findall(r"^([0-9]+),", i)
                    point_2 = re.findall(r",([0-9]+),")
                    distance = re.findall(r",([0-9]+)$", i)
                    arc = new(Arc(point_1, point_2, distance))
                    l_arc.append(arc)

                elif re.match(r" ",i):
                    pass

                else:
                    raise Exception('le fichier text est corrompu, la ligne {} n\'a pas le bon format (\"int,int\"'.format(i))

                self.l_arc=l_arc
                self.l_sommet=l_sommet

    def __str__(self):
        print("la liste des chemins est: " + self.l_arc)
        print("la liste des sommets est: " + self.l_sommet)

    def creerGraphe(self):
        max=0
        for i in self.l_sommet:
            if self.l_sommet.get_id() > max:
                max = self.l_sommet.get_id()

        while len(self.matrice_graph)<= max:
            line=[]

            while len(line)<=max:
                line.append("")

            self.matrice_graph.append(column)

        for arc in self.l_arc:
            if arc.get_id()[0] < arc.get_id[1]:
                n_line = arc.get_id()[0]
                n_colmun = arc.get_id()[1]
            else:
                n_line = arc.get_id()[1]
                n_colmun = arc.get_id()[0]
            self.matrice_graph[n_line][n_colmun]=arc.get_distance()


    def lireGrapĥe(self):
        """
        fonction d'affichage du graph (recursif)
        :return: ...
        """