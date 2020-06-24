#!/bin/zsh
#maybe you are using bash,fix the first line.
#!/bin/zsh
# Program:
#	This program shows function.
#History:
#2015/xx/xx  wikinee First release

export PATH

function printit(){

	echo -n "you chioce is : "

}

echo "this program will show you selections."

case $1 in
	"one")
	printit; echo $1 | tr 'a-z' 'A-Z'
	;;
	"two")
	printit; echo $1 | tr 'a-z' 'A-Z'
	;;
	"three")
	printit; echo $1 | tr 'a-z' 'A-Z'
	;;
	*)
	echo "Usage $0 { one | two | three }"
	;;
esac