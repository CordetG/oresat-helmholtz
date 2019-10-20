import sys
from utilities import *
from PyQt5.QtWidgets import QApplication, QMessageBox
from main_window import MainWindow

# Imports only for simulating
from random import random, randrange, choice
from PyQt5.QtCore import QTimer

def tick(timer, window, undef, voltages, currents):
    for i in range(0, 3):
        new_status = randrange(0, 100)

        if(not undef[i] and new_status >= 10):
            direction = choice([-1, 1])
            voffset = random() * direction
            coffset = (random() * direction) / 2

            voltages[i] = voltages[i] + voffset
            currents[i] = currents[i] + coffset

            window.update_pwr_connection(i + 1, Status.ON)
            window.update_pwr_status(i + 1, voltages[i], currents[i])
        elif(not undef[i] and new_status < 10 and new_status > 1):
            window.update_pwr_connection(i + 1, Status.OFF)
            window.update_pwr_status(i + 1, 0, 0)
        else:
            undef[i] = True
            window.update_pwr_connection(i + 1, Status.UNDF)
            window.update_pwr_status(i + 1, -1, -1)

    if(not (False in undef)):
        msg = 'All three power supplies were lost. The helmholtz cage can no longer operate.'
        window.create_popup(title="Total Power Loss", text=msg)
        log(Mode.ERROR, msg)
        timer.stop()

def main():
    # Pre init details
    undef = [False, False, False]
    voltages = [3.75, 2.28, 1.25]
    currents = [0.72, 1.11, 0.33]

    config = load_json('../res/config.json')

    # Init
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # Tick
    timer = QTimer()
    tick(timer, window, undef, voltages, currents)
    timer.timeout.connect(lambda: tick(timer, window, undef, voltages, currents))
    timer.start(config['tick_rate'])

    # Exit
    sys.exit(app.exec_())

if __name__ == '__main__': main()
