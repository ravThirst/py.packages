from datetime import date
import keyboard
from application.salary import set_salary
from application.db.people import get_people
from threading import Thread


def simulate():
    print('\n')
    worker = get_people()
    set_salary(worker)
    print(date.today())


def main_thread():
    simulate()
    print('\nPress "Alt + Z" to run program again or "Esc" to cancel')
    keyboard.wait('esc')


def program():
    keyboard.add_hotkey('alt + z', simulate)
    t = Thread(target=main_thread)
    t.run()


if __name__ == '__main__':
    program()
