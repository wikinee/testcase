#!/bin/zsh
#maybe you are using bash,fix the first line.
#!/bin/zsh
# Program:
#	This program shows case

#History:
#2015/xx/xx  wikinee First release

export PATH

echo "This problem will shows you selection."

read -p "Input your chioce :" chioce

case $chioce in
	"one")
	echo "you chioce is ONE"
	;;
	"two")
	echo "you chioce is TWO"
	;;
	"three")
	echo "You chioce is THREE"
	;;
*)
	echo "Usage $0 ( one | two | three )"
	;;
esac




