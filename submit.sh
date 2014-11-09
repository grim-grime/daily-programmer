#This script submits the code to daily programmer 
#and adds four line spaces for submission to Reddit.

git add $1
git add submit.sh
git commit -m "To: You From: Me"
git push
sed 's/^/    /' "$1" > temp
subl temp