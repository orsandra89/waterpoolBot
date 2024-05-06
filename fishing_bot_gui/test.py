import ctypes
import multiprocessing
import os
import subprocess
import sys
from ctypes.wintypes import HWND

import wx
import wx.lib.delayedresult as delayedresult
import threading
import time

from logger import app_logger
from utils.command import ButtonExecutionCommand, WaitCommand, CommandProcessor


class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)

        self.panel = wx.Panel(self)
        self.start_button = wx.Button(self.panel, label="Start Bot", pos=(10, 10))
        self.stop_button = wx.Button(self.panel, label="Stop Bot", pos=(10, 40))
        self.result_label = wx.StaticText(self.panel, label="", pos=(10, 80))

        self.process_thread = None
        self.is_process_running = False

        self.Bind(wx.EVT_BUTTON, self.on_start_button_click, self.start_button)
        self.Bind(wx.EVT_BUTTON, self.on_stop_button_click, self.stop_button)

    def on_start_button_click(self, event):
        if not self.is_process_running:
            self.is_process_running = True
            self.process_thread = multiprocessing.Process(target=run_endless_process)
            self.process_thread.start()
            app_logger.info("Process started.")

    def on_stop_button_click(self, event):
        if self.is_process_running:
            self.is_process_running = False
            self.process_thread.terminate()
            self.process_thread.join()
            app_logger.info("Process stopped.")

    def update_result_label(self, result):
        self.result_label.SetLabel(result)


def run_endless_process():
    command_button_1 = ButtonExecutionCommand(0x02, 0.1)
    wait_command = WaitCommand(17)
    command_button_2 = ButtonExecutionCommand(0x03, 0.1)
    wait_command_2 = WaitCommand(2)

    processor = CommandProcessor([command_button_1, wait_command, command_button_2, wait_command_2])
    while 1:
        # Simulate some work
        time.sleep(1)
        processor.process()
        app_logger.info("Continue...")


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
    frame = MyFrame(parent=None, id=-1, title="Fishing Bot")
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    run_with_admin_privileges()

1
