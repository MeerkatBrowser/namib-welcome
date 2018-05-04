#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QDesktopWidget
import webbrowser
import os
import subprocess

class Ui_WelcomeScreen(object):
    def forumButtonAction(self):
        webbrowser.open("https://forum.meerkat.tk/forums/")
    def ircButtonAction(self):
        webbrowser.open("https://namib.meerkat.tk/support/chat/")
    def donateButtonAction(self):
        webbrowser.open("https://namib.meerkat.tk/donate/")
    def wikiButtonAction(self):
        webbrowser.open("https://wiki.archlinux.org/")
    def newsButtonAction(self):
        webbrowser.open("https://forum.meerkat.tk/")
    def helpButtonAction(self):
        webbrowser.open("https://github.com/meerkatbrowser")
    def installButtonAction(self):
        subprocess.Popen(["pkexec", "calamares"])
    def startCheckAction(self):
        if self.startCheck.isChecked():
            homedir = os.path.expanduser('~')
            autostartfile = os.path.join(homedir, ".config/autostart/namib-welcome.desktop")
            subprocess.Popen(["cp", "/usr/share/applications/namib-welcome.desktop", autostartfile])
        else:
            homedir = os.path.expanduser('~')
            autostartfile = os.path.join(homedir, ".config/autostart/namib-welcome.desktop")
            subprocess.Popen(["rm", autostartfile])


    def setupUi(self, WelcomeScreen):
        WelcomeScreen.setObjectName("WelcomeScreen")
        WelcomeScreen.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WelcomeScreen.sizePolicy().hasHeightForWidth())
        WelcomeScreen.setSizePolicy(sizePolicy)
        WelcomeScreen.setMinimumSize(QtCore.QSize(640, 471))
        WelcomeScreen.setMaximumSize(QtCore.QSize(640, 493))
        WelcomeScreen.setFixedSize(640, 477)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/usr/share/icons/namib-welcome.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WelcomeScreen.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(WelcomeScreen)
        self.centralwidget.setMinimumSize(QtCore.QSize(640, 471))
        self.centralwidget.setMaximumSize(QtCore.QSize(640, 471))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 210, 641, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.linkLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.linkLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.linkLayout.setContentsMargins(0, 0, 0, 0)
        self.linkLayout.setHorizontalSpacing(6)
        self.linkLayout.setObjectName("linkLayout")
        self.helpButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.helpButton.setObjectName("helpButton")
        ######################### HELP BUTTON #########################
        self.helpButton.clicked.connect(self.helpButtonAction)
        ###############################################################
        self.linkLayout.addWidget(self.helpButton, 1, 2, 1, 1)
        self.ircButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ircButton.setObjectName("ircButton")
        ######################### IRC BUTTON ##########################
        self.ircButton.clicked.connect(self.ircButtonAction)
        ###############################################################
        self.linkLayout.addWidget(self.ircButton, 2, 1, 1, 1)
        self.newsButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.newsButton.setObjectName("newsButton")
        ######################### NEWS BUTTON ##########################
        self.newsButton.clicked.connect(self.newsButtonAction)
        ################################################################
        self.linkLayout.addWidget(self.newsButton, 1, 0, 1, 1)
        self.donateButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.donateButton.setObjectName("donateButton")
        ######################### DONATE BUTTON ########################
        self.donateButton.clicked.connect(self.donateButtonAction)
        ################################################################
        self.linkLayout.addWidget(self.donateButton, 2, 2, 1, 1)
        self.wikiButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.wikiButton.setObjectName("wikiButton")
        ######################### WIKI BUTTON ##########################
        self.wikiButton.clicked.connect(self.wikiButtonAction)
        ################################################################
        self.linkLayout.addWidget(self.wikiButton, 2, 0, 1, 1)
        self.forumButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.forumButton.setObjectName("forumButton")
        ######################### FORUM BUTTON #########################
        self.forumButton.clicked.connect(self.forumButtonAction)
        ################################################################
        self.linkLayout.addWidget(self.forumButton, 1, 1, 1, 1)
        self.linksLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.linksLabel.setMaximumSize(QtCore.QSize(16777215, 14))
        self.linksLabel.setScaledContents(True)
        self.linksLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.linksLabel.setWordWrap(True)
        self.linksLabel.setObjectName("linksLabel")
        self.linkLayout.addWidget(self.linksLabel, 0, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 440, 641, 35))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.startCheck = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.startCheck.setChecked(False)
        ######################### FORUM BUTTON #########################
        self.startCheck.clicked.connect(self.startCheckAction)
        ################################################################
        self.startCheck.setObjectName("startCheck")
        self.horizontalLayout.addWidget(self.startCheck)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 641, 211))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.infoLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.infoLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.infoLayout.setContentsMargins(0, 0, 0, 0)
        self.infoLayout.setObjectName("infoLayout")
        self.line = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.infoLayout.addWidget(self.line, 3, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.infoLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.iconLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.iconLabel.setMaximumSize(QtCore.QSize(64, 64))
        self.iconLabel.setText("")
        self.iconLabel.setPixmap(QtGui.QPixmap("/usr/share/icons/namib-welcome.png"))
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setObjectName("iconLabel")
        self.infoLayout.addWidget(self.iconLabel, 0, 1, 1, 1)
        self.infoLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.infoLabel.setScaledContents(True)
        self.infoLabel.setWordWrap(True)
        self.infoLabel.setObjectName("infoLabel")
        self.infoLayout.addWidget(self.infoLabel, 2, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.infoLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.welcomeLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.welcomeLabel.setTextFormat(QtCore.Qt.RichText)
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.infoLayout.addWidget(self.welcomeLabel, 1, 0, 1, 3)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 360, 641, 81))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.installButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.installButton.setObjectName("installButton")
        ######################### INSTALL BUTTON ##########################
        self.installButton.clicked.connect(self.installButtonAction)
        self.installButton.setVisible(False)
        ###################################################################
        self.gridLayout_3.addWidget(self.installButton, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 1, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 2, 0, 1, 3)
        self.installLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.installLabel.setScaledContents(True)
        self.installLabel.setWordWrap(True)
        self.installLabel.setObjectName("installLabel")
        ######################### INSTALL LABEL ##########################
        self.installLabel.setVisible(False)
        ##################################################################
        self.gridLayout_3.addWidget(self.installLabel, 0, 1, 1, 1)
        WelcomeScreen.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WelcomeScreen)
        self.statusbar.setObjectName("statusbar")
        WelcomeScreen.setStatusBar(self.statusbar)

        self.retranslateUi(WelcomeScreen)
        QtCore.QMetaObject.connectSlotsByName(WelcomeScreen)

        ######################### LIVEUSER ? ##########################
        if os.path.isfile("/usr/bin/calamares_polkit"):
            self.installButton.setVisible(True)
            self.installLabel.setVisible(True)
        ###############################################################

        ######################### IS AUTOSTART ? ######################
        homedir = os.path.expanduser('~')
        autostartfile = os.path.join(homedir, ".config/autostart/namib-welcome.desktop")
        if os.path.isfile(autostartfile):
            self.startCheck.setChecked(True)
        ###############################################################

    def retranslateUi(self, WelcomeScreen):
        _translate = QtCore.QCoreApplication.translate
        WelcomeScreen.setWindowTitle(_translate("WelcomeScreen", "Welcome Screen"))
        self.helpButton.setText(_translate("WelcomeScreen", "Help us"))
        self.ircButton.setText(_translate("WelcomeScreen", "Chat room"))
        self.newsButton.setText(_translate("WelcomeScreen", "News"))
        self.donateButton.setText(_translate("WelcomeScreen", "Donate"))
        self.wikiButton.setText(_translate("WelcomeScreen", "Wiki"))
        self.forumButton.setText(_translate("WelcomeScreen", "Forums"))
        self.linksLabel.setText(_translate("WelcomeScreen", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">LINKS :</span></p></body></html>"))
        self.startCheck.setText(_translate("WelcomeScreen", "Launch at start"))
        self.infoLabel.setText(_translate("WelcomeScreen", "<html><head/><body><p align=\"center\">Welcome to Namib GNU/Linux. The links below will help you get started with Namib. So enjoy the experience, and don\'t hesitate to send us your feedback</p></body></html>"))
        self.welcomeLabel.setText(_translate("WelcomeScreen", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Welcome to Namib GNU/Linux !</span></p></body></html>"))
        self.installButton.setText(_translate("WelcomeScreen", "Install Now"))
        self.installLabel.setText(_translate("WelcomeScreen", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">INSTALLATION :</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomeScreen = QtWidgets.QMainWindow()
    ui = Ui_WelcomeScreen()
    ui.setupUi(WelcomeScreen)
    WelcomeScreen.show()
    sys.exit(app.exec_())

