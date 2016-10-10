from pyne import data
from pyne import nuc_data
from pyne.material import MaterialLibrary
from pyne import nucname
import scipy.constants as const
from geometric import microscopic_cross_section


mats = MaterialLibrary(nuc_data, datapath='/material_library/materials', nucpath='/material_library/nucid')

class Material(object):
    def __init__(self, *args, **kwargs):
        # super(object, self).__init__(self, *args, **kwargs)
        self._Z = kwargs.get("Z")
        self._I = kwargs.get("I")
        self._density = kwargs.get("density")
        self._mass = kwargs.get("mass")
        self._name = kwargs.get("name")

        self._data =  kwargs.get("data")

        self._A = kwargs.get("A")

    def __repr__(self):
        return self._name

    def __str__(self):
        return self._name

    @property
    def Z(self):
        if self._Z is None and self._data is None:
            raise Exception("I don't have a Z value for this material")
        elif self._data is not None:
            # This should be a MaterialLibrary material
            Zeff = 0
            for isotope, fraction in self._data.items():
                Zeff += fraction * nucname.znum(isotope) / data.atomic_mass(isotope)
            return Zeff * self.mass
        else:
            return self._Z

    @Z.setter
    def Z(self, value):
        if value >= 1 and value <= 112:
            self._Z = value
        else:
            raise ValueError("I can't handle elements above Ununbium")

    @property
    def I(self):
        """

        :rtype: float
        """
        if self._I is None:
            return 9.73 * self.Z() + 58.8 * self.Z() ** -0.19
        else:
            return self._I

    @property
    def mass(self):
        return self._mass

    @property
    def density(self):
        if self._data is not None:
            return self._data.density
        else:
            return self._density

    @property
    def A(self):
        return self._A

    def macroscopic_cross_section(self, beam_A):
        if self._data is None:
            # This must be a simple material
            N = self.density * const.Avogadro / self.mass
            sigma = microscopic_cross_section(self.A, beam_A) * 10.0 ** -24
            return N * sigma
        else:
            # Complex Material
            Sigma = 0
            for isotope, number_fraction in self._data.to_atom_dens().items():
                Sigma += microscopic_cross_section(nucname.anum(isotope), beam_A) * number_fraction / 10.0 ** 24
            return Sigma


materials = {
    "Concrete": Material(A=None, Z=0.502746276, I=135.2, density=2.3, mass=1.0, name="Concrete", data=mats['Concrete, Portland']),
    "Water": Material(A=None, Z=0.555086707, I=75.0, density=1.0, mass=1.0, name="Water", data=mats['Water, Liquid']),
    "Air": Material(A=None, Z=0.499184128, I=85.7, density=0.00120479, mass=1.0, name="Air", data=mats['Air (dry, near sea level)']),
    "Tissue": Material(A=None, Z=0.558459289, I=63.2, density=0.92, mass=1.0, name="Tissue", data=mats['Tissue, Adipose (ICRP)']),
    "Hydrogen, 1": Material(A=1.0, Z=1.0, mass=1.008, I=19.2, density=0.000083748, name="Hydrogen", data=mats["Hydrogen"]),
    "Carbon, 6": Material(A=12.0, Z=6.0, mass=12.011, I=81.0, density=2.0, name="Carbon", data=mats["Carbon, Graphite (reactor grade)"]),
    "Nitrogen, 7": Material(A=14.0, Z=7.0, mass=14.007, I=82.0, density=0.00116528, name="Nitrogen", data=mats["Nitrogen"]),
    "Oxygen, 8": Material(A=16.0, Z=8.0, mass=15.999, I=95.0, density=0.00133151, name="Oxygen", data=mats["Oxygen"]),
    "Sodium, 11": Material(A=23.0, Z=11.0, mass=22.98976928, I=149.0, density=0.971, name="Sodium", data=mats["Sodium"]),
    "Magnesium, 12": Material(A=24.0, Z=12.0, mass=24.305, I=156.0, density=1.74, name="Magnesium", data=mats["Magnesium"]),
    "Aluminum, 13": Material(A=27.0, Z=13.0, mass=26.9815385, I=166.0, density=2.6989, name="Aluminum", data=mats["Aluminum"]),
    "Silicon, 14": Material(A=28.0, Z=14.0, mass=28.085, I=173.0, density=2.33, name="Silicon", data=mats["Silicon"]),
    "Argon, 18": Material(A=40.0, Z=18.0, mass=39.948, I=188.0, density=0.00166201, name="Argon", data=mats["Argon"]),
    "Iron, 26": Material(A=56.0, Z=26.0, mass=55.845, I=286.0, density=7.874, name="Iron", data=mats["Iron"]),
    "Copper, 29": Material(A=64.0, Z=29.0, mass=63.546, I=322.0, density=8.96, name="Copper", data=mats["Copper"]),
    "Tin, 50": Material(A=119.0, Z=50.0, mass=118.71, I=488.0, density=7.31, name="Tin", data=mats["Tin"]),
    "Tungsten, 74": Material(A=184.0, Z=74.0, mass=183.84, I=727.0, density=19.3, name="Tungsten", data=mats["Tungsten"]),
    "Gold, 79": Material(A=200.0, Z=79.0, mass=196.966569, I=790.0, density=19.32, name="Gold", data=mats["Gold"]),
    "Lead, 82": Material(A=207.0, Z=82.0, mass=207.2, I=823.0, density=11.35, name="Lead", data=mats["Lead"]),
    "Uranium, 92": Material(A=238.0, Z=92.0, mass=238.02891, I=890.0, density=18.95, name="Uranium", data=mats["Uranium, Natural (NU)"])
}
