This is a little project to make an interface for terminal that acts similar to jupyter notebook. 
These are the functionalities supported and their description:
1. Create a new project:
create_project(name, project_type='py')
This function creates a directory in the existing "directory with name as the name of the project and the directorty. Then, it changes current directory of the process to that new directory. 

2. create a new cell, 
new_cell( cell_type)
This will make a new coding cell , a python file by default, of the following convention: 
        "type_#.ext".  
The number of the cell is determined automatically after the last existing cell. e.g. if the last cell number is 'n', then it will create cell with number 'n+1'.
cell_type->type of cell, currently supporting code and text only.

3. create new code cell
ncc()
This function calls "new_cell('code')". It's no more than an appreviation. 

4. New text cell
ntc()
This function calls "new_cell('text')". It is just an appreviation.  "


Note: the following commands assume an existing directory of specified format here 
1. run a cell 
r(cell_num) | run(cell_num) 
We could use any of the formats to run a specific cell using its number. 
