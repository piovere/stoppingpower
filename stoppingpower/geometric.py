from numpy import pi


def cross_section(a1, a2):
    r0 = 1.4 * 10 ** -13

    b1 = a1 ** (1.0 / 3.0)
    b2 = a2 ** (1.0 / 3.0)

    sigma = pi * (r0 ** 2.0) * (b1 + b2) ** 2.0

    # convert from cm^2 to barn
    return sigma * 10.0 ** 24
