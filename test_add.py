from add import add


def test_add():
    assert add(2, 3) == 5
    assert add(2, 4) == 6
    assert add(1, -1) == 0
