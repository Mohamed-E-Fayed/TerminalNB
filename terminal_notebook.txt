This is a little project to make an interface for terminal that acts similar to jupyter notebook. 
These are the functionalities supported and their description:
1. create a new cell, 
new_cell(num, type="cell", extension="py")
This will make a new coding cell , a python file by default, of the following convention: 
        "#_type.ext". 
# 'num' in parameters->stands for the number of cell. This will sequence according to coding cells  only. That means if you insert a new cell, it's number was 5 and there was no previous text cell, it will insert a text cell under the name of 6 to support a convention of text cell explaining the upcoming code cell.
type->type of cell, either code or text or something else. 
ext, 'extension' in parameters-> the extension of file. this extension should specify in which programming language the file was written. We aim to support as much programming languages as we can in the future.

Note: the following commands assume an existing directory of specified format here 
1. run a cell
    In ipython, we should type "%load 1_cell.py".
    In terminal_nb, we could type "run_cell('1')"
