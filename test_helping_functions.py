from .helping_functions import * 

def test_get_cel_name():
    assert get_cell_name(4) == 'code-' + str(4) + '.py'

def test_get_iteration():
    assert get_iteration() == 20

