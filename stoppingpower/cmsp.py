import numpy as np
import scipy.constants as const
from scipy.interpolate import interp1d
from .utility import beta_2, gamma_2
from .materials import Material


def normal_S_c(z, Z, T, M_b, I, M_m):
    # type: (float, float, float, float, float, float) -> float
    # define useful constants
    pi = np.pi
    r = const.value('classical electron radius') * 100 # convert to cm
    N_A = const.Avogadro
    m_e = const.value('electron mass energy equivalent in MeV')
    mass_to_energy = const.value('atomic mass constant energy equivalent in MeV')

    # Convert beam mass from AMU to MeV
    M_b = M_b * mass_to_energy

    # Change I from eV to MeV
    I = I * 10 ** -6

    b_2 = beta_2(T, M_b)
    g_2 = gamma_2(T, M_b)

    first = 4.0 * pi * (r ** 2) * m_e
    second = N_A * Z / M_m
    third = z ** 2.0 / b_2
    logpart = (2.0 * m_e * b_2 * g_2) / (I)
    fourth = np.log(logpart) - b_2 # - (T * (T + 2 * M_b)) / (T + M_b) ** 2.0

    return first * second * third * fourth


def S_c(z, medium, T, M_b):
    """

    :type z: float
    :type medium: Material
    :type T: float
    :type M_b: float
    :rtype: float
    """
    I = medium.I_a
    Z = medium.Z_eff()
    M_m = medium.mass

    return normal_S_c(z, Z, T, M_b, I, M_m)
