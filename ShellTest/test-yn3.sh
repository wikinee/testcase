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

elif [ "$yn" == "N" ]||[ "$yn" == "n" ] ;then
	echo "OH,interruput"

else
echo "I don't know what you chioce is" 
fi


