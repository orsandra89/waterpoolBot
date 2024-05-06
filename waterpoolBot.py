# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

from pyautogui import *
import pyautogui

from multiprocessing import Process, Pool, freeze_support

from directInputs import LEFT, UP, RIGHT, DOWN, set_pos, left_click
from eventDetectorListener import BaseHandler, DetectorListener, PixelDetectorListener


# # left_box_region = (-1560, 350, 100, 130)
# # up_box_region = (-1430, 275, 100, 130)
# # right_box_region = (-1325, 345, 100, 130)
# # down_box_region = (-1465, 385, 100, 130)
# # wal_box_region = (-1637, 395, 500, 60)
# # result_box_region = (-1620, 325, 530, 220)
# # win_box_region = (773, 342, 138, 32)
#
# left_box_region = (770, 470, 100, 130)
# up_box_region = (930, 410, 100, 130)
# right_box_region = (1040, 465, 100, 130)
# down_box_region = (885, 520, 100, 130)
# wal_box_region = (720, 520, 500, 60)
# result_box_region = (700, 430, 530, 220)
# win_box_region = (773, 342, 138, 32)
#
# left_rod_position = (843, 527)
# right_rod_position = (1115, 528)
# up_rod_position = (997, 479)
# down_rod_position = (959, 585)
#
# wait_time = (1.0, 5.0)
# wal_key_press_time = 0.1
# rod_key_press_time = 0.415
# # rod_key_press_time = 0.1
#
#
# wal_confidence = 0.9
# rod_confidence = 0.98
#
# color = (198, 247, 255)
#
# ####### Event Handlers #########
#
#
# wal_left_key_handler = BaseHandler(key=LEFT, press_time=wal_key_press_time)
# wal_up_key_handler = BaseHandler(key=UP, press_time=wal_key_press_time)
# wal_right_key_handler = BaseHandler(key=RIGHT, press_time=wal_key_press_time)
# wal_down_key_handler = BaseHandler(key=DOWN, press_time=wal_key_press_time)
# rod_left_key_handler = BaseHandler(key=LEFT, press_time=rod_key_press_time)
# rod_up_key_handler = BaseHandler(key=UP, press_time=rod_key_press_time)
# rod_right_key_handler = BaseHandler(key=RIGHT, press_time=rod_key_press_time)
# rod_down_key_handler = BaseHandler(key=DOWN, press_time=rod_key_press_time)
#
# ####### Event Handlers END #########
#
#
# ####### Detector Listeners #########
#
#
# wal_list = [
#     (
#         './samples/left_wal_arrow_sample.png',
#         wal_box_region,
#         wal_confidence,
#         wal_left_key_handler
#     ),
#     (
#         './samples/up_wal_arrorw_sample.png',
#         wal_box_region,
#         wal_confidence,
#         wal_up_key_handler
#     ),
#     (
#         './samples/right_wal_arrow_sample.png',
#         wal_box_region,
#         wal_confidence,
#         wal_right_key_handler
#     ),
#     (
#         './samples/down_wal_arrorw_sample.png',
#         wal_box_region,
#         wal_confidence,
#         wal_down_key_handler
#     )
# ]
# rod_list = [
#     (
#         './samples/left_rod_sample_test.png',
#         left_box_region,
#         rod_confidence,
#         rod_left_key_handler
#     ),
#     (
#         './samples/up_rod_sample_test.png',
#         up_box_region,
#         rod_confidence,
#         rod_up_key_handler
#     ),
#     (
#         './samples/right_rod_sample_test.png',
#         right_box_region,
#         rod_confidence,
#         rod_right_key_handler
#     ),
#     (
#         './samples/down_rod_sample_test.png',
#         down_box_region,
#         rod_confidence,
#         rod_down_key_handler
#     )
# ]
# pixel_rod_list = [
#     (
#         left_rod_position[0],
#         left_rod_position[1],
#         color,
#         rod_left_key_handler
#     ),
#     (
#         up_rod_position[0],
#         up_rod_position[1],
#         color,
#         rod_up_key_handler
#     ),
#     (
#         right_rod_position[0],
#         right_rod_position[1],
#         color,
#         rod_right_key_handler
#     ),
#     (
#         down_rod_position[0],
#         down_rod_position[1],
#         color,
#         rod_down_key_handler
#     )
# ]
#
# wal_listener = DetectorListener(
#     t=wal_list
# )
#
# rod_listener = DetectorListener(
#     t=rod_list
# )
#
# pixel_rod_listener = PixelDetectorListener(
#     t=pixel_rod_list
# )
#
# ####### Detector Listeners END #########
#
#
# ####### Processes #########
#
#
# rod_process = Process(target=rod_listener.start)
# pixel_rod_process = Process(target=pixel_rod_listener.start)
# wal_process = Process(target=wal_listener.start)
#
#
# ####### Processes END #########
#
#
# def start_game():
#     print("start_game")
#     pixel_rod_process.start()
#     wal_process.start()
#
#
# def stop_game():
#     pixel_rod_process.terminate()
#     wal_process.terminate()
#     pixel_rod_process.close()
#     wal_process.close()
#
#
# def minigame_bot():
#     stopped_game = False
#     center_coordinate = locateCenterOnScreen('./samples/minigame_window.png', grayscale=False, confidence=0.9)
#     print(center_coordinate)
#     time.sleep(random.uniform(wait_time[0], wait_time[1]))
#     press_start_button()
#     start_game()
#     while 1:
#         if not stopped_game and pyautogui.locateOnScreen('./samples/two_sample.png', region=win_box_region,
#                                                          confidence=0.9) is not None:
#             stop_game()
#             time.sleep(random.uniform(wait_time[0], wait_time[1]))
#             stopped_game = True
#         elif stopped_game and pyautogui.locateOnScreen('./samples/result_sample.png', region=result_box_region,
#                                                        confidence=0.9) is not None:
#             get_reward()
#             time.sleep(random.uniform(wait_time[0], wait_time[1]))
#             chose_level()
#             time.sleep(random.uniform(wait_time[0], wait_time[1]))
#             try_again_win()
#             stopped_game = False
#             time.sleep(random.uniform(wait_time[0], wait_time[1]))
#             press_start_button()
#             time.sleep(random.uniform(wait_time[0], wait_time[1]))
#             start_game()
#         elif not stopped_game and pyautogui.locateOnScreen('./samples/result_sample.png', region=result_box_region,
#                                                            confidence=0.9) is not None:
#             try_again_lose()
#             time.sleep(random.uniform(wait_time[0], wait_time[1]))
#             stopped_game = False
#             press_start_button()
#             time.sleep(random.uniform(wait_time[0], wait_time[1]))
#         # else:
#         #     try_again_lose()
#         #     time.sleep(random.uniform(wait_time[0], wait_time[1]))
#         #     stopped_game = False
#         #     press_start_button()
#         #     time.sleep(random.uniform(wait_time[0], wait_time[1]))
#
#
# def try_again_lose():
#     time.sleep(5.0)
#     set_pos(835, 590)
#     left_click()
#
#
# def try_again_win():
#     set_pos(900, 620)
#     left_click()
#
#
# def get_reward():
#     set_pos(1085, 590)
#     left_click()
#
#
# def chose_level():
#     set_pos(1085, 590)
#     left_click()
#
#
# def press_start_button():
#     print("press start")
#     set_pos(955, 708)
#     left_click()


