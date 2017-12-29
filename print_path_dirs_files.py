#!/usr/bin/env python3

from os import walk

# Set path here
mypath = "/home/"

# Variables for directory path, directory names and file names
dirpath_list = ""
dirnames_list = []
filenames_list = []

# Loop through directory path, directory names 
# and file names to save in associated variables
for (dirpath, dirnames, filenames) in walk(mypath):
    dirpath_list = dirpath
    dirnames_list.extend(dirnames,)
    filenames_list.extend(filenames)
    break

# Print a formated string that displays all the variables' values
print("dirpath:\n {}\n\ndirnames:\n {}\n\nfilenames:\n {}\n\n".format(
	dirpath_list,dirnames_list, filenames_list))