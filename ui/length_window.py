from PySide6.QtWidgets import QMainWindow
from ui.ui_loader import load_ui

class LengthWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = load_ui("ui/length_window.ui") 
        self.setCentralWidget(self.ui)
        