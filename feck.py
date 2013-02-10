import curses
import sys

screen = curses.initscr()

screen_y, screen_x = screen.getmaxyx()

curses.noecho()
curses.curs_set(0)
screen.keypad(1)

screen.addstr(5, 10, "This is a string")

screen.addstr(10, 10, "Reverse Styled String", curses.A_REVERSE)

while True: 
    #event = screen.getch()
    screen.addstr(1,1, '>> ')
    screen.refresh()
    input = screen.getstr(2, 2, 60)
    input = input.decode(sys.stdout.encoding)
    if input == 'quit' or input == 'q': break
    screen.refresh()
    screen.addstr(10, 10, input)
    screen.refresh()
    
   
curses.endwin()