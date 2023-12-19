from qtpy.QtWidgets import QDial
from qtpy.QtCore import Property

from qtpyvcp.actions import bindWidget
from qtpyvcp.utilities.logger import getLogger
from qtpyvcp.plugins import getPlugin


LOG = getLogger(__name__)
STATUS = getPlugin('status')


class ActionDial(QDial):
    """docstring for ActionDial."""
    def __init__(self, parent=None):
        super(ActionDial, self).__init__(parent)

        self._action_name = ''

    @Property(str)
    def actionName(self):
        """The fully qualified name of the action the dial should trigger.

        Returns:
            str : The action name.
        """
        return self._action_name

    @actionName.setter
    def actionName(self, action_name):
        """Sets the name of the action the dial should trigger.

        Args:
            action_name (str) : A fully qualified action name.
        """
        self._action_name = action_name
        bindWidget(self, action_name)

    def mousePressEvent(self, event):
        # Test for UI LOCK and consume event but do nothing if LOCK in place
        if STATUS.isLocked():
            LOG.debug('Accept mouse Press Event')
            event.accept()
            return 
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if STATUS.isLocked():
            LOG.debug('Accept mouse Release Event')
            event.accept()
            return 
        super().mouseReleaseEvent(event)

    def keyPressEvent(self, event):
        # Test for UI LOCK and consume event but do nothing if LOCK in place
        if STATUS.isLocked():
            LOG.debug('Accept keyPressEvent Event')
            event.accept()
            return 
        super().keyPressEvent(event)

    def keyReleaseEvent(self, event):
        # Test for UI LOCK and consume event but do nothing if LOCK in place
        if STATUS.isLocked():
            LOG.debug('Accept keyReleaseEvent Event')
            event.accept()
            return 
        super().keyReleaseEvent(event)
