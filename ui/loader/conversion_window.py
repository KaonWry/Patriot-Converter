from PySide6.QtWidgets import QMainWindow
from ui.loader.ui_loader import load_ui
from logics.converter import get_units, convert_unit, convert_all_unit

class ConversionWindow(QMainWindow):
    def __init__(self, unit_type):
        super().__init__()
        self.ui = load_ui("ui/conversion_window.ui") 
        self.setCentralWidget(self.ui)
        
        self.unit_type = unit_type
        self.units = get_units(unit_type)
        self.fill_dropdowns(self.units)
        
        self.ui.combo_unit_from.currentIndexChanged.connect(lambda: self.update_combo(self.ui.combo_unit_from, self.ui.combo_unit_to))
        self.ui.combo_unit_to.currentIndexChanged.connect(lambda: self.update_combo(self.ui.combo_unit_to, self.ui.combo_unit_from))

        self.ui.btn_flip.clicked.connect(self.flip)
        self.ui.btn_convert.clicked.connect(self.convert)
        self.ui.btn_convert_all.clicked.connect(self.convert_all)
        self.ui.btn_back.clicked.connect(self.open_main_window)
    
    def fill_dropdowns(self, unit_type):
        self.ui.combo_unit_from.clear()
        self.ui.combo_unit_to.clear()
        self.ui.combo_unit_from.addItems(unit_type)
        self.ui.combo_unit_to.addItems(unit_type)        
        self.update_combo_unit_to()

    def update_combo(self, combo_change, combo_keep):
        selected_change = combo_change.currentText()
        selected_keep = combo_keep.currentText()
        combo_keep.blockSignals(True)
        combo_keep.clear()
        combo_keep.addItems([unit for unit in self.units if unit != selected_change])
        combo_keep.setCurrentText(selected_keep)
        combo_keep.blockSignals(False) 
                    
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
            result = convert_unit(self.unit_type, amount, unit_from, unit_to)
            self.ui.lbl_result.setText(result)
        except ValueError:
            self.ui.lbl_result.setText("Please enter a valid number.")
        
    def convert_all(self):
        try:
            amount = float(self.ui.txt_amount.text())
            unit_from = self.ui.combo_unit_from.currentText()
            result = convert_all_unit(self.unit_type, amount, unit_from)
            self.ui.lbl_result.setText(result)
        except ValueError:
            self.ui.lbl_result.setText("Please enter a valid number.")