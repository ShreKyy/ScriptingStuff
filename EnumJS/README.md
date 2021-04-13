# EnumJS  
This tool is meant to automate gathering JavaScript files to find information disclosure while doing Bug Bounties  
It is made off of this article --> https://medium.com/@patelkathan22/beginners-guide-on-how-you-can-use-javascript-in-bugbounty-492f6eb1f9ea  
It's just put together so you dont have to type it over and over again  
lol

# Requirements

For this to work you will need a couple of tools:  
-**gau** --> https://github.com/lc/gau  
-**meg** --> https://github.com/tomnomnom/meg  
-**subjs** --> https://github.com/lc/subjs  
-**hakcheckurl** --> https://github.com/hakluke/hakcheckurl  
-**LinkFinder** --> https://github.com/GerbenJavado/LinkFinder  
-**SecretFinder** --> https://github.com/m4ll0k/SecretFinder 

# Usage  
Simply compile the script with `chmod +x EnumJS.sh` or run it directly with `bash`.  
Run the script with the first argument being your target **without** the protocol(http/https), like so:  
``./EnumJS.sh www.example.com`` / ``bash EnumJS.sh www.example.com``  
After the script finishes the output will be saved in current directory --> *EnumJS/www.example.com/*  
Also change the path of LinkFinder and SecretFinder in the script to where you have them installed (default is the /opt folder).  
