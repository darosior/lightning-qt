#!/usr/bin/env python3
from lightning import Plugin
from PyQt5.QtWidgets import QApplication, QWidget

from mainWindow import MainWindow

plugin = Plugin()

@plugin.init()
def init(options, configuration, plugin):
    print('aa')

@plugin.method("gui")
def gui(plugin):
    """Launches the Qt GUI"""
    app = QApplication([])
    win = MainWindow(plugin)
    win.show()
    return "Succesfully stopped lightning-qt." if not app.exec_() else "An error occured."

plugin.run()
