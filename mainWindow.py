from lightning import Plugin
from PyQt5.QtWidgets import QMainWindow, QWidget, QAction, qApp, QDesktopWidget

class MainWindow(QMainWindow):
    """The main window of our application.
    
    It will contain a toolbar and a QStackedWidget to switch between page.
    :parameter plugin: A reference to the plugin used to access its methods such as the RPC.
    """
    def __init__(self, plugin):
        super().__init__()
        self.plugin = plugin
        self.initUi()

    def initUi(self):
        """Initializes the default parameters for the window (title, position, size)."""
        self.setWindowTitle("lightning-qt")
        self.resize(700, 500)
        geo = self.frameGeometry()
        geo.moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(geo.topLeft())
        self.createActions()
        self.createMenu()

    def createActions(self):
        """Creates the main actions of the page.
        
        Namely the menubar and toolbar actions.
        """
        self.quit_action = QAction("&Quit", self)
        self.quit_action.setShortcut("Ctrl+Q")
        self.quit_action.setStatusTip("Exit the GUI without stopping lightningd")
        self.quit_action.triggered.connect(qApp.quit)
        self.minimize_action = QAction("&Minimize", self)
        self.minimize_action.setShortcut("Ctrl+M")
        self.minimize_action.triggered.connect(lambda: self.showMinimized())
        self.restore_action = QAction("&Restore", self)
        self.restore_action.triggered.connect(lambda: self.show())
        self.del_expired_invoices = QAction("&Delete expired invoices", self)
        # Wait for the method to be merged in pylightning
        #self.del_expired_invoices.triggered.connect(lambda: self.plugin.rpc.delexpiredinvoice())

    def createMenu(self):
        """Creates the menu at the top of the window."""
        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(self.quit_action)
        window_menu = menu.addMenu("&Window")
        window_menu.addAction(self.minimize_action)
        window_menu.addAction(self.restore_action)
        invoice_menu = menu.addMenu("&Invoices")
        invoice_menu.addAction(self.del_expired_invoices)
