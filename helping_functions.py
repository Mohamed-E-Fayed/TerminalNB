#Some functions to be used in other modules 
import os 
from constants  import *
from variables import * 

def get_extension(cell_type):
    """
    This function returns the extension corresponding to given cell type
    """
    extension=str()
    if cell_type == CODE:
        extension=project_language
    elif cell_type == TEXT:
        extension=RES
    elif cell_type == RESULT:
        extension=RES
    return extension 

def get_cell_num(name):
    """
    This function returns the number of cell mentioned from its name. It is used to extract numbers from complicated cell names. 
    It assumes that the cell number is at its  beginning before the first  '-' or '.'. 
    """
    num = str()
    if name[0].isdigit() :
        if name.find(DASH) != -1 :
            num = name[:name.find(DASH)] 
        elif name.find(DOT) !=-1: 
            num = name[:name.find(DOT)]
        else:
            print('Error: Invalid file name')

    if not num.isdigit():
        num = -1
    return int(num) 

def get_cell_name(num, cell_type=CODE, extension='py'):
    """ 
    This function returns the name corresponding to the given number
    """
    name = str(str(num) + DOT + extension) 
    files = os.listdir() 
    files = [f for f in files if f.find(extension[0])!=-1 and f[0].isdigit()]

    for file in files:
        number = get_cell_num(file)
        if num == number:
            name = file
            break
    return name

def get_iteration(cell_type='code'): 
    """
    This function returns the number of iteration should be used in the upcoming code or text cell to be created. e.g. if the last cell has the number of 'n', then it should return 'n+1' to be used as the number of the next cell when creating it.
    """

    global extensions 
    itr=0
    files= os.listdir()
    files = [f for f in files if f[0].isdigit()]

    if cell_type == CODE:
        files = [s for s in files if extensions[0] == s[s.rfind(DOT)+1:]]
    elif cell_type == TEXT:
        files = [s for s in  files if TXT == s[s.rfind(DOT)+1:]]

    print(files)
    files.sort() 
    itr = get_cell_num(files[-1]) + 1
    print(itr) 
    return itr


def get_cell_programming_language(num):
    """
    This function returns the number of programming language of the cell. 
    """
    extension = str()
    files = os.listdir() 
    for file in files:
        if file.find(str(num)) != -1: 
            extension = file[:file.find(DOT)] 
    cmdlst = list()
    for key, value in commands.itritems():
        cmdlst.append(value) 
    return cmdlst.index(extension) 
