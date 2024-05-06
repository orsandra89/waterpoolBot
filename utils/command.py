from __future__ import annotations
from abc import ABC, abstractmethod
from directInputs import press_key, release_key
import time
from typing import List


from logger import app_logger


class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self) -> None:
        pass


class ButtonExecutionCommand(Command):

    def __init__(self, key, press_time):
        self._key = key
        self._press_time = press_time

    def execute(self):
        t = None
        if self._press_time is None:
            t = 0.1
        else:
            t = self._press_time
        app_logger.info("press button")
        press_key(self._key)
        time.sleep(t)
        release_key(self._key)


class WaitCommand(Command):

    def __init__(self, wait_time):
        self._wait_time = wait_time

    def execute(self):
        app_logger.info(f"sleep for: [{self._wait_time}]")
        time.sleep(self._wait_time)


class Processor(ABC):

    _commands: List[Command]

    @abstractmethod
    def process(self) -> None:
        pass


class CommandProcessor:

    _commands: List[Command]

    def __init__(self, commands: List[Command]):
        self._commands = commands

    def process(self):
        for command in self._commands:
            command.execute()


if __name__ == '__main__':
    command_button_1 = ButtonExecutionCommand(0x02, 0.1)
    wait_command = WaitCommand(10)
    command_button_2 = ButtonExecutionCommand(0x03, 0.1)

    CommandProcessor([command_button_1, wait_command, command_button_2]).process()
