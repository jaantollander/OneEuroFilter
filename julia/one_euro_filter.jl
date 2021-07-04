function smoothing_factor(t_e::R, cutoff::R) where R <: Real
    r = 2 * π * cutoff * t_e
    r / (r + 1)
end

function exponential_smoothing(a::R, x::R, x_prev::R) where R <: Real
    a * x + (1 - a) * x_prev
end

function one_euro_filter(t::R, x::R, t_prev::R, x_prev::R, dx_prev::R; min_cutoff::R = R(1), beta::R = R(0), d_cutoff::R = R(1)) where R <: Real
    # Time difference
    t_e = t - t_prev

    # The filtered derivative of the signal.
    a_d = smoothing_factor(t_e, d_cutoff)
    dx = (x - x_prev) / t_e
    dx_hat = exponential_smoothing(a_d, dx, dx_prev)

    # The filtered signal.
    cutoff = min_cutoff + beta * abs(dx_hat)
    a = smoothing_factor(t_e, cutoff)
    x_hat = exponential_smoothing(a, x, x_prev)

    return t, x_hat, dx_hat
end

function one_euro_filter(t::R, x::R, t_prev::R, x_prev::R; min_cutoff::R = R(1), beta::R = R(0), d_cutoff::R = R(1)) where R <: Real
    one_euro_filter(t, x, t_prev, x_prev, R(0); min_cutoff, beta, d_cutoff)
end
