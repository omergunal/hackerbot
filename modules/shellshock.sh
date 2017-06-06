#!/bin/bash

bold=$(tput bold)
normal=$(tput sgr0)

function cve_2014_6271
{
	echo "${bold}Testing $1 for CVE-2014-6271${normal}"
	env x="() { :;}; echo VULNERABLE" $1 -c "" 2>/dev/null
}

function cve_2014_7169
{
	echo "${bold}Testing $1 for CVE-2014-7169${normal}"
	rm -f echo
	env x='() { (a)=>\' $1 -c "echo echo VULNERABLE" >/dev/null 2>&1
	cat echo 2>/dev/null
	rm -f echo
}

function cve_2014_7186
{
	echo "${bold}Testing $1 for CVE-2014-7186${normal}"
	bash -c "true $(printf '<<EOF %.0s' {1..79})" > /dev/null 2>&1
	if [ $? -ne 0 ]
	then
		echo "VULNERABLE"
	fi
}

function cve_2014_7187
{
	echo "${bold}Testing $1 for CVE-2014-7187${normal}"
	$1 -c "`for i in {1..200}; do echo -n "for x$i in; do :;"; done; for i in {1..200}; do echo -n "done;";done`" 2>/dev/null
	if [ $? -ne 0 ]
	then
		echo "VULNERABLE"
	else
		echo "Test not reliable without bash being built with -fsanitize=address"
	fi
}

function shellshock_test
{
	cve_2014_6271 "$1"
	cve_2014_7169 "$1"
	cve_2014_7186 "$1"
	cve_2014_7187 "$1"
}

for path in ${PATH//:/ }
do
	if [ -f "$path/sh" ]
	then
		shellshock_test "$path/sh"
		echo
	fi
	if [ -f "$path/bash" ]
	then
		shellshock_test "$path/bash"
		echo
	fi
done
