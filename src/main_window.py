import sys
from utilities import *
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from generic_main_window import Ui_gen_window

class MainWindow(QtWidgets.QMainWindow, Ui_gen_window):
    def __init__(self, parent=None):
        # Pre-Config setup
        super(MainWindow, self).__init__()
        log(Mode.INFO, "Constructing main window...")
        self.setupUi(self)
        self.event_listeners()

        self.p_connected = [ False, False, False ]
        self.p_vars = {
            1: [self.p1_vread, self.p1_cread, self.pstat_1],
            2: [self.p2_vread, self.p2_cread, self.pstat_2],
            3: [self.p3_vread, self.p3_cread, self.pstat_3]
        }

        # Load the local config
        self.config = load_json("../res/config.json")
        log(Mode.INFO, "Loaded config from file: " + str(self.config))

        # Post-config setup
        self.setWindowTitle(self.config['title'])

    def event_listeners(self):
        log(Mode.INFO, "Adding event listerner and signalers...")

    def update_pwr_connection(self, s_index, mode):
        self.p_vars[s_index][2].setText(mode.name)
        self.p_vars[s_index][2].setStyleSheet( 'font-size: 30px; color: rgb(' + mode.value + '); background: rgb(40, 44, 52); border-radius: 10px;')

    def update_pwr_status(self, s_index, voltage, current):
        self.p_vars[s_index][0].display(float(voltage))
        self.p_vars[s_index][1].display(float(current))

    def resizeEvent(self, event):
        # Determine the scale size
        size = event.size()
        prev_size = event.oldSize()
        x_scale = size.width() / prev_size.width()
        y_scale = size.height() / prev_size.height()

        # Apply scaling
        if(x_scale > -4 and y_scale > -4): # Band-aid fix for window init trying to scale by incredibly large negative numbers
            x_menu = self.menu.width() * x_scale
            y_menu = self.menu.height() * y_scale
            new_font = int(self.font().pointSize() * y_scale)
            self.font().setPointSize(new_font)
            # self.menu.resize(x_menu, y_menu) # TODO Broken
            # self.p1_status.resize(self.p1_status.width() * x_scale, self.p1_status.height()) # TODO Broken
            if(self.config['qtg_debug']):
                log(Mode.DEBUG, "ScaleEvent(" + str(x_scale) + " x " + str(y_scale) +")")
                log(Mode.DEBUG, "\tFont: " + str(new_font) + "px")
                log(Mode.DEBUG, "\tMenu: From(" + str(self.menu.width()) + " x " + str(self.menu.height()) + ") To(" + str(x_menu) + " x " + str(y_menu) +")")

    def button_clicked(self, i):
        if(self.config['qtg_debug']): log(Mode.DEBUG, "Button clicked: " + i.text())

    def create_popup(self, title="N/A", icon=QMessageBox.Information, text="N/A", default=None, buttons=[]):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(icon)

        if(isinstance(buttons, list)):
            for button in buttons: msg.addButton(button)
        if(default in buttons): msg.setDefaultButton(default)
        msg.buttonClicked.connect(self.button_clicked)
        x = msg.exec_()

def main(): log(Mode.ERROR, "Do not call this module directly!\n\tCall driver.py instead to initialize the GUI!")
if __name__ == '__main__': main()
