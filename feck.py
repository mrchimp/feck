#!/usr/bin/env python
# -*- coding: utf-8 -*-

import curses
import sys
import os

prompt_str = "Say > "
chatmode_str = "Chat Mode - type /quit or /q to leave"

screen = curses.initscr()

screen_y, screen_x = screen.getmaxyx()

curses.noecho()
curses.cbreak()
screen.keypad(1)



status_win = curses.newwin(1, screen_x, 0, 0)
status_win.addstr(chatmode_str)
status_win.refresh()

input_win = curses.newwin(1, screen_x, 1, 0)
input_win.addstr(0,0,prompt_str)
input_win.refresh()

output_win = curses.newpad(20, screen_x)
output_win.refresh(0,0, 2,0, 20,20)

def showStatus(msg):
    status_y, status_x = status_win.getmaxyx()
    status_win.clear()
    status_win.refresh()
    status_win.addstr(msg + (" "*(screen_x - len(msg) - 1)), curses.A_REVERSE)
    #status_win.addstr(msg + str(screen_x) + "-" + str(len(msg)) + "-" + str(screen_x - len(msg)), curses.A_REVERSE)
    status_win.refresh()    

def showMessage(message):
    output_win.addstr(message + "\n")
    output_win.refresh(0,0, 2,0, 20,20)

while True: 
    # event = screen.getch()
    # if event == ord('q'): break
    curses.echo()
    input = input_win.getstr(0, 6, 60)
    curses.noecho()
    input = input.decode(sys.stdout.encoding)
    if input == '/quit' or input == '/q':
        #input_win.clear()
        showStatus('Are you sure you want to quit? y/n ')
        #screen.refresh()
        event = input_win.getch()
        if event == ord('y'): 
            break
        else:
            showStatus(chatmode_str)
            input_win.clear()
            input_win.addstr(0,0, prompt_str)
            input_win.refresh()
            continue
    input_win.clear()
    input_win.addstr(0,0, prompt_str)
    input_win.refresh()
    showMessage(input)
    
screen.clear()
curses.nocbreak()
screen.keypad(0)
curses.echo()
curses.endwin()
os.system('cls')
print('Bye then.')
