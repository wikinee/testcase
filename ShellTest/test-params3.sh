#!/bin/zsh
#maybe you are using bash,fix the first line.
#!/bin/zsh
# Program:
#	This program check $1 equal hello
#History:
#2015/xx/xx  wikinee First release

export PATH

if [ "$1" == "hello" ]; then
	echo "Hello,how are you?"
elif [ "$1" == "" ]; then
	echo "You MUST input parameters,ex >('$0 someword')"
else 
	echo "You only parameter is 'hello',ex> ($0 hello)"
fi