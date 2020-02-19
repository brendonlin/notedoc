import os
import datetime


def getDateString():
    today = datetime.datetime.today()
    dateString = datetime.datetime.strftime(today, "%Y-%m-%d")
    return dateString


def createNote(diretoryPath=None):
    dateString = getDateString()
    filename = dateString + ".md"
    if diretoryPath:
        filepath = os.path.join(diretoryPath, filename)
    else:
        filepath = filename
    if os.path.exists(filepath):
        return False
    with open(filepath, "w") as f:
        f.write("")
    return filepath
