#This module aims to  implement main functionalities  the notebook  should support. 
import os
import shutil 
from pathlib import Path 
from functools import singledispatch 
import threading 

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

def open_project(name):
    """
    This function just changes the directory to be inside the project. 
    """ 
    os.chdir(name)

#create new cell 
def new_cell(name=None, cell_type=CODE, num=-1, extension='py'): 
    """
    Function to create a new cell. It assumes that the programmer would insert text cell before a code cell to describe the content of the cell. 
    Regarding result cells, it just create a cell with the given code cell number. 
    """
    global code_iteration 
    global text_iteration 
    global project_name  
    global project_language
    global supported_cell_types  
    cell_type = cell_type.lower() 
    if not cell_type in supported_cell_types: 
        print('This type of cells is not supported')
        return 
    #if num is given, create a cell of this number and return.
    if num == -1:
        code_iteration = get_iteration()
        num = code_iteration
    else:
        Path(get_cell_name(num, name,cell_type, extension)).touch()
        print(get_cell_name(num, name,cell_type, extension) + ' file has been created') 
        return 
    cell_name = get_cell_name(num, name, cell_type, extension) 
    if os.path.isfile(cell_name):
        reply = input('This file already exists. Would you like to replace it with a new one?(y/n) \n').lower()
        if reply=='y':
            os.remove(cell_name)
            Path(cell_name).touch()
            print(cell_name +  ' file has been created')
        elif reply =='n':
            return 
    
    if cell_type == CODE:
        Path(cell_name).touch() #code cells is the default.
        print(cell_name +  ' file has been created') 
        code_iteration +=1 
        text_iteration = code_iteration + 1
    elif cell_type == TEXT:
        Path(get_cell_name(text_iteration, name, cell_type, extension)).touch()
        print(get_cell_name(text_iteration, name, cell_type, extension) + ' file has been created')
        text_iteration +=1 
        code_iteration =text_iteration
    elif cell_type == RESULT: 
        Path(get_cell_name(code_iteration, name, cell_type, extension)).touch() 
        print(get_cell_name(code_iteration, name, cell_type, extension) + ' file has been created')

# create new code cell
def ncc( name=None, num=-1):
    """
    This function creates a new code cell
    """
    new_cell(num=num, name=name, cell_type=CODE, extension=PY)

# create new text cell 
def ntc( name=None, num=-1):
    """
    This function creates a new text cell
    """
    new_cell(num=num, name=name, cell_type=TEXT, extension=TXT) 

def nrc(num=None):
    """
    This function creates a new results cell.
    """
    if num is None:
        print('This function must have an input number')
        return 
    new_cell(cell_type=RESULT, num=num, extension=RES)

#running cells  
#The functions of running cells independently are  implemented in nb_functionalities.ipy
def run_all(result_file=True): 
    """ 
    This function runs all the code cells in the project directory. It's algorithm is very basic to make sure everything works well. It may be updated later.
    The algorithm:
    1. Open all code cells in sequence and merge all of them into a big file. 
    2. This file is executed normally using run_cell() function.
    """ 
    global commands 
    global extensions 
    global RES 
    ALL_CODE = 'all_code.' + extensions[0]
    ALL_RESULTS = 'all_results.' + RES
    files = os.listdir() 
    files = [f for f in files if f[0].isdigit() and  f.find(DOT + extensions[0])!= -1] 
    files.sort() 
    code = str()
    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines() 
            for line in lines:
                code = code + line
            code = code + ENDL
    
    with open(ALL_CODE, 'w' ) as f:
        f.write(code)
    
    if result_file==True :
        os.system(str(commands[0] + SPACE + ALL_CODE + GREATER_THAN + ALL_RESULTS))
    else:
        os.system(str(commands[0] + SPACE + ALL_CODE))  

def ra(result_file=False):
    """
    This function is an appreviation for run_all() function
    """
    run_all(result_file)

#Functions to delete project and cells. 
def delete_project(name= None):
    """
    This function deletes the project folder.
    """ 
    if name == None:
        name = os.getcwd() 
        name = name[name.rfind(SLASH)+1:] 
    os.chdir(DOT + DOT+ SLASH)
    shutil.rmtree(name)

@singledispatch 
def delete_cell(num, cell_type=CODE): 
    """
    This function deletes the cell of given number and type. It assumes the default value of cell_type is 'code'
    """
    os.remove(str(get_cell_name(num, cell_type = cell_type)))

@delete_cell.register(str)
def _(name):
    """
    This function deletes a cell of given name or number and type. 
    """ 
    os.remove(name)


@singledispatch 
def dc(num, cell_type=CODE):
    delete_cell(num, cell_type) 

@dc.register(str)
def _(name):
    delete_cell(name) 
