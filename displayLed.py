#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

import re
import time
import argparse

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT


def showMessage(msg,n, block_orientation, rotate):
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=n or 4, block_orientation=block_orientation, rotate=rotate or 0)
    print("Created device")

    # start 
    #msg = "Slow scrolling: The quick brown fox jumps over the lazy dog"
    i=0
    repeats=2
    while i<repeats : 
        show_message(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=0.1)
        time.sleep(1)
        i=i+1
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='matrix_demo arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--message', type=str)
    parser.add_argument('--cascaded', '-n', type=int, default=4, help='Number of cascaded MAX7219 LED matrices')
    parser.add_argument('--block-orientation', type=int, default=-90, choices=[0, 90, -90], help='Corrects block orientation when wired vertically')
    parser.add_argument('--rotate', type=int, default=0, choices=[0, 1, 2, 3], help='Rotate display 0=0°, 1=90°, 2=180°, 3=270°')

    args = parser.parse_args()

    try:
        showMessage(args.message,args.cascaded, args.block_orientation, args.rotate)
    except KeyboardInterrupt:
        pass


