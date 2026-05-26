import curses
from main import *
import threading
from state import appareils
def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_RED)
    stdscr.nodelay(True)
    choice = 0
    while True:
        stdscr.erase()
        height, width = stdscr.getmaxyx()

        stdscr.addstr(0, 0, "=== Pyrate ===", curses.color_pair(1))
        if choice == 1:
            stdscr.addstr(1, 0, "scan", curses.color_pair(2))
            stdscr.addstr(1, 6, "spy", curses.color_pair(1))
        elif choice == 2:
            stdscr.addstr(1, 0, "scan", curses.color_pair(1))
            stdscr.addstr(1, 6, "spy", curses.color_pair(2))
        elif choice == 0:    
            stdscr.addstr(1, 0, "scan", curses.color_pair(1))
            stdscr.addstr(1, 6, "spy", curses.color_pair(1))
        n = 2
        for adresse, infos in appareils.items():
            stdscr.addstr(n, 0, f"{adresse} | {infos['nom']} | {infos['rssi']} dBm")
            n += 1
        stdscr.addstr(height-1, 0, "q : quitter")
        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == curses.KEY_UP:
            choice += 1
        elif key == curses.KEY_DOWN:
            choice -= 1
        elif key in (10, 13, curses.KEY_ENTER):
            if choice == 1:
                threading.Thread(target=lambda: asyncio.run(scan()), daemon=True).start()
                

            elif choice == 2: 
                threading.Thread(target=lambda: asyncio.run(spy()), daemon=True).start()
            

curses.wrapper(main)