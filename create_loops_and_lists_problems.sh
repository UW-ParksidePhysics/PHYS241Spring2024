#!/bin/sh

chapter_name="loops_and_lists"


mkdir $chapter_name

files="table_temperature_conversion_with_while.py table_temperature_conversion_and_approximation.py sum_integers.py generate_coordinate_grid.py table_vertical_projectile_positions.py table_vertical_projectile_with_lists.py sum_integer_reciprocals_using_while.py calculate_vertical_projectile_with_nested_lists.py"

for file in $files 
do 
	touch $chapter_name/$file 
#	git add $chapter_name/$file 
done
git add $chapter_name/

name=`echo $chapter_name | sed 's/_/ /g'`

git commit –m "Adding empty files for $name"
git push

