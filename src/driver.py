import sys, time
from random import  randrange, choice
from utilities import *
from main_window import MainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication

def vtick(supply, volt, window):
    offset = float((randrange(-100, 100) / 50) * choice([-1, 1]))
    window.update_status(supply, float(volt  + offset))

def main():
    time_per_tick = 3000

    volt_1 = 3.0
    volt_2 = 2.5
    volt_3 = 2.0

    app = QApplication(sys.argv)
    window = MainWindow()
    window.update_status(1, volt_1)
    window.update_status(2, volt_2)
    window.update_status(3, volt_3)
    window.show()

    #
    # Tick loop timer
    #
    volt1_timer = QTimer()
    volt1_timer.timeout.connect(lambda: vtick(1, volt_1, window))
    volt1_timer.start(time_per_tick / 3)

    volt2_timer = QTimer()
    volt2_timer.timeout.connect(lambda: vtick(2, volt_2, window))
    volt2_timer.start(time_per_tick / 3)

    volt3_timer = QTimer()
    volt3_timer.timeout.connect(lambda: vtick(3, volt_3, window))
    volt3_timer.start(time_per_tick / 3)

    sys.exit(app.exec_())

if __name__ == '__main__': main()
