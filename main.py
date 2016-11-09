#!/usr/bin/env python3

import curses
import math
from matrix import Matrix

def drawMatrix(x,y,matrix,scr):
    rows = matrix.getRows()
    cols = matrix.getCols()
    mat = matrix.getMatrix()
    lotSize = 0
    if rows > 0 and cols > 0:
        lotSize = max([max([len(str(i)) for i in row]) for row in mat])
    scr.addstr(y,x,'┌' + ' ' * (cols*(1 + lotSize) + 1) + '┐')
    for j in range(rows):
        scr.addstr(y+j+1,x,"│ " + ' '.join([str(i) for i in mat[j]]) + " │")
    scr.addstr(y+rows+1,x,'└' + ' ' * (cols*(1 + lotSize) + 1) + '┘')
    return 3 + cols*(1 + lotSize)

def main():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)
    state = [Matrix(), Matrix()]
    nextDraw = drawMatrix(0,0,state[0],stdscr)
    nextDraw += drawMatrix(nextDraw,0,state[1],stdscr) + 3
    drawMatrix(nextDraw,0,state[0]*state[1],stdscr)
    stdscr.refresh()
    from time import sleep
    sleep(3)
    curses.endwin()
    return

if __name__ == "__main__":
    main()
