#!/bin/sh

chapter_name="user_input_and_errors_handling"


mkdir $chapter_name

files="convert_fahrenheit_temperature_to_celsius_from_input.py convert_fahrenheit_temperature_to_celsius_from_command_line.py convert_fahrenheit_temperature_to_celsius_from_file.py convert_fahrenheit_temperature_to_celsius_between_files.py convert_temperature_from_command_line.py convert_temperature.py"

for file in $files 
do 
	touch $chapter_name/$file 
#	git add $chapter_name/$file 
done
git add $chapter_name/

name=`echo $chapter_name | sed 's/_/ /g'`

git commit –m "Adding empty files for $name"
git push

