'''
Created on 18 juil. 2019

@author: f24178c
'''

import curses


def main(stdscr):
 
    stdscr.clear()
    
    stdscr.addstr("Hello World")
    stdscr.refresh()
    
    begin_x = 20; begin_y = 7
    height = 5; width = 40
    win = curses.newwin(height, width, begin_y, begin_x)
    
    win.addstr("Windows")
    win.refresh()

    stdscr.getkey()

if __name__ == '__main__':
    curses.wrapper(main)
