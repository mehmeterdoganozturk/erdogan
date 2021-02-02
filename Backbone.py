class Backbone:

    switches = []

    def __init__(self, id, ip, binaad, binaid):
        self.id = id
        self.ip = ip
        self.binaid = binaid
        self.binaad = binaad

    def setswitches(self, switches):
        self.switches = switches

