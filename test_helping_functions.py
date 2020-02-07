from helping_functions import * 

def test_get_cell_num():
    assert  get_cell_num('5.py') == 5
    assert get_cell_num('4-xe.py')== 4
    assert get_cell_num('re.py') == -1 
    assert get_cell_num(54gf') == -1 

def test_get_cel_name():
    assert get_cell_name(4) ==  str(4) + '.py'
    assert get_cell_name(2) == '2-z.py'

def test_get_iteration():
    assert get_iteration() ==3 

