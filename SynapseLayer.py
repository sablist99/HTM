class SynapseLayer:
    def __init__(self):
        self.__coord_x = []
        self.__coord_y = []
        self.__synapse = []

    def addSynapse(self, x, y, synapse):
        self.__coord_x.append(x)
        self.__coord_y.append(y)
        self.__synapse.append(synapse)



