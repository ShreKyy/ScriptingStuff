#!/bin/bash
#https://medium.com/@patelkathan22/beginners-guide-on-how-you-can-use-javascript-in-bugbounty-492f6eb1f9ea
#Made off of the above article ^^^ to automate finding information disclosure in javascript files while doing bug bounties
#also made it a bit nicer lol 
#Made By ShreKy --> https://github.com/ShreKyy
		
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
Black='\033;[0;30m'

now=$(date)
targetPath=$1
target="https://"$targetPath

printf "${BLUE}[!]Starting to gather JS Files @ ${RED}$now...\n"

mkdir EnumJS && cd EnumJS && mkdir $targetPath && cd $targetPath
echo $target | gau | grep ".js$" | uniq | sort >> JS_links.txt 
printf "${GREEN}[!]Gathered JS links\n"
echo $target | subjs >> JS_links.txt
printf "${BLUE}[*]Gathering the live JS links...\n"
cat JS_links.txt | hakcheckurl | grep "200" | cut -d" " -f2 | sort -u > Live_JS_links.txt
printf "${GREEN}[!]Gathered the live JS links\n"
printf "${BLUE}[*]Running LinkFinder against them...\n"
cat Live_JS_links.txt | while read url;do python3 /opt/LinkFinder/linkfinder.py -d -i $url -o cli ; done > Endpoints.txt #Change the path to linkfinder.py
printf "${GREEN}[!]Finished running LinkFinder against them\n"

printf "${RED}[!]You can now grep for sensitive endpoints (ex. grep admin)\n"

printf "${BLUE}[*]Running SecretFinder against them...\n"
cat Live_JS_links.txt | while read url;do python3 /opt/SecretFinder/SecretFinder.py -i $url -o cli >> JS_Secrets.txt ; done #Change the path to SecretFinder.py
printf "${GREEN}[!]Finished running SecretFinder against them\n"

printf "${BLUE}[*]Collecting the JS files locally...\n"
mkdir jsfiles 
cp Live_JS_links.txt jsfiles/hosts
cd jsfiles
meg -d 1000 -v /
printf "${GREEN}[!]Done,you can now find them in'EnumJS/$targetPath/jsfiles'\n" 
