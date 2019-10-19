import sys
from utilities import *
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from generic_main_window import Ui_gen_window

class MainWindow(QtWidgets.QMainWindow, Ui_gen_window):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.action_listeners()

        self.saved_state = True

    def action_listeners(self):
        self.m_new.triggered.connect(lambda: self.popup(title="New Session",
                                                        icon=QMessageBox.Question,
                                                        text="Start a new session without saving?",
                                                        buttons=[QMessageBox.Yes, QMessageBox.No],
                                                        default=QMessageBox.No))
        self.m_open.triggered.connect(lambda: self.popup(title="Open Session",
                                                         icon=QMessageBox.Question,
                                                         text="Open a session without saving?",
                                                         buttons=[QMessageBox.Yes, QMessageBox.No],
                                                         default=QMessageBox.No))
        self.m_save.triggered.connect(lambda: self.popup(title="Saved Session",
                                                         text="Your session was saved!",
                                                         buttons=[QMessageBox.Ok]))
        # self.m_copy.triggered.connect(lambda: self.popup())
        # self.m_paste.triggered.connect(lambda: self.popup())

        self.submit.clicked.connect(lambda: self.change_control(self.power_supply.currentText(), self.control_mode.currentText()))

        self.b1_img.clicked.connect(lambda: self.set_image("../imgs/banner.png"))
        self.b2_img.clicked.connect(lambda: self.set_image("../imgs/cage-etl.jpg"))

    def update_status(self, supply, voltage):
        greenshift = int((voltage / 3) * 255) - 100
        if(greenshift < 0): greenshift = 0
        elif(greenshift > 255): greenshift = 255
        redshift = int(255 - greenshift)

        if(supply == 3): c_pwr = self.v_pwr3
        elif(supply == 2): c_pwr = self.v_pwr2
        else: c_pwr = self.v_pwr1

        c_pwr.setText(str(voltage))
        c_pwr.setStyleSheet("color: rgb(0, 0, 0);  background: rgb(" + str(redshift) + "," + str(greenshift) + ", 0);")
        c_pwr.adjustSize()

    def button_clicked(self, i):
        log(Mode.DEBUG, "Button clicked: " + i.text())

    def change_control(self, pwr_supply, c_mode):
        log(Mode.INFO, "Setting supply " + str(pwr_supply) + " to " + c_mode + " control mode.")
        self.submit.setStatusTip("Set supply " + str(self.power_supply.currentText()) + " to " + self.control_mode.currentText() + " control mode.")

    def mark_title(self, state):
        if(not state):
            if(self.windowTitle()[0] != '*'): self.setWindowTitle('*' + self.windowTitle())
        else: self.setWindowTitle(self.windowTitle()[1:])

    def set_image(self, img_path):
        self.saved_state = False
        self.mark_title(self.saved_state)
        self.img.setPixmap(QtGui.QPixmap(img_path))

    def popup(self, title="Alert", icon=QMessageBox.Information, text="N/A", default=None, buttons=[]):
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
