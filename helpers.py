from pathlib import Path

def absPath(self):
    return str(Path(__file__).parent.absolute() / file)