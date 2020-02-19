from notedoc import doc


def test_cleanDoc():
    with open("tests/data/rawdoc.md", "r") as f:
        text = f.read()
    newText = doc.cleanDoc(text)
    with open("tests/data/rawdocResult.md", "w") as f:
        f.write(newText)
