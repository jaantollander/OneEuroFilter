import math


def exponential_smoothing(a, x, x_prev):
    return a * x + (1 - a) * x_prev


# def smoothing_factor(t_e, cutoff):
#     tau = 1.0 / (2 * math.pi * cutoff)
#     return 1.0 / (1.0 + tau / t_e)


def smoothing_factor(t_e, cutoff):
    r = 2 * math.pi * cutoff * t_e
    return r / (r + 1)


class OneEuroFilter:
    def __init__(self, t0, x0, dx0=0.0, min_cutoff=1.0, beta=0.0, d_cutoff=1.0):
        self.min_cutoff = float(min_cutoff)
        self.beta = float(beta)
        self.d_cutoff = float(d_cutoff)

        self.x_prev = float(x0)
        self.dx_prev = float(dx0)
        self.t0 = float(t0)

    def __call__(self, t, x):
        t_e = t - self.t0

        # Derivative of the signal
        a_d = smoothing_factor(t_e, self.d_cutoff)
        dx = (x - self.x_prev) / t_e
        dx_hat = exponential_smoothing(a_d, dx, self.dx_prev)

        # Value of the signal
        cutoff = self.min_cutoff + self.beta * abs(dx_hat)
        a = smoothing_factor(t_e, cutoff)
        x_hat = exponential_smoothing(a, x, self.x_prev)

        # Memorize the values.
        self.x_prev = x_hat
        self.dx_prev = dx_hat
        self.t0 = t

        return x_hat
