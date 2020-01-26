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
    global project_name 
    global supported_cell_types  
    cell_type = cell_type.lower() 
    if not cell_type in supported_cell_types: 
        print('This type of cells is not supported')
        return 
    if cell_type == CODE:
        Path(str(CODE + DASH + code_iteration + DOT + project_language))  
        code_iteration +=1 
        text_iteration = code_iteration + 1
    elif cell_type == TEXT:
        Path(str(TEXT+ DASH + text_iteration + DOT + project_language))  
        text_iteration +=1 
        code_iteration =text_iteration
    elif cell_type == RESULT: 
        Path(str(RESULT + DASH + code_iteration + DOT + project_language )).touch()

# create new code cell
def ncc():
    new_cell(CODE)

# create new text cell 
def ntc():
    new_cell(TEXT) 

#running cells 
def run_cell(num):
    os.system(str(commands[programming_language] + SPACE + get_cell_name(num)))

def r(num):
    run_cell(num)

