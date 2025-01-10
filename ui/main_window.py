import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_loader import load_ui
from ui.length_window import LengthWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = load_ui("ui/main_window.ui") 
        self.setCentralWidget(self.ui)

        self.ui.btn_length_menu.clicked.connect(self.open_length_window)

    def open_length_window(self):
        self.length_window = LengthWindow()
        self.length_window.show()
        self.close()
    
    def open_weight_window(self):
        print("")
    
    def open_volume_window(self):
        print('')
    
        
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()