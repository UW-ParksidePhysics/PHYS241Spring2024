#!/bin/sh

mkdir computing_with_formulas

files="add_two_numbers.py print_hello_world.py compare_life_expectancy_to_seconds.py convert_length.py calculate_liter_mass.py calculate_interest_growth.py calculate_shape_regions.py verify_trigonometric_identity.py calculate_displacement.py verify_binomial_expansions.py calculate_gaussian_at_one_value.py calculate_ball_drag_and_gravity.py calculate_egg_cook_time.py"

for file in $files 
do 
	touch computing_with_formulas/$file 
	git add computing_with_formulas/$file 
done

git commit –m “Adding empty files for computing with formulas”
git push

