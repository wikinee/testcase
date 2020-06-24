#!/bin/zsh
#maybe you are using bash,fix the first line.
#!/bin/zsh
# Program:
#	This program shows you PC network status.
#History:
#2015/xx/xx  wikinee First release

export PATH
network="192.168.1"
for sitenu in $(seq 1 100)
do
	ping -c 1 -w 1 ${network}.${sitenu} &> /dev/null && result=0 || result=1
#	ping  $(network).$(sitenu) &> /dev/null && result=0 || result=1
	if [ "$result" == 0 ]; then 
		echo "Server ${network}.${sitenu} is UP."
	else 
		echo "Server ${network}.${sitenu} is DOWN."
	fi
done
