class Incident(object):
    def __init__(self, *args, **kwargs):
        super(object, self).__init__(*args, **kwargs)
        self.q = 0.0
        self.T = 0.0
        self.z = 0.0
        self.m = 0.0


    def collide(self, material):
        """

        :type material: pyne.material.Material
        """
        temp = self.T - S_c(self.q, material, self.T, self.m)
        if temp <= 0.0:
            self.T = 0.0
        else:
            self.T = temp


    def slow(self):
        pass
