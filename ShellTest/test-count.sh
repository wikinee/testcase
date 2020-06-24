#!/bin/zsh
#maybe you are using bash,fix the first line.
#!/bin/zsh
# Program:
#	This program shows "1+2+3+4..."
#History:
#2015/xx/xx  wikinee First release

export PATH

s=0
i=0
while [ "$i" != "100" ]
do
	i=$(($i + 1))
	s=$(($s+$i))
done
echo "The result of 1+2+3+...+99+100 = $s"


