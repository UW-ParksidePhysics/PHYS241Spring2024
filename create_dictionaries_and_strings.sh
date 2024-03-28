#!/bin/sh

chapter_name="dictionaries_and_strings"
mkdir $chapter_name

files="create_constants_dictionary.py
compare_list_and_dictionary.py
read_and_plot_logarithmic_sum_output.py
create_stars_dictionary.py
plot_viscosities.py
generate_animation_report.py"

for file in $files 
do 
	touch $chapter_name/$file 
#	git add $chapter_name/$file 
done

git add $chapter_name/

name=`echo $chapter_name | sed 's/_/ /g'`

git commit –m "Adding empty files for $name"
git push
