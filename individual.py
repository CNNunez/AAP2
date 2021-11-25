# Class with the individual caracteristics/chromosomes
class individual:
    #Attributes/cromosomas
    coord_x = 0
    coord_y = 0
    adap_score = 0
    color = [0,0,0]
    probabilidad = 0

    #Init
    def __init__(self, x, y):
        self.coord_x = x
        self.coord_y = y

    #Methods
    def set_score(self, score):
        self.adap_score = score

    def set_color(self, color):
        self.color = color

    def set_probabilidad(self, probabilidad):
        self.probabilidad = probabilidad
