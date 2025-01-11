import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.loader.ui_loader import load_ui
from ui.loader.conversion_window import ConversionWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = load_ui("ui/main_window.ui") 
        self.setCentralWidget(self.ui)
        self.ui.btn_length_menu.clicked.connect(lambda: self.open_conversion_window('length'))
        self.ui.btn_weight_menu.clicked.connect(lambda: self.open_conversion_window('weight'))
        self.ui.btn_volume_menu.clicked.connect(lambda: self.open_conversion_window('volume'))
        
    def open_conversion_window(self, unit_type):
        self.conversion_window = ConversionWindow(unit_type)
        self.conversion_window.setGeometry(self.geometry())
        self.conversion_window.show()
        self.close()
    
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()