import ctypes
import os
import subprocess
import sys
from ctypes.wintypes import HWND

import wx

from configuration import Configuration
from parameters import USE_PRIZE_COUPON, USE_PRODUCTION_COUPON, MONITOR_RESOLUTION, LOWER_REACTION_TIME, \
    UPPER_REACTION_TIME

config = Configuration()


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 700))

        self.panel = wx.Panel(self)
        self.message_text = wx.StaticText(self.panel, label="Hello, wxPython!", pos=(10, 10))

        menu_bar = wx.MenuBar()
        self.SetMenuBar(menu_bar)

        file_menu = wx.Menu()
        menu_bar.Append(file_menu, "&File")

        self.monitor_resolution_label = wx.StaticText(self.panel, label="Monitor Resolution:", pos=(10, 100))
        self.monitor_resolution_choices = ["1920:1080", "2560:1440", "3840:2160"]
        self.monitor_resolution_dropdown = wx.Choice(self.panel, choices=self.monitor_resolution_choices,
                                                     pos=(120, 100))
        self.monitor_resolution_dropdown.SetSelection(
            self.monitor_resolution_choices.index(config.get_setting(MONITOR_RESOLUTION)))

        self.use_prize_coupon_checkbox = wx.CheckBox(self.panel, label="Use Prize Coupon", pos=(10, 140))
        self.use_prize_coupon_checkbox.SetValue(config.get_setting(USE_PRIZE_COUPON))

        self.use_production_coupon_checkbox = wx.CheckBox(self.panel, label="Use Production Coupon", pos=(10, 180))
        self.use_production_coupon_checkbox.SetValue(config.get_setting(USE_PRODUCTION_COUPON))

        self.lower_time_reaction_label = wx.StaticText(self.panel, label="Lower Time Reaction:", pos=(10, 220))
        self.lower_time_reaction_input = wx.TextCtrl(self.panel, pos=(130, 220))
        self.lower_time_reaction_input.SetValue(str(config.get_setting(LOWER_REACTION_TIME)))

        self.upper_time_reaction_label = wx.StaticText(self.panel, label="Upper Time Reaction:", pos=(10, 260))
        self.upper_time_reaction_input = wx.TextCtrl(self.panel, pos=(130, 260))
        self.upper_time_reaction_input.SetValue(str(config.get_setting(UPPER_REACTION_TIME)))

        self.applied_configuration_label = wx.StaticText(self.panel, label="Applied Configuration:", pos=(250, 100))
        self.applied_configuration_input = wx.TextCtrl(self.panel, value=config.generate_configuration_string(),
                                                       pos=(250, 140), size=(250, 150),
                                                       style=wx.TE_MULTILINE | wx.TE_READONLY)

        self.apply_configuration = wx.Button(self.panel, label="Apply Configuration", pos=(10, 350))
        self.apply_configuration.Bind(wx.EVT_BUTTON, self.on_apply_configuration_click)

        self.start_bot_button = wx.Button(self.panel, label="Start Bot", pos=(450, 400))
        self.stop_bot_button = wx.Button(self.panel, label="Stop Bot", pos=(350, 400))

    def on_apply_configuration_click(self, event):
        monitor_resolution = self.monitor_resolution_dropdown.GetStringSelection()
        use_prize_coupon = self.use_prize_coupon_checkbox.GetValue()
        use_production_coupon = self.use_production_coupon_checkbox.GetValue()
        lower_reaction_time = int(self.lower_time_reaction_input.GetValue())
        upper_reaction_time = int(self.upper_time_reaction_input.GetValue())
        config.set_setting(MONITOR_RESOLUTION, monitor_resolution)
        config.set_setting(USE_PRIZE_COUPON, use_prize_coupon)
        config.set_setting(USE_PRODUCTION_COUPON, use_production_coupon)
        config.set_setting(LOWER_REACTION_TIME, lower_reaction_time)
        config.set_setting(UPPER_REACTION_TIME, upper_reaction_time)
        self.applied_configuration_input.SetValue(config.generate_configuration_string())

    def on_message_choice(self, event):
        selected_message = self.message_choice.GetStringSelection()
        self.message_text.SetLabel(selected_message)

    def on_checkbox_change(self, event):
        selected_message = self.message_choice.GetStringSelection()
        if self.use_prize_coupon_checkbox.GetValue():
            selected_message = "Custom Message"
        self.message_text.SetLabel(selected_message)


def is_admin():
    if os.name == 'posix':  # Unix-based systems (Linux, macOS)
        try:
            return subprocess.check_call(['sudo', sys.executable] + sys.argv) == 0
        except subprocess.CalledProcessError:
            return False

    elif os.name == 'nt':  # Windows
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except subprocess.CalledProcessError:
            return False
    else:
        print("Unsupported platform. Administrator privileges check not available.")
        sys.exit(1)

def run_with_admin_privileges():
    if not is_admin():
        if os.name == 'nt':
            # Prompt for administrator privileges on Windows using UAC
            ctypes.windll.shell32.ShellExecuteW(HWND(0), "runas", sys.executable, " ".join(sys.argv), None, 1)
        else:
            print("Administrator privileges are required to run this script.")
            sys.exit(1)

    # Your code that requires administrator/root privileges goes here
    print("Running with administrator/root privileges!")

    app = wx.App(False)
    frame = MyFrame(None, "Simple wxPython GUI")
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    run_with_admin_privileges()
