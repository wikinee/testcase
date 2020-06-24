#!/bin/zsh
#maybe you are using bash,fix the first line.
#!/bin/zsh
# Program:
#	This program shows the script name, parameters...
#History:
#2015/xx/xx  wikinee First release

export PATH

echo "The script name is       ==> $0"
echo "Total parameter numbers is ==> $#"
[ "$#" -lt 2 ] && echo "The numbers of paramenter is less than 2. Stop here." && exit 0
echo "You whole parameter is ==> '$@' "
echo "The 1st parameter 		==> $1"
echo "The 2nd parameter 		==> $2" 

