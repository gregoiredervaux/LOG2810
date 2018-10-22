class Sommet:
    """Sommet d'un graph
    2 arguments:
        - type="0" ou "1" ("0" si il n'y a pas de borne elec sur ce noeud, ou type="1" si il y en a une)
        - id (type int) identifiant du noeud
    2 constructeurs:
    un avec seulement le type de renseigné => Sommet(type). ID incremente la derniere valeur d'id
    un avec le type et l'identifiant => Sommet(id, type)
    """

    id = 0
    type = 'None'

    def __init__(self, type):
        """Constructeur
        entree: Type
            - "1" si le sommet comporte une borne elec
            - "0" si le sommet ne comporte pas de borne elec
        return: objet Sommet avec le type specifie en entree, et l'id qui correspond à l'ancien sommet + 1
        """
        self.id += 1
        if (type != '0' and type != '1'):
            raise Exception('le type (2eme parametre) doit etre egale a 0 (pas de borne elec) ou a 1 (borne elec). Ici, type = {}'.format(type))

        else:
            self.type = type
    def __init__(self ,id , type):
        """Constructeur
                entree: id, Type:
                    id
                        - int [0-9]+
                    type:
                        - "1" si le sommet comporte une borne elec
                        - "0" si le sommet ne comporte pas de borne elec
                    return: objet Sommet avec le type, et l'id specifies en entree
                """
        self.id= id
        if (type != '0' and type != '1'):
            print(type)
            raise Exception('le type (2eme parametre) doit etre egale a 0 (pas de borne elec) ou a 1 (borne elec). Ici, type = {}'.format(type))


    def get_id(self):
        return(self.id)

    def get_type(self):
        return(self.type)

    def set_type(self, new_type):
        if (new_type != '0' and new_type !='1'):
            raise Exception('le type (2eme parametre) doit etre egale a 0 (pas de borne elec) ou a 1 (borne elec). Ici, type = {}'.format(type))
        else:
            self.type = new_type