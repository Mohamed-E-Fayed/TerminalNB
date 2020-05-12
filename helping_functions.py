# This file contains either functions to
# help in editing (i.e. utility functions) e.g. where_is(string) 
# or some functions to be used in other modules e.g. get_cell_name(args)
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

def get_cell_name(num, name=None, cell_type=CODE, extension='py'):
    """ 
    This function returns the name corresponding to the given number
    """ 
    if name: 
        #It should be updated in the future.
        return str(str(num) + DASH + name + DOT + extension) 
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
    
    if files:
        files.sort() 
        itr = get_cell_num(files[-1]) 
    return int(itr+1)


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

def organize_cells():
    """
    This functions  organize the cells numbers in case   it  became unordered according to numbers due to delete, adding a cell in different place, ...etc. 
    """
    files = os.listdir()
    files = [f for f in files if extensions[0] in f]
    files.sort() 

    itr = 0 
    for file in files:
        itr +=1 
        if not  str(itr) in file:
            if file.find(DASH) !=-1:
                file[:file.find(DASH)] = str(itr)
            elif file.find(DOT)!= -1:
                file[:file.find(DOT)] = str(itr)  
    #continue 
    # make sure to update files names and to handle corresponding text cells. 


def where_is(string):
    """
    This function is used to search for a specific string in all projects files.
    """
    files=[f for f in os.listdir() if 'py' in f or 'txt' in f]
    if len(files)==0:
        print('empty directory')
        return 
    for file in files:
        exists=False
        print('In file : ', file)
        with open(file, 'r') as f:
            lines = f.read().split('\n')
            for line in lines:
                if string in line:
                    exists=True
                    print(lines.index(line), ' ', line)
        if not exists:
            print('This file does not contain {}'.format(string))

def whereis(string):
    """
    another naming for where_is(string)
    """
    where_is(string)

def ws(string):
    """
    appreviation for where_is(string)
    """
    where_is(string)
