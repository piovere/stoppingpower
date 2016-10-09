# from pyne import data
# from pyne import nuc_data
# from pyne.material import MaterialLibrary


# mats = MaterialLibrary(nuc_data, datapath='/material_library/materials', nucpath='/material_library/nucid')

class Material(object):
    def __init__(self, *args, **kwargs):
        # super(object, self).__init__(self, *args, **kwargs)
        self.Z = kwargs.get("Z")
        self.I = kwargs.get("I")
        self.density = kwargs.get("density")
        self.mass = kwargs.get("mass")

    def Z_eff(self):
        if self.Z is None:
            raise Exception("I don't have a Z value for this material")
        else:
            return self.Z

    def I_a(self):
        """

        :rtype: float
        """
        if self.I is None:
            return 9.73 * self.Z_eff() + 58.8 * self.Z_eff() ** -0.19
        else:
            return self.I

materials = {
    "Concrete": Material(Z=0.502746276, I=135.2, density=2.3, mass=1.0),
    "Water": Material(Z=0.555086707, I=75.0, density=1.0, mass=1.0),
    "Air": Material(Z=0.499184128, I=85.7, density=0.00120479, mass=1.0),
    "Tissue": Material(Z=0.558459289, I=63.2, density=0.92, mass=1.0),
    "Hydrogen, 1": Material(Z=1.0, mass=1.008, I=19.2, density=0.000083748),
    "Carbon, 6": Material(Z=6.0, mass=12.011, I=81.0, density=2.0),
    "Nitrogen, 7": Material(Z=7.0, mass=14.007, I=82.0, density=0.00116528),
    "Oxygen, 8": Material(Z=8.0, mass=15.999, I=95.0, density=0.00133151),
    "Sodium, 11": Material(Z=11.0, mass=22.98976928, I=149.0, density=0.971),
    "Magnesium, 12": Material(Z=12.0, mass=24.305, I=156.0, density=1.74),
    "Aluminum, 13": Material(Z=13.0, mass=26.9815385, I=166.0, density=2.6989),
    "Silicon, 14": Material(Z=14.0, mass=28.085, I=173.0, density=2.33),
    "Argon, 18": Material(Z=18.0, mass=39.948, I=188.0, density=0.00166201),
    "Iron, 26": Material(Z=26.0, mass=55.845, I=286.0, density=7.874),
    "Copper, 29": Material(Z=29.0, mass=63.546, I=322.0, density=8.96),
    "Tin, 50": Material(Z=50.0, mass=118.71, I=488.0, density=7.31),
    "Tungsten, 74": Material(Z=74.0, mass=183.84, I=727.0, density=19.3),
    "Gold, 79": Material(Z=79.0, mass=196.966569, I=790.0, density=19.32),
    "Lead, 82": Material(Z=82.0, mass=207.2, I=823.0, density=11.35),
    "Uranium, 92": Material(Z=92.0, mass=238.02891, I=890.0, density=18.95)
}