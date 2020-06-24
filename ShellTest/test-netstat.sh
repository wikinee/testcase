#!/bin/zsh
#maybe you are using bash,fix the first line.
#!/bin/zsh
# Program:
#	Using netstat and grep to detect WWW,SSH,FTP and Mail service.
#History:
#2015/xx/xx  wikinee First release

export PATH

echo "Now,I will detect you *nix services!"
echo -e "The www,ftp,ssh,and mail will be detect! \n"

testing = $(netstat -tuln | grep ":80")
if [ "$testing" != "" ]; then
	echo -e "The WWW is running in you system."
fi

testing = $(netstat -tuln | grep ":22")
if [ "$testing" != "" ]; then
	echo -e "The SSH is running in you system."
fi
testing = $(netstat -tuln | grep ":21")
if [ "$testing" != "" ]; then
	echo -e "The FTP is running in you system."
fi
testing = $(netstat -tuln | grep ":25")
if [ "$testing" != "" ]; then
	echo -e "The Mail is running in you system."
fi

