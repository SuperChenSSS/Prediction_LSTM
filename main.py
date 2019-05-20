# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sentiment.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from sentiment_analysis import PreData
from PyQt5.QtWidgets import QMessageBox, QDialog, QFileDialog
from PyQt5.QtCore import QObject , pyqtSignal
from Help import *
import sys

class Ui_Sentiment(object):
    def setupUi(self, Sentiment):
        self.Sentiment = Sentiment

        Sentiment.setObjectName("Sentiment")
        Sentiment.resize(808, 425)
        self.centralWidget = QtWidgets.QWidget(Sentiment)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 791, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(190, 70, 421, 271))
        self.textEdit.setObjectName("textEdit")

        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(652, 170, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.onButtonClick());

        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 151, 21))
        self.tabWidget.setObjectName("tabWidget")

        self.tabWidget.tabBarClicked.connect(self.showHelp)


        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        Sentiment.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(Sentiment)
        self.mainToolBar.setObjectName("mainToolBar")
        Sentiment.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(Sentiment)
        self.statusBar.setObjectName("statusBar")
        Sentiment.setStatusBar(self.statusBar)

        self.retranslateUi(Sentiment)
        QtCore.QMetaObject.connectSlotsByName(Sentiment)

    def showHelp(self,i):
        if i == 1:
            help = QtWidgets.QDialog()
            ui = Ui_HelpDialog()
            ui.setupUi(help)
            help.show()
            help.exec_()
        else:
            filePath = QFileDialog.getOpenFileName(self.Sentiment,"打开模型",
            "/Users/superchen/Qt_Project/TestPyQt/sentiment_analysis/model/","Model Files (*.meta)")
            if filePath[0] != "" and filePath[1] != "":
                QMessageBox.information(self.Sentiment,"成功","已成功定位并添加该模型!",QMessageBox.Ok)
            else:
                QMessageBox.critical(self.Sentiment,"错误","您没有成功添加模型!",QMessageBox.Ok)

    def onButtonClick(self):
        input = self.textEdit.toPlainText()
        output = PreData.run(input)
        QMessageBox.information(self.Sentiment, "信息提示框", output, QMessageBox.Ok)

    def retranslateUi(self, Sentiment):
        _translate = QtCore.QCoreApplication.translate
        Sentiment.setWindowTitle(_translate("Sentiment", "情感分析系统"))
        self.label.setText(_translate("Sentiment", "情感分析系统"))
        self.textEdit.setHtml(_translate("Sentiment", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.pushButton.setText(_translate("Sentiment", "情感分析"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Sentiment", " 添加模型"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Sentiment", "  帮助   "))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Sentiment()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

