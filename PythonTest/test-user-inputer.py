"""
test User Input
"""

#! /usr/bin/python3
# -*- coding:utf-8 -*-

import time
import unittest
import random
import threading
from pynput import mouse, keyboard


class TestUserInputer(unittest.TestCase):
    """TestUserInputer
    This need install pynput module.
    $ sudo [pip|pip3] install pynput
    """
    global T

    def __init__(self):
        super(TestUserInputer, self).__init__()
        self.mouse = mouse.Controller()
        self.keyboard = keyboard.Controller()

    def test_url(self):
        """go_docs"""
        self.mouse.position = (792, 54)
        self.mouse.press(mouse.Button.left)
        self.mouse.release(mouse.Button.left)
        print("sleep...1")
        time.sleep(2)
        self.keyboard.press(keyboard.Key.ctrl_l)
        self.keyboard.press('l')
        self.keyboard.release(keyboard.Key.ctrl_l)
        self.keyboard.release('l')
        self.keyboard.press(keyboard.Key.delete)
        self.keyboard.release(keyboard.Key.delete)
        print("sleep...2")
        time.sleep(2)
        self.keyboard.type('https://docs.python.org/3.7/library/index.html')
        print("sleep...3")
        time.sleep(2)
        self.keyboard.press(keyboard.Key.enter)
        self.keyboard.release(keyboard.Key.enter)
        # just in case use fcitx input, press enter again
        self.keyboard.press(keyboard.Key.enter)
        self.keyboard.release(keyboard.Key.enter)
        print("sleep...4")
        time.sleep(2)
        self.mouse.position = (792, 754)
        self.mouse.press(mouse.Button.left)
        self.mouse.release(mouse.Button.left)

    def test_wheel(self, delta=1):
        """test mouse wheel action"""
        self.mouse.scroll(0, random.randrange(-10 - delta, 10 + delta))
        return False

    def test_refresh_browser(self):
        """press F5"""
        self.keyboard.press(keyboard.Key.f5)
        self.keyboard.release(keyboard.Key.f5)

    def test_while_sleep(self, time_interval):
        """test threading"""
        for i in range(160):
            self.test_wheel()
            time.sleep(time_interval)
            if i % 3 == 0:
                self.test_refresh_browser()
        return

    def test_log(self):
        """test print log"""
        print("yooho!!!\n\n")

    def test_thread(self, count, time_interval):
        """test thread use for multiple"""
        for i in range(count):
            T = threading.Timer(time_interval, self.test_log)
            T.start()
            T.join(timeout=time_interval)
        T.cancel()


def main():
    """main function"""
    print("========start======")
    time.sleep(2)
    tui = TestUserInputer()
    tui.test_url()
    tui.test_while_sleep(60)
    # tui.test_thread(10, 5)
    print("========end======")


if __name__ == '__main__':
    main()
