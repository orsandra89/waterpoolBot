import time
import random
from abc import ABC, abstractmethod

from pyautogui import *
import pyautogui

from directInputs import press_key, release_key


class BaseListener(ABC):
    human_reaction_time = (0.1, 0.15)

    def start(self):
        while 1:
            if self._detect():
                time.sleep(random.uniform(self.human_reaction_time[0], self.human_reaction_time[1]))
                self._handle()

    @abstractmethod
    def _handle(self):
        pass

    @abstractmethod
    def _detect(self) -> bool:
        pass


class BaseHandler(ABC):

    def __init__(self, key, press_time):
        self.key = key
        self.press_time = press_time

    def press_key(self, p_time=None):
        t = None
        if p_time is None:
            t = self.press_time
        else:
            t = p_time
        print("press")
        press_key(self.key)
        time.sleep(t)
        release_key(self.key)
        # time.sleep(0.1)


class DetectorListener(object):
    human_reaction_time = (0.1, 0.15)

    def __init__(self, t, reaction=(0.1, 0.15)):
        self.t = t
        self.human_reaction_time = reaction

    def start(self):
        while 1:
            if self._detect(self.t[0][0], self.t[0][1], self.t[0][2]):
                time.sleep(random.uniform(self.human_reaction_time[0], self.human_reaction_time[1]))
                self.t[0][3].press_key()
            elif self._detect(self.t[1][0], self.t[1][1], self.t[1][2]):
                time.sleep(random.uniform(self.human_reaction_time[0], self.human_reaction_time[1]))
                self.t[1][3].press_key()
            elif self._detect(self.t[2][0], self.t[2][1], self.t[2][2]):
                time.sleep(random.uniform(self.human_reaction_time[0], self.human_reaction_time[1]))
                self.t[2][3].press_key()
            elif self._detect(self.t[3][0], self.t[3][1], self.t[3][2]):
                time.sleep(random.uniform(self.human_reaction_time[0], self.human_reaction_time[1]))
                self.t[3][3].press_key()

    def _detect(self, sample, region, confidence) -> bool:
        return pyautogui.locateOnScreen(sample, region=region, confidence=confidence) is not None


class PixelDetectorListener(object):
    human_reaction_time = (0.1, 0.15)

    def __init__(self, t, reaction=(0.1, 0.15)):
        self.t = t
        self.human_reaction_time = reaction

    def start(self):
        while 1:

            # if self._detect_pixel(self.t[0][1][0], self.t[0][1][1], self.t[0][2][1], self.t[0][5]):
            #     print("find evil left")
            #     time.sleep(random.uniform(self.human_reaction_time[0], self.human_reaction_time[1]))
            #     self.t[0][4].press_key(self.t[0][3][1])
            #     time.sleep(0.545)
            # elif self._detect_pixel(self.t[1][1][0], self.t[1][1][1], self.t[1][2][1], self.t[1][5]):
            #     print("find evil left")
            #     time.sleep(random.uniform(self.human_reaction_time[0], self.human_reaction_time[1]))
            #     self.t[1][4].press_key(self.t[1][3][1])
            #     time.sleep(0.545)
            # elif self._detect_pixel(self.t[2][1][0], self.t[2][1][1], self.t[2][2][1], self.t[2][5]):
            #     print("find evil left")
            #     time.sleep(random.uniform(self.human_reaction_time[0], self.human_reaction_time[1]))
            #     self.t[2][4].press_key(self.t[2][3][1])
            #     time.sleep(0.545)
            # elif self._detect_pixel(self.t[0][1][0], self.t[0][1][1], self.t[0][2][1], self.t[3][5]):
            #     print("find evil left")
            #     time.sleep(random.uniform(self.human_reaction_time[0], self.human_reaction_time[1]))
            #     self.t[0][4].press_key(self.t[0][3][1])
            #     time.sleep(0.545)
            if self._detect_pixel(self.t[0][1][0], self.t[0][1][1], self.t[0][2][0], self.t[0][5]):
                print("find evil left")
                time.sleep(random.uniform(self.human_reaction_time[0], self.human_reaction_time[1]))
                self.t[0][4].press_key(self.t[0][3][0])
                time.sleep(0.545)
            elif self._detect_pixel(self.t[1][1][0], self.t[1][1][1], self.t[1][2][0], self.t[1][5]):
                print("find evil left")
                time.sleep(random.uniform(self.human_reaction_time[0], self.human_reaction_time[1]))
                self.t[1][4].press_key(self.t[1][3][0])
                time.sleep(0.545)
            elif self._detect_pixel(self.t[2][1][0], self.t[2][1][1], self.t[2][2][0], self.t[2][5]):
                print("find evil left")
                time.sleep(random.uniform(self.human_reaction_time[0], self.human_reaction_time[1]))
                self.t[2][4].press_key(self.t[2][3][0])
                time.sleep(0.545)
            elif self._detect_pixel(self.t[0][1][0], self.t[0][1][1], self.t[0][2][0], self.t[3][5]):
                print("find evil left")
                time.sleep(random.uniform(self.human_reaction_time[0], self.human_reaction_time[1]))
                self.t[0][4].press_key(self.t[0][3][0])
                time.sleep(0.545)

    def _detect_pixel(self, x, y, color, region) -> bool:
        return pyautogui.pixelMatchesColor(int(x), int(y), color, tolerance=10)
