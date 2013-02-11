#!/usr/bin/env python
# -*- coding: utf-8 -*-

import curses
import sys
import os

prompt_str = "Say > "
chatmode_str = "Chat Mode - type /quit or /q to leave"

class Feck:

    def __init__(self):
        curses.wrapper(self.main)
        print('Bye then.')

    def main(self, screen):
        curses.use_default_colors()
        self.screen_y, self.screen_x = screen.getmaxyx()
        
        self.status_win = curses.newwin(1, self.screen_x, 0, 0)
        self.status_win.addstr(chatmode_str)
        self.status_win.refresh()

        self.input_win = curses.newwin(1, self.screen_x, 1, 0)
        self.input_win.addstr(0,0,prompt_str)
        self.input_win.refresh()

        self.output_win = curses.newpad(20, self.screen_x)
        self.output_win.refresh(0,0, 2,0, 20,20)
        
        while True:
            curses.echo()
            input = self.input_win.getstr(0, 6, 60)
            curses.noecho()
            input = input.decode(sys.stdout.encoding)
            if input == '/quit' or input == '/q':
                self.showStatus('Are you sure you want to quit? y/n ')
                event = self.input_win.getch()
                if event == ord('y'): 
                    break
                else:
                    self.showStatus(chatmode_str)
                    self.input_win.clear()
                    self.input_win.addstr(0,0, prompt_str)
                    self.input_win.refresh()
                    continue
            self.input_win.clear()
            self.input_win.addstr(0,0, prompt_str)
            self.input_win.refresh()
            self.showMessage(input)
        
    def showStatus(self, msg):
        self.status_win.clear()
        self.status_win.refresh()
        self.status_win.addstr(msg + (" "*(self.screen_x - len(msg) - 1)), curses.A_BLINK)
        self.status_win.refresh()    

    def showMessage(self, message):
        self.output_win.addstr(message + "\n")
        self.output_win.refresh(0,0, 2,0, 20,20)
        
if __name__ == '__main__':
    feck = Feck()