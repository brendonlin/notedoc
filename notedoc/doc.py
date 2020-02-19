import os
import argparse
import re


def cleanDoc(text):
    newText = text[:]
    cases = [
        (r"\s+\（\d+\）", " "),
        (r"&quot;", "**"),
        (r"\d+\、", "#### "),
        (r"\s+\（[一二三四五六七八九十]+\）", "#### ")
    ]
    for pattern, repl in cases:
        newText = re.sub(pattern, repl, newText)
    return newText


def format(fp):
    name, ext = fp.split(".")
    newfp = ".".join([name+"_copy", ext])
    with open(fp, "r") as f:
        text = f.read()
    newText = cleanDoc(text)
    with open(newfp, "w") as f:
        f.write(newText)
