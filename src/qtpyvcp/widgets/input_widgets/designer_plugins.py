from qtpyvcp.widgets.qtdesigner import _DesignerPlugin
from qtpyvcp.widgets.qtdesigner.designer_plugin import RulesEditorExtension
from qtpyvcp.widgets.qtdesigner.dro_editor import DroEditorExtension
from qtpyvcp.widgets.qtdesigner.settings_selector import SettingSelectorExtension
from .action_combobox import ActionComboBox
from .action_dial import ActionDial
from .action_slider import ActionSlider
from .dro_line_edit import DROLineEdit
from .file_system import FileSystemTable
from .file_system import RemovableDeviceComboBox
from .gcode_text_edit import GcodeTextEdit
from .jog_increment import JogIncrementWidget
from .jog_speed_percentage import JogSpeedPercentageWidget
from .line_edit import VCPLineEdit
from .mdientry_widget import MDIEntry
from .mdihistory_widget import MDIHistory
from .offset_table import OffsetTable
from .probesim_widget import ProbeSim
from .recent_file_combobox import RecentFileComboBox
from .setting_slider import (VCPSettingsLineEdit,
                             VCPSettingsSlider,
                             VCPSettingsSpinBox,
                             VCPSettingsDoubleSpinBox,
                             VCPSettingsCheckBox,
                             VCPSettingsPushButton,
                             VCPSettingsComboBox)
from .teachin_dro_label import TeachInDroLabel
from .teachin_line_edit import TeachInLineEdit
from .tool_table import ToolTable


class VCPLineEditPlugin(_DesignerPlugin):
    def pluginClass(self):
        return VCPLineEdit


class MDIEntryPlugin(_DesignerPlugin):
    def pluginClass(self):
        return MDIEntry

    def toolTip(self):
        return "MDI command entry"


class MDIHistoryPlugin(_DesignerPlugin):
    def pluginClass(self):
        return MDIHistory


# from .gcode_editor import GcodeEditor
# class GcodeEditorPlugin(_DesignerPlugin):
#     def pluginClass(self):
#         return GcodeEditor


class gCodeEditPlugin(_DesignerPlugin):
    def pluginClass(self):
        return GcodeTextEdit


class RecentFileComboBoxPlugin(_DesignerPlugin):
    def pluginClass(self):
        return RecentFileComboBox


class ToolTablePlugin(_DesignerPlugin):
    def pluginClass(self):
        return ToolTable


class JogIncrementPlugin(_DesignerPlugin):
    def pluginClass(self):
        return JogIncrementWidget


class JogSpeedPercentagePlugin(_DesignerPlugin):
    def pluginClass(self):
        return JogSpeedPercentageWidget


class FileSystemPlugin(_DesignerPlugin):
    def pluginClass(self):
        return FileSystemTable


class RemovableDeviceComboBoxPlugin(_DesignerPlugin):
    def pluginClass(self):
        return RemovableDeviceComboBox


class ActionSliderPlugin(_DesignerPlugin):
    def pluginClass(self):
        return ActionSlider


class ActionDialPlugin(_DesignerPlugin):
    def pluginClass(self):
        return ActionDial


class ActionComboBoxPlugin(_DesignerPlugin):
    def pluginClass(self):
        return ActionComboBox


class ProbeSimPlugin(_DesignerPlugin):
    def pluginClass(self):
        return ProbeSim


class VCPSettingsLineEditPlugin(_DesignerPlugin):
    def pluginClass(self):
        return VCPSettingsLineEdit

    def objectName(self):
        return 'settings_lineedit'

    def designerExtensions(self):
        return [SettingSelectorExtension, RulesEditorExtension]


class VCPSettingsSliderPlugin(_DesignerPlugin):
    def pluginClass(self):
        return VCPSettingsSlider

    def objectName(self):
        return 'settings_slider'

    def designerExtensions(self):
        return [SettingSelectorExtension, RulesEditorExtension]


class VCPSettingsSpinBoxPlugin(_DesignerPlugin):
    def pluginClass(self):
        return VCPSettingsSpinBox

    def objectName(self):
        return 'settings_spinbox'

    def designerExtensions(self):
        return [SettingSelectorExtension, RulesEditorExtension]


class VCPSettingsDoubleSpinBoxPlugin(_DesignerPlugin):
    def pluginClass(self):
        return VCPSettingsDoubleSpinBox

    def objectName(self):
        return 'settings_double_spinbox'

    def designerExtensions(self):
        return [SettingSelectorExtension, RulesEditorExtension]


class VCPSettingsCheckBoxPlugin(_DesignerPlugin):
    def pluginClass(self):
        return VCPSettingsCheckBox

    def designerExtensions(self):
        return [SettingSelectorExtension, RulesEditorExtension]

    def domXml(self):
        return """
        <widget class="VCPSettingsCheckBox" name="settings_checkbox">
          <property name="text">
            <string>CheckBox</string>
          </property>
        </widget>"""


class VCPSettingsPushButtonPlugin(_DesignerPlugin):
    def pluginClass(self):
        return VCPSettingsPushButton

    def designerExtensions(self):
        return [SettingSelectorExtension, RulesEditorExtension]

    def domXml(self):
        return """
        <widget class="VCPSettingsPushButton" name="settings_pushbutton">
          <property name="text">
            <string>Settings Button</string>
          </property>
        </widget>"""


class VCPSettingsComboBoxPlugin(_DesignerPlugin):
    def pluginClass(self):
        return VCPSettingsComboBox

    def designerExtensions(self):
        return [SettingSelectorExtension, RulesEditorExtension]


class OffsetTablePlugin(_DesignerPlugin):
    def pluginClass(self):
        return OffsetTable

    def objectName(self):
        return 'offset_table'


class DROLineEdit_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return DROLineEdit

    def objectName(self):
        return 'dro_entry'

    def designerExtensions(self):
        return [DroEditorExtension, RulesEditorExtension]


class TeachInLineEdit_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return TeachInLineEdit

    def objectName(self):
        return 'teachin_line_edit'

    def designerExtensions(self):
        return [DroEditorExtension, RulesEditorExtension]


class TeachInDroLabel_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return TeachInDroLabel

    def objectName(self):
        return 'teachin_dro_label'

    def designerExtensions(self):
        return [DroEditorExtension, RulesEditorExtension]
