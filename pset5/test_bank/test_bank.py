from bank import value

def test_greeting():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("How you doing?") == 20
    assert value("What's happening?") == 100