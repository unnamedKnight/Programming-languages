'''
Python Files
'''

# - When we use file.read() it will give us all the text inside the file
# - When we use file.readlines() it will give us a list of all the lines in the file
# - We can use replace method to remove white space from the middle of a sentence

# - When we are using write mode we have to be careful, Because write mode not only creates new files
# - It also override the same existing file

# - Append mode appends at the end of an existing file
# - In append mode we are not overwriting the file we are just appending new data at the end of the file

#- r+ mode is for reading file and writing. We can simply read and write in a file with this mode.


# - file.seek() Changes the cursor location in the file

# - when we do file.read(), the cursor's position is at the end of the file.
# - Because file.read() reads the whole file, so cursor stays at the end of the file.
# - But we can change cursor position manually with file.seek() method