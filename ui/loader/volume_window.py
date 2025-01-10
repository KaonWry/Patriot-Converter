from PySide6.QtWidgets import QMainWindow
from ui.loader.ui_loader import load_ui
from logics.converter import convert_unit, convert_all_unit

class VolumeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = load_ui("ui/volume_window.ui") 
        self.setCentralWidget(self.ui)
        
        self.ui.btn_flip.clicked.connect(self.flip)
        self.ui.btn_convert.clicked.connect(self.convert)
        self.ui.btn_convert_all.clicked.connect(self.convert_all)
        self.ui.btn_back.clicked.connect(self.open_main_window)
        
    def flip(self):
        unit_from_index = self.ui.combo_unit_from.currentIndex()
        unit_to_index = self.ui.combo_unit_to.currentIndex()

        self.ui.combo_unit_from.setCurrentIndex(unit_to_index)
        self.ui.combo_unit_to.setCurrentIndex(unit_from_index)
    
    def open_main_window(self):
        from ui.loader.main_window import MainWindow
        self.main_window = MainWindow()
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.close()
        
    def convert(self):
        try:
            amount = float(self.ui.txt_amount.text())
            unit_from = self.ui.combo_unit_from.currentText()
            unit_to = self.ui.combo_unit_to.currentText()
            result = convert_unit('volume', amount, unit_from, unit_to)
            self.ui.lbl_result.setText(result)
        except ValueError:
            self.ui.lbl_result.setText("Please enter a valid number.")
        
    def convert_all(self):
        try:
            amount = float(self.ui.txt_amount.text())
            unit_from = self.ui.combo_unit_from.currentText()
            result = convert_all_unit('volume', amount, unit_from)
            self.ui.lbl_result.setText(result)
        except ValueError:
            self.ui.lbl_result.setText("Please enter a valid number.")