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
