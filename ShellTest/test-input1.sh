#!/bin/zsh
#maybe you are using bash,fix the first line.
#!/bin/zsh
# Program:
#    Programe creates three files,which named by user's input
#History:
#2015/xx/xx  wikinee First release

export PATH

#1.让用户输入文件名并取得fileuser这个变量
echo -e "I will use 'touch' command  to create 3 files. "
read -p "please input your filename:" fileuser

#2.为了避免用户随意按［Enter］，利用变量功能分析文件名设置是否有效
filename=${fileuser:-"filename"}

#3.开始利用date命令来获取文件名了
date1=$(date --date='2 days ago' +%Y%m%d)
date2=$(date --date='1 days ago' +%Y%m%d)
date3=$(date +%Y%m%d)

file1=${filename}${date1}
file2=${filename}${date2}
file3=${filename}${date3}

#4.创建文件
touch "$file1"
touch "$file2"
touch "$file3"
