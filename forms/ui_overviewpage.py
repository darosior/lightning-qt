# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/overviewpage.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OverviewPage(object):
    def setupUi(self, OverviewPage):
        OverviewPage.setObjectName("OverviewPage")
        OverviewPage.resize(593, 262)
        self.verticalLayout = QtWidgets.QVBoxLayout(OverviewPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_5 = QtWidgets.QFrame(OverviewPage)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.pushButtonBalance = QtWidgets.QPushButton(self.frame_5)
        self.pushButtonBalance.setEnabled(True)
        self.pushButtonBalance.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonBalance.setToolTip("")
        self.pushButtonBalance.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/warning"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/icons/warning"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.pushButtonBalance.setIcon(icon)
        self.pushButtonBalance.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonBalance.setFlat(True)
        self.pushButtonBalance.setObjectName("pushButtonBalance")
        self.horizontalLayout_8.addWidget(self.pushButtonBalance)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.verticalLayout_10.addLayout(self.horizontalLayout_8)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(12)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labelPendingLightning = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelPendingLightning.setFont(font)
        self.labelPendingLightning.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.labelPendingLightning.setText("0 MSAT")
        self.labelPendingLightning.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPendingLightning.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelPendingLightning.setObjectName("labelPendingLightning")
        self.gridLayout_3.addWidget(self.labelPendingLightning, 2, 2, 1, 1)
        self.labelBalanceBitcoin = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelBalanceBitcoin.setFont(font)
        self.labelBalanceBitcoin.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.labelBalanceBitcoin.setText("0 SAT")
        self.labelBalanceBitcoin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelBalanceBitcoin.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelBalanceBitcoin.setObjectName("labelBalanceBitcoin")
        self.gridLayout_3.addWidget(self.labelBalanceBitcoin, 1, 1, 1, 1)
        self.labelBalanceLightning = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelBalanceLightning.setFont(font)
        self.labelBalanceLightning.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.labelBalanceLightning.setText("0 MSAT")
        self.labelBalanceLightning.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelBalanceLightning.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelBalanceLightning.setObjectName("labelBalanceLightning")
        self.gridLayout_3.addWidget(self.labelBalanceLightning, 1, 2, 1, 1)
        self.labelPending = QtWidgets.QLabel(self.frame_5)
        self.labelPending.setObjectName("labelPending")
        self.gridLayout_3.addWidget(self.labelPending, 2, 0, 1, 1)
        self.labelBitcoin = QtWidgets.QLabel(self.frame_5)
        self.labelBitcoin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelBitcoin.setObjectName("labelBitcoin")
        self.gridLayout_3.addWidget(self.labelBitcoin, 0, 1, 1, 1)
        self.labelPendingBitcoin = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelPendingBitcoin.setFont(font)
        self.labelPendingBitcoin.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.labelPendingBitcoin.setText("0 SAT")
        self.labelPendingBitcoin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPendingBitcoin.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelPendingBitcoin.setObjectName("labelPendingBitcoin")
        self.gridLayout_3.addWidget(self.labelPendingBitcoin, 2, 1, 1, 1)
        self.lineBitcoinBalance = QtWidgets.QFrame(self.frame_5)
        self.lineBitcoinBalance.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineBitcoinBalance.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineBitcoinBalance.setObjectName("lineBitcoinBalance")
        self.gridLayout_3.addWidget(self.lineBitcoinBalance, 3, 0, 1, 2)
        self.lineLightningBalance = QtWidgets.QFrame(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineLightningBalance.sizePolicy().hasHeightForWidth())
        self.lineLightningBalance.setSizePolicy(sizePolicy)
        self.lineLightningBalance.setMinimumSize(QtCore.QSize(140, 0))
        self.lineLightningBalance.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineLightningBalance.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineLightningBalance.setObjectName("lineLightningBalance")
        self.gridLayout_3.addWidget(self.lineLightningBalance, 3, 2, 1, 1)
        self.labelTotal = QtWidgets.QLabel(self.frame_5)
        self.labelTotal.setObjectName("labelTotal")
        self.gridLayout_3.addWidget(self.labelTotal, 4, 0, 1, 1)
        self.labelBitcoinTotal = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelBitcoinTotal.setFont(font)
        self.labelBitcoinTotal.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.labelBitcoinTotal.setText("0 SAT")
        self.labelBitcoinTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelBitcoinTotal.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelBitcoinTotal.setObjectName("labelBitcoinTotal")
        self.gridLayout_3.addWidget(self.labelBitcoinTotal, 4, 1, 1, 1)
        self.labelLightningTotal = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelLightningTotal.setFont(font)
        self.labelLightningTotal.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.labelLightningTotal.setText("0 MSAT")
        self.labelLightningTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelLightningTotal.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelLightningTotal.setObjectName("labelLightningTotal")
        self.gridLayout_3.addWidget(self.labelLightningTotal, 4, 2, 1, 1)
        self.labelLightning = QtWidgets.QLabel(self.frame_5)
        self.labelLightning.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelLightning.setObjectName("labelLightning")
        self.gridLayout_3.addWidget(self.labelLightning, 0, 2, 1, 1)
        self.labelAvailable = QtWidgets.QLabel(self.frame_5)
        self.labelAvailable.setObjectName("labelAvailable")
        self.gridLayout_3.addWidget(self.labelAvailable, 1, 0, 1, 1)
        self.verticalLayout_10.addLayout(self.gridLayout_3)
        self.verticalLayout_9.addWidget(self.frame_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem1)
        self.horizontalLayout_7.addLayout(self.verticalLayout_9)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_6 = QtWidgets.QFrame(OverviewPage)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.labelLightningOverview = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelLightningOverview.setFont(font)
        self.labelLightningOverview.setObjectName("labelLightningOverview")
        self.horizontalLayout_9.addWidget(self.labelLightningOverview)
        self.label_33 = QtWidgets.QPushButton(self.frame_6)
        self.label_33.setEnabled(True)
        self.label_33.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_33.setToolTip("")
        self.label_33.setText("")
        self.label_33.setIcon(icon)
        self.label_33.setIconSize(QtCore.QSize(24, 24))
        self.label_33.setFlat(True)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_9.addWidget(self.label_33)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.verticalLayout_12.addLayout(self.horizontalLayout_9)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSpacing(12)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.labelChannelCountTotalText = QtWidgets.QLabel(self.frame_6)
        self.labelChannelCountTotalText.setObjectName("labelChannelCountTotalText")
        self.gridLayout_5.addWidget(self.labelChannelCountTotalText, 4, 0, 1, 2)
        self.labelConnectedNodesText = QtWidgets.QLabel(self.frame_6)
        self.labelConnectedNodesText.setObjectName("labelConnectedNodesText")
        self.gridLayout_5.addWidget(self.labelConnectedNodesText, 5, 0, 2, 2)
        self.labelChannelCountActiveText = QtWidgets.QLabel(self.frame_6)
        self.labelChannelCountActiveText.setObjectName("labelChannelCountActiveText")
        self.gridLayout_5.addWidget(self.labelChannelCountActiveText, 3, 0, 1, 2)
        self.labelConnectedNodes = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelConnectedNodes.setFont(font)
        self.labelConnectedNodes.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.labelConnectedNodes.setText("0")
        self.labelConnectedNodes.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelConnectedNodes.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelConnectedNodes.setObjectName("labelConnectedNodes")
        self.gridLayout_5.addWidget(self.labelConnectedNodes, 5, 2, 2, 1)
        self.labelChannelCountTotal = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelChannelCountTotal.setFont(font)
        self.labelChannelCountTotal.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.labelChannelCountTotal.setText("0")
        self.labelChannelCountTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelChannelCountTotal.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelChannelCountTotal.setObjectName("labelChannelCountTotal")
        self.gridLayout_5.addWidget(self.labelChannelCountTotal, 4, 2, 1, 1)
        self.labelAliasText = QtWidgets.QLabel(self.frame_6)
        self.labelAliasText.setObjectName("labelAliasText")
        self.gridLayout_5.addWidget(self.labelAliasText, 0, 0, 1, 2)
        self.labelChannelCountActive = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelChannelCountActive.setFont(font)
        self.labelChannelCountActive.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.labelChannelCountActive.setText("0")
        self.labelChannelCountActive.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelChannelCountActive.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelChannelCountActive.setObjectName("labelChannelCountActive")
        self.gridLayout_5.addWidget(self.labelChannelCountActive, 3, 2, 1, 1)
        self.labelAlias = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelAlias.setFont(font)
        self.labelAlias.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.labelAlias.setText("")
        self.labelAlias.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelAlias.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelAlias.setObjectName("labelAlias")
        self.gridLayout_5.addWidget(self.labelAlias, 0, 2, 1, 1)
        self.labelColorText = QtWidgets.QLabel(self.frame_6)
        self.labelColorText.setObjectName("labelColorText")
        self.gridLayout_5.addWidget(self.labelColorText, 1, 0, 1, 2)
        self.labelColor = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelColor.setFont(font)
        self.labelColor.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.labelColor.setText("#000000")
        self.labelColor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelColor.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelColor.setObjectName("labelColor")
        self.gridLayout_5.addWidget(self.labelColor, 1, 2, 1, 1)
        self.labelPublicKeyText = QtWidgets.QLabel(self.frame_6)
        self.labelPublicKeyText.setObjectName("labelPublicKeyText")
        self.gridLayout_5.addWidget(self.labelPublicKeyText, 2, 0, 1, 1)
        self.labelPublicKey = QtWidgets.QLabel(self.frame_6)
        self.labelPublicKey.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelPublicKey.setFont(font)
        self.labelPublicKey.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.labelPublicKey.setText("")
        self.labelPublicKey.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPublicKey.setWordWrap(True)
        self.labelPublicKey.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelPublicKey.setObjectName("labelPublicKey")
        self.gridLayout_5.addWidget(self.labelPublicKey, 2, 1, 1, 2)
        self.verticalLayout_12.addLayout(self.gridLayout_5)
        self.verticalLayout_11.addWidget(self.frame_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem3)
        self.horizontalLayout_7.addLayout(self.verticalLayout_11)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.retranslateUi(OverviewPage)
        QtCore.QMetaObject.connectSlotsByName(OverviewPage)

    def retranslateUi(self, OverviewPage):
        _translate = QtCore.QCoreApplication.translate
        OverviewPage.setWindowTitle(_translate("OverviewPage", "Form"))
        self.label_8.setText(_translate("OverviewPage", "Balances"))
        self.labelPendingLightning.setToolTip(_translate("OverviewPage", "Your total not yet locked on channels balance"))
        self.labelBalanceBitcoin.setToolTip(_translate("OverviewPage", "Your current on chain balance"))
        self.labelBalanceLightning.setToolTip(_translate("OverviewPage", "Your current on channels balance"))
        self.labelPending.setText(_translate("OverviewPage", "Pending:"))
        self.labelBitcoin.setText(_translate("OverviewPage", "Bitcoin:"))
        self.labelPendingBitcoin.setToolTip(_translate("OverviewPage", "Your total not yet confirmed on chain balance"))
        self.labelTotal.setText(_translate("OverviewPage", "Total:"))
        self.labelBitcoinTotal.setToolTip(_translate("OverviewPage", "Your total on chain balance"))
        self.labelLightningTotal.setToolTip(_translate("OverviewPage", "Your total on channels balance"))
        self.labelLightning.setText(_translate("OverviewPage", "Lightning:"))
        self.labelAvailable.setText(_translate("OverviewPage", "Available:"))
        self.labelLightningOverview.setText(_translate("OverviewPage", "Lightning overview"))
        self.labelChannelCountTotalText.setText(_translate("OverviewPage", "Channel count (total)"))
        self.labelConnectedNodesText.setText(_translate("OverviewPage", "Connected nodes count"))
        self.labelChannelCountActiveText.setText(_translate("OverviewPage", "Channel count (active)"))
        self.labelConnectedNodes.setToolTip(_translate("OverviewPage", "The number of other Lightning Network nodes you are connected to"))
        self.labelChannelCountTotal.setToolTip(_translate("OverviewPage", "The total number of Lightning Network channels"))
        self.labelAliasText.setText(_translate("OverviewPage", "Alias"))
        self.labelChannelCountActive.setToolTip(_translate("OverviewPage", "The number of active channels on the Lightning Network"))
        self.labelAlias.setToolTip(_translate("OverviewPage", "Your current alias on the Lightning Network"))
        self.labelColorText.setText(_translate("OverviewPage", "Color"))
        self.labelColor.setToolTip(_translate("OverviewPage", "Your current color on the Lightning Network"))
        self.labelPublicKeyText.setText(_translate("OverviewPage", "Public key"))
        self.labelPublicKey.setToolTip(_translate("OverviewPage", "Your Lightning Network public key (identifier)"))


