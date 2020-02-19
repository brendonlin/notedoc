import os
import argparse
from . import doc
from . import note


def main():
    parser = argparse.ArgumentParser("notedoc")
    parser.add_argument("action", choices=["newnote", "format"])
    parser.add_argument("-p", "--path")
    args = parser.parse_args()
    action = args.action
    path = args.path
    if action == "newnote":
        note.createNote(path)
    elif action == "format":
        if path:
            doc.format(path)
        else:
            print("Need a file path to format")
