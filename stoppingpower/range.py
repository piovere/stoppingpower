from .cmsp import S_c
import numpy as np
from scipy.interpolate import interp1d
import scipy.constants as const
from scipy.special import expi


def rangeout(z, medium, T, M_b):
    # Set up an interpolator so we don't have to calculate this more than we want to
    T_r = np.linspace(1.0, T, 100000)
    interpolator = interp1d(T_r, S_c(z, medium, T_r, M_b))

    # Don't need to check below this threshold
    lower_limit = 2 * M_b

    # this is the tuning parameter.
    # units are in density*length (g/cm^2)
    step = 0.001

    t = T
    l = 0
    while t >= lower_limit:
        l += step / medium.density
        t = t - interpolator(t) * step

    return l


def exit_energy(z, medium, T, M_b, thickness):
    # Set up an interpolator so we don't have to calculate this more than we want to
    T_r = np.linspace(1.0, T, 10000000)
    interpolator = interp1d(T_r, S_c(z, medium, T_r, M_b))

    # Don't need to check below this threshold
    lower_limit = 2 * M_b

    # this is the tuning parameter.
    # units are in density*length (g/cm^2)
    step = 0.00001

    collision_counter = 0

    t = T
    l = 0
    while t >= lower_limit and l <= thickness:
        l += step / medium.density
        t = t - interpolator(t) * step
        collision_counter += 1

    if t <= lower_limit:
        return 0.0
    else:
        return t


def u(material, T):
    """

    :type material: materials.Material
    :param material: Material through which the particle is moving
    :param T: Kinetic energy of the particle
    :return: value of u for the range equation
    """
    numerator = (4.0 * const.value('electron mass energy equivalent in MeV') * T)
    I = material.I_a()
    denominator = I * (10 ** (-6.0))

    return (numerator / denominator) ** 2.0


def range_equation(z, medium, T, A):
    r0 = const.value('classical electron radius') * 100 # m to cm
    me = const.value('electron mass energy equivalent in MeV')
    A = const.value('Avogadro constant')
    m_to_e = const.value('atomic mass constant energy equivalent in MeV')

    numerator = A * m_to_e * ((medium.I * 10 ** (-6.0)) ** 2.0)
    const_part = 32.0 * (z ** 2.0) * np.pi * (r0 ** 2.0) * (me ** 3.0)
    electron_density_part = A * medium.Z_eff() * medium.density / medium.mass
    denominator = const_part * electron_density_part

    u_num = u(medium, T)

    ei_part = expi(u_num)

    result = numerator * ei_part / denominator

    return result
