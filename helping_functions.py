#Some functions to be used in other modules 
import os 
from constants  import *

def get_cell_name(num, cell_type=CODE, extension='py'):
    """ 
    This function returns the name corresponding to the given number
    """
    return str(cell_type + UNDERSCO + str(num) + DOT + extension)
def get_iteration(cell_type='code'): 
    """
    This function returns the number of iteration should be used in the upcoming code or text cell to be created. e.g. if the last cell has the number of 'n', then it should return 'n+1' to be used as the number of the next cell when creating it.
    """

    itr=0
    everything_in_directory = os.listdir()
    files = [s for s in everything_in_directory if '.' in s]
    for file in files:
        if any(char.isdigit() for char in file):
            if file[0:4] == cell_type:
                temp = file[file.find(DASH)+1:] 
                temp = temp[:temp.find(DOT)] 
                if temp.find(DASH) != -1:
                    temp = temp[:temp.find(DASH)]
                int_temp = int(temp)
                if int_temp > itr: 
                    itr = int_temp + 1

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
