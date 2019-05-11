from lightning import Plugin
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
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
        self.createToolbar()

    def createActions(self):
        """Creates the main actions of the page.
        
        Namely the menubar and toolbar actions.
        """
        #MenuBar actions
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
        self.del_expired_invoices.triggered.connect(lambda: self.plugin.rpc.delexpiredinvoice())
        #ToolBar actions
        self.overview_action = QAction(QIcon(":/icons/overview"), "&Overview", self)
        self.overview_action.setToolTip("Show overview page")
        self.overview_action.setShortcut("Alt+1")
        #self.overview_action.triggered.connect()
        self.receivepay_action = QAction(QIcon(":/icons/receive"), "&Receive Payment", self)
        self.receivepay_action.setToolTip("Show receive payment page")
        self.receivepay_action.setShortcut("Alt+2")
        #self.overview_action.triggered.connect()
        self.sendpay_action = QAction(QIcon(":/icons/send"), "&Send Payment", self)
        self.sendpay_action.setToolTip("Show send payment page")
        self.sendpay_action.setShortcut("Alt+3")
        #self.overview_action.triggered.connect()
        self.managechan_action = QAction(QIcon(":/icons/lightning"), "&Manage channels", self)
        self.managechan_action.setToolTip("Show channel management page")
        self.managechan_action.setShortcut("Alt+4")
        #self.overview_action.triggered.connect()

    def createMenu(self):
        """Creates the menu at the top of the window."""
        self.menu = self.menuBar()
        file_menu = self.menu.addMenu("&File")
        file_menu.addAction(self.quit_action)
        window_menu = self.menu.addMenu("&Window")
        window_menu.addAction(self.minimize_action)
        window_menu.addAction(self.restore_action)
        invoice_menu = self.menu.addMenu("&Invoices")
        invoice_menu.addAction(self.del_expired_invoices)

    def createToolbar(self):
        """Creates the toolbar used to navigate between pages"""
        self.toolbar = self.addToolBar("")
        self.toolbar.setContextMenuPolicy(Qt.PreventContextMenu)
        self.toolbar.setMovable(False)
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolbar.addAction(self.overview_action)
        self.toolbar.addAction(self.receivepay_action)
        self.toolbar.addAction(self.sendpay_action)
        self.toolbar.addAction(self.managechan_action)
