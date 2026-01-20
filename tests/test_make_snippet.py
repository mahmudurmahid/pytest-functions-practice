from lib.make_snippet import *

"""
the method takes a string as an argument,
returns a string
"""
def test_make_snippet_returns_string_value():
    result = make_snippet("this method does return a string")
    assert result == "this method does return a string"