#!/usr/bin/env python3
import os

from lightning import LightningRpc, Plugin, RpcError
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

from mainWindow import MainWindow

class HackedLightningRpc(LightningRpc):
    """Dark side Lightning Rpc

    PyQt5 (after v5.5) will call qFatal() (and then abort()) when an exception is
    thrown in a slot. This behavior cannot be changed (C++ API) nor it can `except`ed.
    It means that if you make a Rpc call which raises an error in a slot (for example,
    randomly, `decodepay` with an user-entered value) it will exit the application
    without even a traceback : PyQt5.5 we <3 u.

    To avoid this behevior I thought of making hand checks before making a Rpc call in
    a slot (i.e. doing this for each Rpc call since a GUI is event-driven), or override
    the `call` method which raises exceptions to quiet the RPC exception and open a dialog
    for the user to understand what's happening. I chose the second method.
    """
    def call(self, method, payload=None):
        """Original call method with Qt-style exception handling"""
        try:
            return super(HackedLightningRpc, self).call(method, payload)
        except RpcError as e:
            QMessageBox.warning(None, "RPC error", str(e))
            pass
        return False # Rpc call failed


plugin = Plugin()

@plugin.init()
def init(options, configuration, plugin):
    path = os.path.join(plugin.lightning_dir, plugin.rpc_filename)
    # See above the docstring for rationale
    plugin.rpc = HackedLightningRpc(path)

@plugin.method("gui")
def gui(plugin):
    """Launches the Qt GUI"""
    app = QApplication([])
    win = MainWindow(plugin)
    win.show()
    return "Succesfully stopped lightning-qt" if not app.exec_() else "An error occured"

plugin.run()
