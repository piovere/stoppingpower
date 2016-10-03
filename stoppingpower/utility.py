def beta_2(T, m):
    """ Gives value of beta^2 for a given Mass (MeV/c^2) and Kinetic Energy (MeV)
    """
    numerator = T * (T + 2 * m)
    denominator = (T + m) ** 2
    return numerator / denominator

def gamma_2(T, m):
    """ Gives value of gamma^2 for a given mass (MeV/c^2) and Kinetic Energy (MeV)
    """
    return 1.0 / (1 - beta_2(T, m)) ** 0.5
