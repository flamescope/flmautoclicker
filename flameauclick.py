import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, Key, KeyCode

de = input("Input Delay: ")
de2 = float(de)
#inp = input("Input Key: ")
#inp2 = str(inp)

delay = de2
button = Button.left
start_stop_key = Key.f4
exit_key = KeyCode(char="      ")

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super().__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        print("Started")
        self.running = True

    def stop_clicking(self):
        print("stopped")
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running == True:
            time.sleep(0.1)
            while self.running == True:
                mouse.click(self.button)
                print("clicked")
                time.sleep(self.delay)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit
        listener.stop()


with Listener(on_press=press) as listener:
    print("CURRENT KEY TO START/STOP IS F4")
    listener.join()
