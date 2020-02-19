#This module have the global variables.
# I added the enum of the programming languages here to make that the person who modifies the list of programming languages  updates the commands dictionary. 
import os 
from enum import Enum 

code_iteration = int(-1)
text_iteration = int(-1)
project_name = str()
project_language= str('py') 
project_path = os.getcwd()
preferred_text_editor = str()

class ProgrammingLanguages(Enum):
    py3 = 0
    py2 = 1
    c = 2
    cpp = 3 


commands = {0:'python3', 1:'python', 2:'gcc', 3:'g++'} 
extensions = {0: 'py', 1:'py', 2:'c', 3:'cpp', -1:'txt'}
