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
<<<<<<< HEAD
=======
    Path(str(get_cell_name(iteration, cell_type=cell_type))).touch() 
>>>>>>> 9fc7591e3c930ca28dc39a550c4744cd50f3989e
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
def run_cell(num, result_file=True):
    """
    This function is used to run code cell with given number. The result_file variable is used to indicate whether to print the output into console ,if False, or print it into a file, if True. 
    This function is working only with python3. It needs to be updated for supporting other programming languages. 
    """
    global ProgrammingLanguages 
    global commands  
    global extensions 
    if result_file == True:
        os.system(str(ECHO + SPACE + commands[0] + SPACE + get_cell_name(num, cell_type=CODE, extension=extensions[0]) + SPACE + GREATER_THAN + get_cell_name(num, cell_type=RESULT, extension=extensions[-1])))
            else:
        os.system(str(commands[0] + SPACE + get_cell_name(num, cell_type=CODE, extension=extensions[0]))) 
    return 1 # indicate correct exit 

def rc(num, result_file=True):
    return run_cell(num, result_file=result_file)

def run_all(): 
    """ 
    This function runs all the code cells in the project directory.
    """
    global project_language 
    files = os.listdir() 
    files = [f for f in files if f.find(project_language) != -1]
    files = files.sort() 
    for file in files:
        os.system(commands[project_language] + SPACE + file) #continue 

