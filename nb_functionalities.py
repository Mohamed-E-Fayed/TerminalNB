#This module aims to  implement main functionalities  the notebook  should support. 
import os

#Global variables 
iteration = int()
project_name = str()
project_language = str('py')
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
        iteration =  1 
        project_name = name 
        project_language = proj_lang 
        os.makedirs(name) 
        os.system('cd ' + name)
    except OSError:
        if OSError.errno == errno.EXIST:
            print('Folder already exist. We will  continue adding to it')
            iteration = 1 # to be updated 
            os.system('cd ' + name)
        else:
            print('Error: Can not  create folder.') 
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
    os.mknod(str(cell_type + DASH + str(iteration) + DOT + project_language))
    iteration +=1 

# create new code cell
def ncc():
    new_cell(CODE)

# create new text cell 
def ntc():
    new_cell(TEXT) 



    #main 
    os.system('ipython') 
