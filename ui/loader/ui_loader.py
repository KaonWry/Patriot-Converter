import os
import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.abspath(relative_path)

def load_ui(ui_file):
    file_path = resource_path(ui_file)  
    file = QFile(file_path)
    file.open(QFile.ReadOnly)
    
    loader = QUiLoader()
    window = loader.load(file)
    file.close()
    return window