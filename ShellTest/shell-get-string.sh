#!/bin/sh

has_cn()
{
	localeFile="/etc/plymouth/locale"
	if [ ! -f $localeFile ]; then
		echo 1
	else
		locale_value=$(grep -e '^LANG=' $localeFile | sed -e 's/LANG=\|\"//g')
		zh_cn="zh_CN.UTF-8"
		# en_us="en_US.UTF-8"
		if [ "$locale_value" = "$zh_cn" ]; then
			echo 0
		else
			echo 1
		fi
	fi
}

test_func()
{
	ret=$(has_cn)
	echo "$ret"

	if [ "$ret" -eq 0 ]; then
		echo "locale is Chinese"
	else
		echo "locale is Not Chinsse"
	fi
}

test_func
