import ctypes
import os
import subprocess
import sys
import threading
from ctypes.wintypes import HWND
from multiprocessing import Process

import wx
from wx.lib import delayedresult

from configuration import Configuration
from parameters import USE_PRIZE_COUPON, USE_PRODUCTION_COUPON, MONITOR_RESOLUTION, LOWER_REACTION_TIME, \
    UPPER_REACTION_TIME
from utils.command import ButtonExecutionCommand, WaitCommand, CommandProcessor

config = Configuration()


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 700))

        self._bot_process = None
        self.panel = wx.Panel(self)
        self.message_text = wx.StaticText(self.panel, label="Hello, wxPython!", pos=(10, 10))

        menu_bar = wx.MenuBar()
        self.SetMenuBar(menu_bar)

        file_menu = wx.Menu()
        menu_bar.Append(file_menu, "&File")

        self.start_bot_button = wx.Button(self.panel, label="Start Bot", pos=(450, 400))
        self.start_bot_button.Bind(wx.EVT_BUTTON, self.on_start_button_click)
        self.stop_bot_button = wx.Button(self.panel, label="Stop Bot", pos=(350, 400))
        self.stop_bot_button.Bind(wx.EVT_BUTTON, self.stop_fishing_bot)

    def on_start_button_click(self, event):
        if self._bot_process is None or not self._bot_process.is_alive():
            self._bot_process = threading.Thread(target=self.run_bot_function)
            self._bot_process.start()

    def _function_completed(self, result):
        # You can handle the result manually here, e.g., update a label or log the result
        print(result)

    def start_bot_process(self, event):
        command_button_1 = ButtonExecutionCommand(0x02, 0.1)
        wait_command = WaitCommand(6)
        wait_command_1 = WaitCommand(1)
        command_button_2 = ButtonExecutionCommand(0x03, 0.1)

        processor = CommandProcessor([wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1,wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1,wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1,wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1,wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command, command_button_1, wait_command_1, command_button_2])
        while 1:
            processor.process()

    def run_bot_function(self):
        delayedresult.startWorker(self.start_bot_process, self._function_completed)

    def stop_fishing_bot(self, event):
        self._bot_process.terminate()
        self._bot_process.join()
        self._bot_process.close()


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
