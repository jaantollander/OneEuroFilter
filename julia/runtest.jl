using Test

include("one_euro_filter.jl")
no_errors(x) = true

@test no_errors(smoothing_factor(1.0, 1.0))
@test no_errors(exponential_smoothing(0.5, 1.0, 1.0))
@test no_errors(one_euro_filter(0.0, 0.0, 1.0, 1.0))
@test no_errors(one_euro_filter(0.0, 0.0, 1.0, 1.0, 1.0))

@test no_errors(smoothing_factor.(1.0, [1.0, 2.0]))
@test no_errors(exponential_smoothing.([0.5, 0.6], [1.0, 2.0], [1.0, 2.0]))
@test no_errors(one_euro_filter(0.0, [0.0], 1.0, [1.0]))
@test no_errors(one_euro_filter(0.0, [0.0], 1.0, [1.0], [1.0]))
