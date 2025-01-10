import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.loader.ui_loader import load_ui
from ui.loader.length_window import LengthWindow
from ui.loader.volume_window import VolumeWindow
from ui.loader.weight_window import WeightWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = load_ui("ui/main_window.ui") 
        self.setCentralWidget(self.ui)
        self.ui.btn_length_menu.clicked.connect(self.open_length_window)
        self.ui.btn_weight_menu.clicked.connect(self.open_weight_window)
        self.ui.btn_volume_menu.clicked.connect(self.open_volume_window)

    def open_length_window(self):
        self.length_window = LengthWindow()
        self.length_window.setGeometry(self.geometry())
        self.length_window.show()
        self.close()
    
    def open_weight_window(self):
        self.weight_window = WeightWindow()
        self.weight_window.setGeometry(self.geometry())
        self.weight_window.show()
        self.close()
    
    def open_volume_window(self):
        self.volume_window = VolumeWindow()
        self.volume_window.setGeometry(self.geometry())
        self.volume_window.show()
        self.close()
    
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()