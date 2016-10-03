import numpy as np
import scipy.constants as const
from scipy.interpolate import interp1d
from .utility import beta_2, gamma_2


def normal_S_c(z, Z, T, M_b, I, M_m):
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

    first = 4.0 * pi * (r ** 2) * m_e
    second = N_A * Z / M_m
    third = z ** 2.0 / beta_2(T, M_b)
    logpart = (2.0 * m_e * beta_2(T, M_b) * gamma_2(T, M_b)) / (I)
    fourth = np.log(logpart) - beta_2(T, M_b)

    return first * second * third * fourth
