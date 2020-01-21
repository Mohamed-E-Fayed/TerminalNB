#This module aims to  implement main functionalities  the notebook  should support. 
import os
from pathlib import Path

#Global variables 
iteration = int()
project_name = str()
project_language = str('py') 
project_path = os.getcwd()
preferred_text_editor = str() 

#constants 
SPACE = ' '
SLASH = '/' 
DOT = '.'
DASH = '-'
CODE = 'code'
TEXT='text'
supported_cell_types = [CODE, TEXT] 


# create new project 
def create_project(name, proj_lang ='py'): 
    try:
        global iteration
        global project_name 
        global project_language 
        global project_path 
        iteration =  1 
        project_name = name 
        project_language = proj_lang 
        os.makedirs(name) 
        os.chdir(str(project_path + SLASH + project_name + SLASH)) 
    except OSError:
        os.chdir(project_path + SLASH + name +SLASH )
        print('This project already exists, we will continue in it') 
        raise

#create new cell 
def new_cell(cell_type):
    global iteration 
    global preferred_text_editor  
    global project_name 
    global supported_cell_types 
    if not cell_type.lower() in supported_cell_types: 
        print('This type of cells is not supported')
        return 
    Path(str(cell_type + DASH + str(iteration) + DOT + project_language)).touch() 
    iteration +=1 

# create new code cell
def ncc():
    new_cell(CODE)

# create new text cell 
def ntc():
    new_cell(TEXT) 



