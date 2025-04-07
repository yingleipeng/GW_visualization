This script references the paper "Second post-Newtonian motion of compact binaries" by Schafer and Wex. It plots the trajectories
given by equations (22) and (23), (21) isn't needed since that only defines the period of the trajectories. There are free variables
that need to be specified, namely E (total energy), J (total angular momentum), and nu (symmetric mass ratio),
for the validate_params function (this checks whether the combination of values
specified gives a valid orbit), and for the function solve_orbit. 

E must be less than 0 for a bound orbit, nu must be within the interval (0, 1/4], and J also has another constraint on it
determined by the ellipticity of the orbit. 

This takes a while to run since the animation is a bit large
