#This module aims to  implement main functionalities  the notebook  should support. 
import os
from pathlib import Path
from helping_functions import * 
from constants import *
from variables import * 

# create new project 
def create_project(name, proj_lang ='py'): 
    try:
        global code_iteration
        global text_iteration 
        global project_name 
        global project_language 
        global project_path 
        code_iteration =  1 
        text_iteration = 1
        project_name = name 
        project_language = proj_lang 
        os.makedirs(name) 
        os.chdir(str(project_path + SLASH + project_name + SLASH)) 
    except OSError:
        os.chdir(project_path + SLASH + name +SLASH )
        print('This project already exists, we will continue in it') 
        code_iteration = get_iteration(CODE)
        text_iteration = code_iteration 
        raise

#create new cell 
def new_cell(cell_type): 
    """
    Function to create a new cell. It assumes that the programmer would insert text cell before a code cell to describe the content of the cell. 
    """
    global code_iteration 
    global text_iteration 
    global preferred_text_editor  
    global project_name 
    global supported_cell_types 
    if not cell_type.lower() in supported_cell_types: 
        print('This type of cells is not supported')
        return 
    Path(str(get_cell_name(iteration, cell_type=cell_type))).touch() 
    if cell_type == CODE:
        code_iteration +=1 
        text_iteration = code_iteration + 1
    elif cell_type == TEXT:
        text_iteration +=1 
        code_iteration =text_iteration

# create new code cell
def ncc():
    """
    This function creates a new code cell
    """
    new_cell(CODE)

# create new text cell 
def ntc():
    """
    This function creates a new text cell
    """
    new_cell(TEXT) 

def nrc():
    """
    This function creates a new results cell.
    """
    new_cell(RESULT)

#running cells 
def run_cell(num):
    global ProgrammingLanguages 
    global commands 
    os.system(str(commands[ProgrammingLanguages(get_cell_programming_language(num))] + SPACE + get_cell_name(num))) 
    return 1 # indicate correct exit 

def rc(num):
    return run_cell(num)

