"""
TouchFakeLineEdit
--------

"""
from qtpy.QtCore import Slot
from qtpy.QtWidgets import QLabel

from qtpyvcp.widgets import VCPWidget
from qtpyvcp.widgets.base_widgets.dro_base_widget import DROBaseWidget


class TouchFakeLineEdit(QLabel, VCPWidget):

    def __init__(self, parent=None):
        super(TouchFakeLineEdit, self).__init__(parent)
