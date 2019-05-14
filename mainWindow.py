import resources

from lightning import Plugin
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QAction, qApp, QDesktopWidget, QStackedWidget, QInputDialog, QMessageBox

from overviewPage import OverviewPage
from receivePage import ReceivePage
from sendPage import SendPage
from channelsPage import ChannelsPage

class MainWindow(QMainWindow):
    """The main window of our application.
    
    It will contain a toolbar and a QStackedWidget to switch between page.
    :parameter plugin: A reference to the plugin used to access its methods such as the RPC.
    """
    def __init__(self, plugin):
        super().__init__()
        self.plugin = plugin
        self.initUi()

    def createActions(self):
        """Creates the main actions of the page.
        
        Namely the menubar and toolbar actions.
        """
        # MenuBar actions
        self.quit_action = QAction("&Quit", self)
        self.quit_action.setShortcut("Ctrl+Q")
        self.quit_action.setStatusTip("Exit the GUI without stopping lightningd")
        self.quit_action.triggered.connect(qApp.quit)
        self.minimize_action = QAction("&Minimize", self)
        self.minimize_action.setShortcut("Ctrl+M")
        self.minimize_action.triggered.connect(lambda: self.showMinimized())
        self.restore_action = QAction("&Restore", self)
        self.restore_action.triggered.connect(lambda: self.show())
        self.del_expired_invoices_action = QAction("&Delete expired invoices", self)
        self.del_expired_invoices_action.triggered.connect(lambda: self.plugin.rpc.delexpiredinvoice())
        self.del_invoice_action = QAction("&Delete a specified unpaid invoice", self)
        self.del_invoice_action.triggered.connect(self.menuDelInvoice)
        #self.get_address_act
        # ToolBar actions
        self.show_overview_action = QAction(QIcon(":/icons/overview"), "&Overview", self)
        self.show_overview_action.setToolTip("Show overview page")
        self.show_overview_action.setShortcut("Alt+1")
        self.show_overview_action.triggered.connect(self.showOverview)
        self.show_receivepay_action = QAction(QIcon(":/icons/receive"), "&Receive Payment", self)
        self.show_receivepay_action.setToolTip("Show receive payment page")
        self.show_receivepay_action.setShortcut("Alt+2")
        self.show_receivepay_action.triggered.connect(self.showReceive)
        self.show_sendpay_action = QAction(QIcon(":/icons/send"), "&Send Payment", self)
        self.show_sendpay_action.setToolTip("Show send payment page")
        self.show_sendpay_action.setShortcut("Alt+3")
        self.show_sendpay_action.triggered.connect(self.showSend)
        self.show_managechan_action = QAction(QIcon(":/icons/lightning"), "&Manage channels", self)
        self.show_managechan_action.setToolTip("Show channel management page")
        self.show_managechan_action.setShortcut("Alt+4")
        self.show_managechan_action.triggered.connect(self.showChannelsPage)

    def createMenu(self):
        """Creates the menu at the top of the window."""
        self.menu = self.menuBar()
        file_menu = self.menu.addMenu("&File")
        file_menu.addAction(self.quit_action)
        window_menu = self.menu.addMenu("&Window")
        window_menu.addAction(self.minimize_action)
        window_menu.addAction(self.restore_action)
        invoice_menu = self.menu.addMenu("&Invoices")
        invoice_menu.addAction(self.del_expired_invoices_action)
        invoice_menu.addAction(self.del_invoice_action)

    def createPages(self):
        """Creates each of our pages, which are QWidget-inherited objects
        
        We pass a reference to the plugin to pages, so that they can interact
        with it (for now it's mainly for RPC).
        """
        self.overview_page = OverviewPage(self.plugin)
        self.page_manager.addWidget(self.overview_page)
        self.receive_page = ReceivePage(self.plugin)
        self.page_manager.addWidget(self.receive_page)
        self.send_page = SendPage(self.plugin)
        self.page_manager.addWidget(self.send_page)
        self.channels_page = ChannelsPage(self.plugin)
        self.page_manager.addWidget(self.channels_page)

    def createPageManager(self):
        """Creates the QStackedWidget which we will use as the page manager"""
        self.page_manager = QStackedWidget(self)
        self.setCentralWidget(self.page_manager)

    def createToolbar(self):
        """Creates the toolbar used to navigate between pages"""
        self.toolbar = self.addToolBar("")
        self.toolbar.setContextMenuPolicy(Qt.PreventContextMenu)
        self.toolbar.setMovable(False)
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolbar.addAction(self.show_overview_action)
        self.toolbar.addAction(self.show_receivepay_action)
        self.toolbar.addAction(self.show_sendpay_action)
        self.toolbar.addAction(self.show_managechan_action)
    
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
        self.createPageManager()
        self.createPages()
    
    def menuDelInvoice(self):
        """Shows a message which asks for an invoice label and delete this invoice"""
        label = QInputDialog.getText(self, "Delete an unpaid invoice", "Enter the label of the invoice you want to delete")
        if label[1]:
            result = self.plugin.rpc.delinvoice(label[0], 'unpaid')
            if result:
                QMessageBox.information(self, "Delete an unpaid invoice", "Succesfully deleted invoice")

    def showChannelsPage(self):
        """Set channelsPage as the current widget"""
        self.channels_page.clear()
        self.channels_page.populateChannels()
        self.page_manager.setCurrentWidget(self.channels_page)
    
    def showOverview(self):
        """Set overviewPage as the current widget"""
        self.overview_page.update()
        self.page_manager.setCurrentWidget(self.overview_page)

    def showReceive(self):
        """Set receivePage as the current widget"""
        self.page_manager.setCurrentWidget(self.receive_page)

    def showSend(self):
        """Set sendPage as the current widget"""
        self.page_manager.setCurrentWidget(self.send_page)
