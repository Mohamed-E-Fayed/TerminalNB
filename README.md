# TerminalNB

This is a little project to provide new functions or point to some existing functions in ipython terminal session that have similar features to that of jupyter notebook. 
The only way we know, till now, for using it is to copy the source file "nb_functionalities.py" into "~/.ipython/profile_default/startup/" on Mac OS and Linux.

These are the functionalities supported and their description:
Functions on Project folder:

1. Create a new project:
create_project(name, project_type='py')
This function creates a directory in the existing "directory with name as the name of the project and the directorty. Then, it changes current directory of the process to that new directory. 
If the project already exists, it will get into the  directory of the project and update global variables code_iteration and text_iteration with the same value of the next number to be used in the code cell assuming that anyone who will write a text cell will write it before the corresponding code cell.
2. delete_project(name=None) 
Deletes the directory of the project and its contents. If a name is given, it will delete it from the parent directory, whether it is the current project or not. If name is not given, it will delete current directory and get to parent directory. 
3. create a new cell, 
	new_cell( num=-1, cell_type=CODE)
This will make a new coding cell , a python file by default, of the following convention: 
        "type-#.ext".  
cell_type->type of cell, currently supporting code, text and result cells.
num: an optional number for the cell. It is used in case the programmer would define a cell with a specific number by hand. It's default value is -1. 
4. create new code cell
ncc()
This function calls "new_cell('code')". It's no more than an appreviation. 
5. New text cell
ntc()
This function calls "new_cell('text')". It is just an appreviation.  "
6. nrc(num) 
It generates a result cell with the given number.  This result cell is just a text file. 
It is mainly used by the code itself. So, it doesn't handle existing files.


## Editing a cell:

### 1. !<command> <args> #Built-in
The first way is to use '!' to type a terminal command. It could be used with any supported command. For editing purposes, we could use it to edit a file. 
For example, assume we want to edit '1.py' using 'vim' editor. the command will be:
"!vim 1.py". 
You could use any editor installed to your system. 

### 2. %ed | %edit  #built-in magic command
It is used to edit a specific file on the go then run it just after exiting. 
To change the default text editor, add your favorite editor to the environment variables.
For example, Add the following line, to make vim as your default text editor,  to ~/.bash_profile or ~/.bashrc if bash is your default shell. If your default shell is zsh, you will add the following line to ~/.zshrc. 
```bash
export EDITOR="/usr/local/bin/vim"
```
For more help from its documentation, type "%edit?".

Note: the following commands assume an existing directory of specified format here 

### 1. run a cell 
rc(num, result_file=False) | run_cell(num, result_file=False)
We could use any of the formats to run a specific cell using its number (num). 
num: A number indicating the number of the cell to be run.
result_file(not useful in current version) : A variable to determine whether the results should be written to a file or not. It's default value is False.   

### 2. Run the entire project.
ra(result_file=True) |run_all(result_file=True) 
These functions run all the cells, in order of name, as a single script. It creates a file "all_code.py" containing all contents of the cells, then the function runs a terminal command to run this python script.  
result_file: a boolean to indicate whether to create a file containing the results or not. 

## 2. Deleting a cell. 
### 1. dc(name) | delete_cell(name)
deletes the cell of given name. 
Caution:  It actually deletes the file of given name regardless being a cell or not.  
2. dc(num, cell_type=CODE) | delete_cell(num, cell_type=CODE)
Deletes the code cell of given number (num) and optionally given cell_type.  The default cell type is 'code' cell. 

