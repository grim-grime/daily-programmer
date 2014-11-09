#This script formats the code for submission.

sed 's/^/    /' "$1.py" > temp
subl temp