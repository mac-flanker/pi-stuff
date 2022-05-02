#Controlling RGB strip ws2812b

import board
import neopixel


def test(led_count):
    pixels = neopixel.NeoPixel(board.D18, led_count)
    pixels[0] = (255, 0, 0)

    return

