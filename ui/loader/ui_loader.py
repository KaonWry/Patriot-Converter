from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

def load_ui(ui_file):
    file = QFile(ui_file)
    file.open(QFile.ReadOnly)
    
    loader = QUiLoader()
    window = loader.load(file)
    return window