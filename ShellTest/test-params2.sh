#!/bin/zsh
#maybe you are using bash,fix the first line.
#!/bin/zsh
# Program:
#	This program shows effect of shift function.
#History:
#2015/xx/xx  wikinee First release

export PATH

echo "Total parameter number is ==> $#"
echo "Your whole parameter is ==>'$@' "
shift
echo "Total parameter number is ==> $#"
echo "Your whole parameter is ==>'$@' "
shift 3
echo "Total parameter number is ==> $#"
echo "Your whole parameter is ==>'$@' "

