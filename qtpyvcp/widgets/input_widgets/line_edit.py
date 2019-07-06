"""
Line Edit
---------
"""

from qtpy.QtCore import Property
from qtpy.QtWidgets import QLineEdit  # , QIntValidator, QDoubleValidator

from qtpyvcp.utilities.logger import getLogger
from qtpyvcp.widgets.base_widgets.base_widget import CMDWidget

LOG = getLogger(__name__)


class VCPLineEdit(QLineEdit, CMDWidget):
    """VCP Entry Widget"""

    DEFAULT_RULE_PROPERTY = "Text"
    RULE_PROPERTIES = CMDWidget.RULE_PROPERTIES.copy()
    RULE_PROPERTIES.update({
        'Text': ['setText', str],
    })

    def __init__(self, parent=None):
        super(VCPLineEdit, self).__init__(parent)

        self._action_name = ''
        self.input_type = "default"

        self.returnPressed.connect(self.onReturnPressed)

    def onReturnPressed(self):
        LOG.debug("Action entry activated with text: %s", self.text())

    @Property(str)
    def actionName(self):
        """The name of the action the entry should trigger.

        Returns:
            str : The action name.
        """
        return self._action_name

    @actionName.setter
    def actionName(self, action_name):
        self._action_name = action_name
        # ToDo: activate action on enter
        # bindWidget(self, action_name)

    @Property(str)
    def inputType(self):
        """The type of the inupt the entry should accept.

        Returns:
            str : The entry type.
        """
        return self._input_type

    @inputType.setter
    def inputType(self, input_type):
        self._input_type = input_type

        # if self._input_type == "integer":
        #     self.setValidator(QIntValidator())
        # elif self._input_type == "decimal":
        #     self.setValidator(QDoubleValidator())
