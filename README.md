# LinuxDictionary  
Using API to create easy access to a dictionary from terminal/shell in Linux  

1. Open dict.sh  
2. Change the *path* in the file with the *path of your python file*
3. Add *export set PATH=$PATH:/yourpath* in the end of your .bashrc file (in home directory) replacing yourpath by the path to your directory where dict.sh lies   
4. Add *alias dict='dict.sh'* in the end of your *.bashrc* file  
5. make dict.sh executable by typing *chmod u+x dict.sh*  
6. Type _dict yourword_ and results will be printed


Edit: if this doesn't work, write ./dict.sh instead of dict.sh in alias in point 4.
