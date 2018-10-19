class Sommet:

    id = 0
    type = "None"

    def __init__(self, type):
        self.id += 1
        if (string != "0" and string != "1"):
            raise Exception('le type (2eme parametre) doit etre egale a 0 (pas de borne elec) ou a 1 (borne elec). Ici, type = {}'.format(type))

        else:
            self.type = type

    def __init__(self ,id , type):
        self.id= id
        if (string != "0" and string != "1"):
            raise Exception('le type (2eme parametre) doit etre egale a 0 (pas de borne elec) ou a 1 (borne elec). Ici, type = {}'.format(type))


    def get_id(self):
        return(self.id)

    def get_type(self):
        return(self.type)

    def set_type(self, string):
        if (string != "0" and string !="1"):
            raise Exception('le type (2eme parametre) doit etre egale a 0 (pas de borne elec) ou a 1 (borne elec). Ici, type = {}'.format(type))
        else:
            self.type = string

