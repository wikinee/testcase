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

    def __init__(self):
        super(TestUserInputer, self).__init__()
        self.mouse = mouse.Controller()
        self.keyboard = keyboard.Controller()
        self.list = "abcdefghijklmnopqrstuvwxyz"

    def test_terminal(self, count):
        """test terminal"""
        while count > 1:
            time.sleep(0.5)
            j = random.choice(self.list)
            self.keyboard.type(j)
            self.keyboard.press(keyboard.Key.space)
            self.keyboard.release(keyboard.Key.space)
            count = count - 1


def main():
    """main function"""
    print("========start======")
    time.sleep(2)
    tui = TestUserInputer()
    tui.test_terminal(1000)
    print("========end======")


if __name__ == '__main__':
    main()
