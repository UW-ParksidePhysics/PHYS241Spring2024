#!/bin/sh

chapter_name="array_computing_and_curve_plotting"


mkdir $chapter_name

files="fill_gaussian_lists.py
fill_arrays_by_for_loop.py
fill_arrays_vectorially.py
plot_gaussian.py
plot_vertical_trajectory.py
animate_heat_wave.py
plot_trajectory.py
animate_ball_trajectories.py
plot_wavepacket.py
animate_wavepacket.py
plot_water_wave_velocity_distribution.py
animate_planet_orbit.py"

for file in $files 
do 
	touch $chapter_name/$file 
#	git add $chapter_name/$file 
done
git add $chapter_name/

name=`echo $chapter_name | sed 's/_/ /g'`

git commit –m "Adding empty files for $name"
git push

