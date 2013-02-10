#!/usr/bin/env python
# -*- coding: utf-8 -*-

import curses
import sys

screen = curses.initscr()

screen_y, screen_x = screen.getmaxyx()

#curses.noecho()
curses.cbreak()
#curses.curs_set(0)
screen.keypad(1)

output_win = curses.newwin(screen_y - 1, screen_x - 1, 1, 0)
output_win.addstr("heres some text\n")
output_win.addstr("heres some more\n")
output_win.refresh()

input_win = curses.newwin(1, 1, 0, 0)
input_win.addstr(">> ")
input_win.refresh()

while True: 
    #event = screen.getch()
    screen.refresh()
    curses.echo()
    input = input_win.getstr(0, 4, 60)
    curses.noecho()
    input = input.decode(sys.stdout.encoding)
    if input == 'quit' or input == 'q': break
    input_win.clear()
    input_win.addstr(0,0, '>> ')
    input_win.refresh()
    output_win.addstr(input + "\n")
    output_win.refresh()
    
curses.nocbreak()
screen.keypad(0)
curses.echo()
curses.endwin()

