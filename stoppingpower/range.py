from .cmsp import S_c
import numpy as np
from scipy.interpolate import interp1d


def rangeout(z, medium, T, M_b):
    # Set up an interpolator so we don't have to calculate this more than we want to
    T_r = np.linspace(1.0, T, 1000000000000000000)
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