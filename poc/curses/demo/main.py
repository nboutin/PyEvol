'''
Created on 18 juil. 2019

@author: f24178c
'''

import curses


def main():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)



    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()


if __name__ == '__main__':
    curses.wrapper(main)
