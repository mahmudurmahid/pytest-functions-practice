from lib.make_snippet import *

"""
the method takes a string as an argument,
returns a string
"""
def test_make_snippet_returns_string_value():
    result = make_snippet("this method returns a string")
    assert result == "this method returns a string"

"""
the method only returns the first 5 words of a string argument
"""
def test_make_snippet_returns_five_words_only():
    result = make_snippet("this method return a string even if longer than five letters")
    assert result == "this method returns a string"