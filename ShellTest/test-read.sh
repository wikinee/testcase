#!/bin/zsh
#maybe you are using bash,fix the first line.
#!/bin/zsh
# Program:
#	User input his first name and last name.Program shows his full name.
#History:
#2015/xx/xx  wikinee First release

export PATH

read -p "Please input your first name: " firstname
read -p "Pleast input your last name: " lastname
echo -e "\nYour full name is :$firstname $lastname"

