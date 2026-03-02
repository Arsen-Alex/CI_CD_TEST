from main import add, add2

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0

def test_add2():
    assert add2(2, 3) == 6
    assert add2(0, 0) == 0