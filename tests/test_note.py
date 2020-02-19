import os
from notedoc import note


def test_createNote():
    filepath = newnote.createNote()
    assert filepath is not None
    os.remove(filepath)
