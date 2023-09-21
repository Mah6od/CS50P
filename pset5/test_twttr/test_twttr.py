from twttr import shorten


def test_assert():
    assert shorten("hello world") == "hll wrld"
    assert shorten("HELLO WORLD") == "HLL WRLD"