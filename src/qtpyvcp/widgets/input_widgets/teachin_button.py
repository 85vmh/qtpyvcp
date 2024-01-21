"""
TeachInButton
--------

"""

from qtpy.QtWidgets import QPushButton
from qtpy.QtCore import Slot, Property, Signal

from qtpyvcp.widgets.base_widgets.dro_base_widget import DROBaseWidget


class TeachInButton(QPushButton, DROBaseWidget):
    """TeachInButton
    """
    currentValue = Signal(float)

    def __init__(self, parent=None):
        super(TeachInButton, self).__init__(parent)
        self.current_value = 0
        self.clicked.connect(lambda: self.currentValue.emit(self.current_value))

    def setValue(self, value):
        self.current_value = float(value)
