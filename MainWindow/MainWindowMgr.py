# coding=utf8

import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot
from MainWindow.MainWindow import Ui_MainWindow
from DictionaryEditer.DictionaryEditerMgr import DictionaryEditerMgr
from unrar import rarfile


class MainWindowMgr(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        """构造方法"""

        # 父类方法
        QtWidgets.QWidget.__init__(self, parent)

        # 字典编辑窗口
        self.__dictEditer = DictionaryEditerMgr()

        # 创建界面
        self.setupUi(self)  # 创建界面

        # 获取需要解压的文件的槽函数链接
        self.btnBrowseForFile.clicked.connect(self.onBtnBrowseForFileClicked)

        # 打开字典按钮的槽函数链接
        self.btnEditDict.clicked.connect(self.onBtnEditDictClicked)

        # 启动按钮槽函数链接
        self.btnStart.clicked.connect(self.onBtnStartClicked)

    @pyqtSlot()
    def onBtnBrowseForFileClicked(self):
        """点击浏览，获取需要解压的文件所在路径"""

        # 打开文件对话框
        (filePath, fileType) = QFileDialog.getOpenFileName(self, u"打开需要解压的文件", u"./", u"压缩文件(*.rar)")

        # 判断打开的是否是WinRAR.exe文件如果非法，警告并清空
        fileName = filePath.split("/")[-1]
        if "rar" in fileName or "zip" in fileName:
            self.lineEditForFile.setText(filePath)
        else:
            QMessageBox.warning(self,"错误", "请选择一个压缩文件", QMessageBox.Cancel, None)
            self.lineEditForFile.clear()

    @pyqtSlot()
    def onBtnEditDictClicked(self):
        """点击按钮，将字典编辑界面显示出来"""
        if self.__dictEditer is None:
            return
        self.__dictEditer.show()

    @pyqtSlot()
    def onBtnStartClicked(self):
        """点击启动，开始进行密码破解尝试"""

        # 获取当前的解压文件路径
        file = self.lineEditForFile.text()
        if len(file) == 0:
            return

        # 加载文件
        fp = rarfile.RarFile(file)

        # 获取密码字典
        dict = self.__dictEditer.getDict()

        # 解压文件
        fp.extractall(path='.\\', pwd=dict)
