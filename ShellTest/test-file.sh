#!/bin/zsh
#maybe you are using bash,fix the first line.
#!/bin/zsh
# Program:
#    User input filename,program will check the flowing:
#	1.) exist ? 2.) file/directory ? 3.) file permissions
#History:
#2015/xx/xx  wikinee First release

export PATH

#1.判断输入是否有字符串 
echo -e "Please input a filename, I will check the filename's type and permissions.\n\n" 
read -p "Input a filename :" filename

test -z $filename && echo "You MUST input a filename." && exit 0
#test -z string 判断是否为0，是则返回true
#test (-n) string 判断是否非空，若空字符串，反悔false
echo $filename


#2.判断文件名是否存在
test ! -e $filename && echo "True" 
#echo "The file name '$filename' DO NOT exist" && exit 0

#3.判断文件属性
test -d $filename && filetype="directory"
test -f $filename && filetype="regulare file"
test -r $filename && perm="readable"
test -w $filename && perm="$perm writeable"
test -x $filename && perm="$perm executable"

#4.开始输出
echo "The filename : $filename is $filetype"
echo "-And the permissions are : $perm"


