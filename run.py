#!/usr/bin/python2
# -*- coding: utf8 -*-

"""
Le Lotus: alpha version.
Licence GNU GPL v3.
    Bapt Abl, 2016.
"""

run_with_curses = True



from core import core

def launch(scr):
    core(
        arduino_port='/dev/ttyACM0',
        arduino_speed=115200,
        SCR=scr,
        ncurses=run_with_curses
    ).start()

if run_with_curses:
    from curses import wrapper
    wrapper(launch)  # encapsulation pour curses
else:
    launch(False)