class MinigameBot:
    ####### Config #############

    wal_confidence = 0.9
    rod_confidence = 0.98

    color = (198, 247, 255)
    evil_color = (204, 43, 37)

    wait_time = (1.0, 5.0)
    wal_key_press_time = 0.1
    rod_key_press_time = 0.1
    evil_key_press_time = 0.41

    use_prize_coupon = True

    ####### Config END ###########

    minigame_window_center = None

    ####### Event Handlers #########

    wal_left_key_handler = BaseHandler(key=LEFT, press_time=wal_key_press_time)
    wal_up_key_handler = BaseHandler(key=UP, press_time=wal_key_press_time)
    wal_right_key_handler = BaseHandler(key=RIGHT, press_time=wal_key_press_time)
    wal_down_key_handler = BaseHandler(key=DOWN, press_time=wal_key_press_time)
    rod_left_key_handler = BaseHandler(key=LEFT, press_time=rod_key_press_time)
    rod_up_key_handler = BaseHandler(key=UP, press_time=rod_key_press_time)
    rod_right_key_handler = BaseHandler(key=RIGHT, press_time=rod_key_press_time)
    rod_down_key_handler = BaseHandler(key=DOWN, press_time=rod_key_press_time)
    evil_left_key_handler = BaseHandler(key=LEFT, press_time=evil_key_press_time)
    evil_up_key_handler = BaseHandler(key=UP, press_time=evil_key_press_time)
    evil_right_key_handler = BaseHandler(key=RIGHT, press_time=evil_key_press_time)
    evil_down_key_handler = BaseHandler(key=DOWN, press_time=evil_key_press_time)

    ####### Event Handlers END #########

    ####### Regions ##############

    wal_box_region = (720, 520, 500, 60)
    result_box_region = (700, 430, 530, 220)
    win_box_region = (773, 342, 138, 32)

    ####### Regions END ##############

    def _generate_rod_position(self):
        left_x = self.minigame_window_center[0] - 116
        left_y = self.minigame_window_center[1] - 13
        right_x = self.minigame_window_center[0] + 156
        right_y = self.minigame_window_center[1] - 12
        up_x = self.minigame_window_center[0] + 38
        up_y = self.minigame_window_center[1] - 61
        down_x = self.minigame_window_center[0] + 0
        down_y = self.minigame_window_center[1] + 45
        Point(x=959, y=540)
        # evil_left_x = self.minigame_window_center[0] - 125
        # evil_left_y = self.minigame_window_center[1] - 4
        # evil_right_x = self.minigame_window_center[0] + 144
        # evil_right_y = self.minigame_window_center[1] - 1
        # evil_up_x = self.minigame_window_center[0] + 26
        # evil_up_y = self.minigame_window_center[1] - 50
        # evil_down_x = self.minigame_window_center[0] - 9
        # evil_down_y = self.minigame_window_center[1] + 55
        evil_left_x = self.minigame_window_center[0] - 125
        evil_left_y = self.minigame_window_center[1] + 1
        evil_right_x = self.minigame_window_center[0] + 147
        evil_right_y = self.minigame_window_center[1] - 1
        evil_up_x = self.minigame_window_center[0] + 25
        evil_up_y = self.minigame_window_center[1] - 46
        evil_down_x = self.minigame_window_center[0] - 12
        evil_down_y = self.minigame_window_center[1] + 59
        Point(-12, +11)
        self.left_rod_position = (left_x, left_y)
        Point(843, 527)
        self.right_rod_position = (right_x, right_y)
        Point(1115, 528)
        self.up_rod_position = (up_x, up_y)
        Point(997, 479)
        self.down_rod_position = (down_x, down_y)
        Point(959, 585)
        self.left_evil_position = (evil_left_x, evil_left_y)
        Point(831, 538)
        self.right_evil_position = (evil_right_x, evil_right_y)
        Point(1103, 539)
        self.up_evil_position = (evil_up_x, evil_up_y)
        Point(985, 490)
        self.down_evil_position = (evil_down_x, evil_down_y)
        Point(948, 595)

    def _generate_wal_detector_listener(self):
        self.wal_list = [
            (
                './samples/left_wal_arrow_sample.png',
                self.wal_box_region,
                self.wal_confidence,
                self.wal_left_key_handler
            ),
            (
                './samples/up_wal_arrorw_sample.png',
                self.wal_box_region,
                self.wal_confidence,
                self.wal_up_key_handler
            ),
            (
                './samples/right_wal_arrow_sample.png',
                self.wal_box_region,
                self.wal_confidence,
                self.wal_right_key_handler
            ),
            (
                './samples/down_wal_arrorw_sample.png',
                self.wal_box_region,
                self.wal_confidence,
                self.wal_down_key_handler
            )
        ]
        self.wal_listener = DetectorListener(
            t=self.wal_list
        )

    def _generate_rod_detector_listener(self):
        self.pixel_rod_list = [
            (
                (self.left_rod_position[0], self.left_rod_position[1]),
                (self.left_evil_position[0], self.left_evil_position[1]),
                (self.color, self.evil_color),
                (self.rod_key_press_time, self.evil_key_press_time),
                self.rod_left_key_handler,
                self.minigame_window
            ),
            (
                (self.up_rod_position[0], self.up_rod_position[1]),
                (self.up_evil_position[0], self.up_evil_position[1]),
                (self.color, self.evil_color),
                (self.rod_key_press_time, self.evil_key_press_time),
                self.rod_up_key_handler,
                self.minigame_window
            ),
            (
                (self.right_rod_position[0], self.right_rod_position[1]),
                (self.right_evil_position[0], self.right_evil_position[1]),
                (self.color, self.evil_color),
                (self.rod_key_press_time, self.evil_key_press_time),
                self.rod_right_key_handler,
                self.minigame_window
            ),
            (
                (self.down_rod_position[0], self.down_rod_position[1]),
                (self.down_evil_position[0], self.down_evil_position[1]),
                (self.color, self.evil_color),
                (self.rod_key_press_time, self.evil_key_press_time),
                self.rod_down_key_handler,
                self.minigame_window
            )
        ]
        self.pixel_rod_listener = PixelDetectorListener(
            t=self.pixel_rod_list
        )

    def _generate_proceses(self):
        self.pixel_rod_process = Process(target=self.pixel_rod_listener.start)
        self.wal_process = Process(target=self.wal_listener.start)

    def start_game(self):
        print("start_game")
        # self.pixel_rod_process.start()
        self.wal_process.start()

    def stop_game(self):
        # self.pixel_rod_process.terminate()
        self.wal_process.terminate()
        # self.pixel_rod_process.join()
        self.wal_process.join()
        # self.pixel_rod_process.close()
        self.wal_process.close()

    def minigame_bot(self):
        stopped_game = False
        self.minigame_window_center = locateCenterOnScreen('./samples/minigame_window.png', grayscale=False,
                                                           confidence=0.9)
        self.minigame_window = locateOnScreen('./samples/minigame_window.png', grayscale=False,
                                                           confidence=0.9)
        print(self.minigame_window_center)
        self._generate_rod_position()
        self._generate_wal_detector_listener()
        self._generate_rod_detector_listener()
        self._generate_proceses()
        time.sleep(random.uniform(self.wait_time[0], self.wait_time[1]))
        self.press_start_button()
        self.start_game()
        while 1:
            if not stopped_game and pyautogui.locateOnScreen('./samples/two_sample.png', region=self.win_box_region,
                                                             confidence=0.9) is not None:
                self.stop_game()
                time.sleep(random.uniform(self.wait_time[0], self.wait_time[1]))
                stopped_game = True
            elif stopped_game and pyautogui.locateOnScreen('./samples/result_sample.png', region=self.result_box_region,
                                                           confidence=0.9) is not None:
                self.get_reward()
                time.sleep(random.uniform(self.wait_time[0], self.wait_time[1]))
                self.chose_level()
                time.sleep(random.uniform(self.wait_time[0], self.wait_time[1]))
                self.use_prize_coupon()
                time.sleep(random.uniform(self.wait_time[0], self.wait_time[1]))
                self.try_again_win()
                stopped_game = False
                time.sleep(random.uniform(self.wait_time[0], self.wait_time[1]))
                self.press_start_button()
                time.sleep(random.uniform(self.wait_time[0], self.wait_time[1]))
                self.start_game()
            elif not stopped_game and pyautogui.locateOnScreen('./samples/result_sample.png',
                                                               region=self.result_box_region,
                                                               confidence=0.9) is not None:
                self.try_again_lose()
                time.sleep(random.uniform(self.wait_time[0], self.wait_time[1]))
                stopped_game = False
                self.press_start_button()
                time.sleep(random.uniform(self.wait_time[0], self.wait_time[1]))

    def try_again_lose(self):
        time.sleep(5.0)
        try_again_button_center = locateCenterOnScreen('./samples/try_again_button.png', grayscale=False,
                                                       confidence=0.9)
        set_pos(try_again_button_center[0], try_again_button_center[1])
        left_click()

    def try_again_win(self):
        time.sleep(5.0)
        try_again_win_button_center = locateCenterOnScreen('./samples/try_again_win_button.png', grayscale=False,
                                                           confidence=0.9)
        set_pos(try_again_win_button_center[0], try_again_win_button_center[1])
        left_click()

    def get_reward(self):
        time.sleep(5.0)
        get_reward_button_center = locateCenterOnScreen('./samples/get_reward_button.png', grayscale=False,
                                                        confidence=0.9)
        set_pos(get_reward_button_center[0], get_reward_button_center[1])
        left_click()
        time.sleep(1.0)
        set_pos(get_reward_button_center[0], get_reward_button_center[1] + 40)

    def chose_level(self):
        time.sleep(5.0)
        chose_level_button_center = locateCenterOnScreen('./samples/chose_level_button.png', grayscale=False,
                                                         confidence=0.98)
        set_pos(chose_level_button_center[0], chose_level_button_center[1])
        left_click()

    def press_start_button(self):
        print("press start")
        start_button_center = locateCenterOnScreen('./samples/start_game_button.png', grayscale=False,
                                                   confidence=0.9)
        set_pos(start_button_center[0], start_button_center[1])
        left_click()

    def use_prize_coupon_f(self):
        print("press start")
        find = False
        try:
            location = locateOnScreen('./samples/prize_coupon_window.png', grayscale=False, confidence=0.9)
            if location is not None:
                find = True
            else:
                find = False
        except pyautogui.ImageNotFoundException:
            find = False

        if find and self.use_prize_coupon:
            confirm_prize_coupon_button_center = locateCenterOnScreen('./samples/prize_coupon_confirm_button.png',
                                                                grayscale=False,
                                                                confidence=0.9)
            set_pos(confirm_prize_coupon_button_center[0], confirm_prize_coupon_button_center[1])
            left_click()

        if find and not self.use_prize_coupon:
            cancel_prize_coupon_button_center = locateCenterOnScreen('./samples/prize_coupon_cancel_button.png',
                                                               grayscale=False,
                                                               confidence=0.9)
            set_pos(cancel_prize_coupon_button_center[0], cancel_prize_coupon_button_center[1])
            left_click()


if __name__ == '__main__':
    # freeze_support()
    time.sleep(5)
    # minigame_bot()
    MinigameBot().minigame_bot()
