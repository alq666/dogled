from time import time, sleep, localtime
from raspledstrip.ledstrip import *
from raspledstrip.color import SysColors

led = LEDStrip(32)
led.all_off()

# Hours start at led 0, minutes start at led 6 and seconds at led 13
LED_OFFSET = (0, 6, 13)
COLORS = (Color(0, 255, 0, 0.25), Color(255, 255, 0, 0.25), Color(255, 0, 0, 0.25))
OFF_COLOR = SysColors.white25

def is_on(v):
    """Convert an integer into a list of 0/1
    This will be used to know which leds to turn on
    """
    assert v >= 0
    return [v == '1' for v in list(bin(v)[2:])]
    
def to_led(led, v, offset, color, off_color):
    """Turns a value into a binary led representation
    """
    seq = is_on(v)
    print v, seq
    for i in range(len(seq)):
        if seq[i]:
            led.set(offset + i, color)
        else:
            led.set(offset + i, off_color)

def main():
    try:
        while True:
            lt = localtime()
            t = (lt.tm_hour, lt.tm_min, lt.tm_sec)
            for i in range(3):
                to_led(led, t[i], LED_OFFSET[i], COLORS[i], OFF_COLOR)
            led.update()
            sleep(1)   
    finally:
        led.all_off()

if __name__ == '__main__':
    main()
