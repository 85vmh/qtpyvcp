#   Copyright (c) 2018 Kurt Jacobson
#      <kurtcjacobson@gmail.com>
#
#   This file is part of QtPyVCP.
#
#   QtPyVCP is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 2 of the License, or
#   (at your option) any later version.
#
#   QtPyVCP is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with QtPyVCP.  If not, see <http://www.gnu.org/licenses/>.

from qtpy.QtCore import Qt, Slot, Property
from qtpy.QtGui import QColor
from qtpy.QtWidgets import QWidget, QBoxLayout, QSizePolicy

from qtpyvcp.utilities.settings import setSetting
from qtpyvcp.widgets.button_widgets.led_button import LEDButton
from qtpyvcp import SETTINGS


class JogSpeedPercentageWidget(QWidget):

    def __init__(self, parent=None, standalone=False):
        super(JogSpeedPercentageWidget, self).__init__(parent)

        self._container = hBox = QBoxLayout(QBoxLayout.LeftToRight, self)

        hBox.setContentsMargins(0, 0, 0, 0)
        self._setting_name = 'rapid_speeds.percentage'
        self._ledDiameter = 15
        self._ledOnColor = QColor('green')
        self._ledOffColor = QColor('gray')
        self._alignment = Qt.AlignTop | Qt.AlignRight
        # This prevents doing unneeded initialization when QtDesginer loads the plugin.
        if parent is None and not standalone:
            return

        self._setting = SETTINGS.get(self._setting_name)

        value = self._setting.getValue()
        percentages = self._setting.enum_options

        for percentage in percentages:
            button = LEDButton()

            button.setCheckable(True)
            button.setAutoExclusive(True)
            button.setFocusPolicy(Qt.NoFocus)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            button.setMinimumSize(50, 42)

            is_on = percentage == value

            if percentage != 0:
                button.setText(f"{percentage}%")
                button.setProperty("percentage", percentage)
                button.clicked.connect(self.setJogSpeedPercentage)
                hBox.addWidget(button)
                button.setLedColor(self._ledOnColor if is_on else self._ledOffColor)

    def setJogSpeedPercentage(self):
        current_percentage = self.sender().property("percentage")
        setSetting('machine.jog.linear-speed-percentage', current_percentage)
        setSetting('rapid_speeds.percentage', current_percentage)
        self.updateLeds(current_percentage)

    def updateLeds(self, current_percentage):
        for w in (self._container.itemAt(i) for i in range(self._container.count())):
            percentage_value = w.widget().property("percentage")
            is_on = current_percentage == percentage_value
            w.widget().setLedDiameter(self._ledDiameter)
            w.widget().setLedColor(self._ledOnColor if is_on else self._ledOffColor)
            w.widget().setAlignment(self._alignment)

    def getLedDiameter(self):
        return self._ledDiameter

    @Slot(int)
    def setLedDiameter(self, value):
        self._ledDiameter = value

    def getLedOnColor(self):
        return self._ledOnColor

    @Slot(QColor)
    def setLedOnColor(self, value):
        self._ledOnColor = value

    def getLedOffColor(self):
        return self._ledOffColor

    @Slot(QColor)
    def setLedOffColor(self, value):
        self._ledOffColor = value

    def getAlignment(self):
        return self._alignment

    @Slot(Qt.Alignment)
    def setAlignment(self, value):
        self._alignment = Qt.Alignment(value)

    def getOrientation(self):
        if self._container.direction() == QBoxLayout.LeftToRight:
            return Qt.Horizontal
        else:
            return Qt.Vertical

    @Slot(Qt.Orientation)
    def setOrientation(self, value):
        if value == Qt.Horizontal:
            self._container.setDirection(QBoxLayout.LeftToRight)
        else:
            self._container.setDirection(QBoxLayout.TopToBottom)
        self.adjustSize()

    def getLayoutSpacing(self):
        return self._container.spacing()

    @Slot(int)
    def setLayoutSpacing(self, value):
        self._container.setSpacing(value)

    @Property(str)
    def settingName(self):
        return self._setting_name

    @settingName.setter
    def settingName(self, name):
        self._setting_name = name

    diameter = Property(int, getLedDiameter, setLedDiameter)
    onColor = Property(QColor, getLedOnColor, setLedOnColor)
    offColor = Property(QColor, getLedOffColor, setLedOffColor)
    alignment = Property(Qt.Alignment, getAlignment, setAlignment)
    orientation = Property(Qt.Orientation, getOrientation, setOrientation)
    layoutSpacing = Property(int, getLayoutSpacing, setLayoutSpacing)


if __name__ == "__main__":
    import sys
    from qtpy.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = JogSpeedPercentageWidget(standalone=True)
    w.show()
    sys.exit(app.exec_())
