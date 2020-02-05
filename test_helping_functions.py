from .helping_functions import * 

def test_get_cel_name():
    assert get_cell_name(4) ==  str(4) + '.py'
    assert get_cell_name(2) == '2-z.py'

def test_get_iteration():
    assert get_iteration() ==3 

