from Neocortex import Neocortex
from Synapse import Synapse
from SynapseLayer import SynapseLayer

if __name__ == '__main__':
    synapse = Synapse(1, 0.2, 3)

    layer = SynapseLayer()
    layer.addSynapse(1, 1, synapse)

    neocortex = Neocortex()
    neocortex.addLayer(layer)