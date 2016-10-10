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
    T_r = np.linspace(1.0, T, 100000)
    interpolator = interp1d(T_r, S_c(z, medium, T_r, M_b))

    # Don't need to check below this threshold
    lower_limit = 2 * M_b

    # this is the tuning parameter.
    # units are in density*length (g/cm^2)
    step = 0.001

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


def u(material, T, A):
    """

    :type material: materials.Material
    :param material: Material through which the particle is moving
    :param T: Kinetic energy of the particle
    :return: value of u for the range equation
    """
    numerator = (4.0 * const.value('electron mass energy equivalent in MeV') * T)
    I = material.I_a()
    denominator = I * (10 ** (-6.0)) * A * const.value('atomic mass constant energy equivalent in MeV')

    result = (numerator / denominator) ** 2.0

    return result


def range_equation(z, medium, T, A):
    r0 = const.value('classical electron radius') * 100 # m to cm
    me = const.value('electron mass energy equivalent in MeV')
    NA = const.value('Avogadro constant')
    m_to_e = const.value('atomic mass constant energy equivalent in MeV')

    numerator = A * m_to_e * ((medium.I * 10 ** (-6.0)) ** 2.0)
    const_part = 32.0 * (z ** 2.0) * np.pi * (r0 ** 2.0) * (me ** 3.0)
    electron_density_part = NA * medium.Z_eff() * medium.density / medium.mass
    denominator = const_part * electron_density_part

    u_num = u(medium, T, A)

    ei_part = expi(np.log(u_num))

    result = numerator * ei_part / denominator

    return result


def energy_deposition(z, medium, T, M_b, thickness):
    energy_left = exit_energy(z, medium, T, M_b, thickness)

    result = T - energy_left

    return result


def nuclear_fraction(beam_a, medium, thickness):
    Sigma = medium.macroscopic_cross_section(beam_a)

    res = 1.0 - np.exp(-1.0 * medium.macroscopic_cross_section(beam_a) * thickness)

    return res
