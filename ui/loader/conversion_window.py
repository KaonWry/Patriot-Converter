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
        
        self.ui.combo_unit_from.currentIndexChanged.connect(self.update_combo)
        self.ui.combo_unit_to.currentIndexChanged.connect(self.update_combo)

        self.ui.btn_flip.clicked.connect(self.flip)
        self.ui.btn_convert.clicked.connect(self.convert)
        self.ui.btn_convert_all.clicked.connect(self.convert_all)
        self.ui.btn_back.clicked.connect(self.open_main_window)
        
    def disable_item_by_text(self, combo_box, text):
        index = combo_box.findText(text)
        if index != -1:
            item = combo_box.model().item(index)
            if item:
                item.setEnabled(False)
    
    def enable_all_items(self, combo_box):
        for i in range(combo_box.count()):
            item = combo_box.model().item(i)
            if item:
                item.setEnabled(True)
        
    def update_combo(self):
        selected_from = self.ui.combo_unit_from.currentText()
        selected_to = self.ui.combo_unit_to.currentText()
        self.enable_all_items(self.ui.combo_unit_from)
        self.enable_all_items(self.ui.combo_unit_to)
        self.disable_item_by_text(self.ui.combo_unit_from, selected_to)
        self.disable_item_by_text(self.ui.combo_unit_to, selected_from)        
    
    def fill_dropdowns(self, unit_type):
        self.ui.combo_unit_from.clear()
        self.ui.combo_unit_to.clear()
        self.ui.combo_unit_from.addItems(unit_type)
        self.ui.combo_unit_from.setCurrentIndex(0)
        self.ui.combo_unit_to.addItems(unit_type)
        self.ui.combo_unit_to.setCurrentIndex(1)
        self.update_combo()
  
    def flip(self):
        selected_from = self.ui.combo_unit_from.currentText()
        selected_to = self.ui.combo_unit_to.currentText()
        self.enable_all_items(self.ui.combo_unit_from)
        self.enable_all_items(self.ui.combo_unit_to)
        self.ui.combo_unit_from.setCurrentText(selected_to)
        self.ui.combo_unit_to.setCurrentText(selected_from)
        self.disable_item_by_text(self.ui.combo_unit_from, selected_from)
        self.disable_item_by_text(self.ui.combo_unit_to, selected_to)

    
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