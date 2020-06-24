#!/bin/zsh
#maybe you are using bash,fix the first line.
#!/bin/zsh
# Program:
#	This program shows user's chioce
#History:
#2015/xx/xx  wikinee First release

export PATH

read -p "Please input (Y/N):" yn

if [ "$yn" == "Y" ]||[ "$yn" == "y" ] ;then
		echo "OK,continue" 
		exit 0
fi
if [ "$yn" == "N" ]||[ "$yn" == "n" ] ;then
	echo "OH,interruput"
	exit 0
fi
echo "I don't know what you chioce is" && exit 0


