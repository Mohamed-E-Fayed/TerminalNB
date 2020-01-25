#This module have the global variables.
# I added the enum of the programming languages here to make that the person who modifies the list of programming languages  updates the commands dictionary. 
import os 
from enum import Enum 

code_iteration = int()
text_iteration = int()
project_name = str()
project_path = os.getcwd()
preferred_text_editor = str()

class ProgrammingLanguages(Enum):
    py3 = 0
    py2 = 1
    c = 2
    cpp = 3 


commands = {0:'python3', 1:'python', 2:'gcc', 3:'g++'} 

#convert the commands into a list to be used if needed 
cmdlst = list() 
for key, value in commands.itritems():
    cmdlst.append(value)
