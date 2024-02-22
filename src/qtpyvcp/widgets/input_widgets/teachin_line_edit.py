"""
TeachInLineEdit
--------

"""
from qtpy.QtCore import Slot
from qtpy.QtWidgets import QLineEdit

from qtpyvcp.widgets.base_widgets.dro_base_widget import DROBaseWidget


class TeachInLineEdit(QLineEdit, DROBaseWidget):

    def __init__(self, parent=None):
        super(TeachInLineEdit, self).__init__(parent)
        self.current_value = 0

    def setValue(self, value):
        self.current_value = float(value)

    @Slot()
    def fillWithCurrentValue(self):
        self.setText(str(self.current_value))
