exponential_smoothing(α, x, x_prev) = α * x + (1 - α) * x_prev

function smoothing_factor(t_e, f_c)
    r = 2 * π * f_c * t_e
    return r / (r + 1)
end
