# This Python file uses the following encoding: utf-8
from PyQt5 import QtCore
from PyQt5 import QtWidgets
import sys

class Ui_HelpDialog(object):
    def setupUi(self, HelpDialog):
        HelpDialog.setObjectName("HelpDialog")
        HelpDialog.resize(518, 439)
        self.label = QtWidgets.QLabel(HelpDialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 501, 411))
        self.label.setObjectName("label")

        self.retranslateUi(HelpDialog)
        QtCore.QMetaObject.connectSlotsByName(HelpDialog)

    def retranslateUi(self, HelpDialog):
        _translate = QtCore.QCoreApplication.translate
        HelpDialog.setWindowTitle(_translate("HelpDialog", "帮助"))
        self.label.setText(_translate("HelpDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">情感分析系统 V1.0</span></p><p align=\"center\"><span style=\" font-size:14pt;\">作者：SuperChen</span></p><p align=\"center\"><span style=\" font-size:14pt;\">完工时间：2019/05/14</span></p><p align=\"center\"><span style=\" font-size:14pt;\">使用技术：TensorFlow，jieba等</span></p><p align=\"center\"><span style=\" font-size:14pt;\">使用机器学习框架：LSTM模型</span></p><p align=\"center\"><span style=\" font-size:14pt;\">程序模块：加载模块，用户输入，</span></p><p align=\"center\"><span style=\" font-size:14pt;\">              模型判断，帮助界面</span></p></body></html>"))
