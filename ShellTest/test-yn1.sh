#!/bin/zsh
#maybe you are using bash,fix the first line.
#!/bin/zsh
# Program:
#	This program shows user's chioce
#History:
#2015/xx/xx  wikinee First release

export PATH

read -p "Please input (Y/N):" yn
[ "$yn" == "Y" -o "$yn" == "y" ] && echo "OK,continue" && exit 0
[ "$yn" == "N" -o "$yn" == "n" ] && echo "OH,interruput" && exit 0
echo "I don't know what you chioce is" && exit 0


