import ctypes
import os
import subprocess
import sys
from ctypes.wintypes import HWND
from multiprocessing import Process

from utils.command import ButtonExecutionCommand, WaitCommand, CommandProcessor


def attack_bob():
    command_button_1 = ButtonExecutionCommand(0x02, 0.1)
    wait_command = WaitCommand(6)

    processor = CommandProcessor([wait_command, command_button_1])
    while 1:
        processor.process()


def mana_potion():
    command_button_1 = ButtonExecutionCommand(0x02, 0.1)
    wait_command = WaitCommand(6)

    processor = CommandProcessor([wait_command, command_button_1])
    while 1:
        processor.process()


def bot():
    attack_bob_process = Process(target=attack_bob)
    mana_potion_process = Process(target=mana_potion)


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
    bot()


if __name__ == '__main__':
    run_with_admin_privileges()
