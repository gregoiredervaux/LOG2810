class Arc:

    id = []
    distance="0"

    def __init__(self, point_1, point_2, distance):

        if (isinstance(point_1, int) and isinstance(point_2, int)):
            self.id=[point_1, point_2]
        else:
            raise Exception('les deux premier parametres doivent etre des entier. Ici, [{}]'.format([point_1, point_2]))
        if (isinstance(distance, int)):
            self.distance= distance
        else:
            raise Exception('distance doit etre un entier. Ici, distance = {}'.format(distance))


    def get_id(self):
        return(self.id)

    def get_distance(self):
        return(self.distance)

    def set_distance(self, entier):
        if (isinstance(entier, int)):
            self.type = string
        else:
            raise Exception('distance doit etre un entier. Ici, distance = {}'.format(distance))
    