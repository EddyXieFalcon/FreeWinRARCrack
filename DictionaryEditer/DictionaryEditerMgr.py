# coding=utf8

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QTableWidgetItem
from DictionaryEditer.DictionaryEditer import Ui_DictionaryEditer


class DictionaryEditerMgr(QtWidgets.QWidget, Ui_DictionaryEditer):
    def __init__(self, parent=None):
        """构造方法"""

        # 父类方法
        QtWidgets.QWidget.__init__(self, parent)

        # 准备字典
        self.__numberList = \
            ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.__capitalizationlist = \
            ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
             "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"]
        self.__lowerCaseList = \
            ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
             "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
             "u", "v", "w", "x", "y", "z"]
        self.__anthoerList = \
            ["\"", "\\", ",", ".", "/", ";", "'", "[", "]", "`",
             "-", "=", "<", ">", "?", ":", "|", "~", "!", "@",
             "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"]

        # 创建界面
        self.setupUi(self)  # 创建界面

        # 连接所有的信号与槽函数
        self.spinBoxMin.editingFinished.connect(self.onSpinboxMinEditingFinished)
        self.spinBoxMax.editingFinished.connect(self.onSpinboxMaxEditingFinished)

        self.checkBoxIsIncludeSpace.clicked.connect(self.onCheckBoxIsIncludeSpaceClicked)
        self.checkBoxIsIncludeNumber.clicked.connect(self.onCheckBoxIsIncludeNumberClicked)
        self.checkBoxIsIncludeCapitalization.clicked.connect(self.onCheckBoxIsIncludeCapitalizationClicked)
        self.checkBoxIsIncludeLowerCase.clicked.connect(self.onCheckBoxIsIncludeLowerCaseClicked)
        self.checkBoxIsIncludeAll.clicked.connect(self.onCheckBoxIsIncludeAllClicked)

        self.btnAdd.clicked.connect(self.onBtnAddClicked)
        self.btnRemove.clicked.connect(self.onBtnRemoveClicked)

    @pyqtSlot()
    def onSpinboxMinEditingFinished(self):
        """当用户编辑完最最小值之后，需要判断，该数值是否合法"""

        # 判断用户设置的最大值是否小于最小值
        if self.spinBoxMin.value() < self.spinBoxMax.value():
            self.spinBoxMin.setValue(self.spinBoxMax.value())

    @pyqtSlot()
    def onSpinboxMaxEditingFinished(self):
        """当用户编辑完最大值之后，需要判断，该数值是否合法"""

        # 判断用户设置的最大值是否小于最小值
        if self.spinBoxMin.value() > self.spinBoxMax.value():
            self.spinBoxMax.setValue(self.spinBoxMin.value())

    @pyqtSlot()
    def onCheckBoxIsIncludeSpaceClicked(self):
        """判断是否包含空格的字符是否被勾选"""

        if self.checkBoxIsIncludeAll.isEnabled():
            self.addStringToTable(" ")
        else:
            self.removeStringToTable(" ")

    @pyqtSlot()
    def onCheckBoxIsIncludeNumberClicked(self):
        """判断是否包含数字的字符是否被勾选"""

        if self.checkBoxIsIncludeAll.isEnabled():
            self.addListToTable(self.__numberList)
        else:
            self.removeListToTable(self.__numberList)

    @pyqtSlot()
    def onCheckBoxIsIncludeCapitalizationClicked(self):
        """判断是否包含大写字母的字符是否被勾选"""

        if self.checkBoxIsIncludeAll.isEnabled():
            self.addListToTable(self.__capitalizationlist)
        else:
            self.removeListToTable(self.__capitalizationlist)

    @pyqtSlot()
    def onCheckBoxIsIncludeLowerCaseClicked(self):
        """判断是否包含小写字母的字符是否被勾选"""

        if self.checkBoxIsIncludeAll.isEnabled():
            self.addListToTable(self.__lowerCaseList)
        else:
            self.removeListToTable(self.__lowerCaseList)

    @pyqtSlot()
    def onCheckBoxIsIncludeAllClicked(self):
        """判断是否包含所有的字符是否被勾选"""

        if self.checkBoxIsIncludeAll.isEnabled():
            self.addListToTable(self.__numberList)
            self.addListToTable(self.__capitalizationlist)
            self.addListToTable(self.__lowerCaseList)
            self.addListToTable(self.__anthoerList)
            self.addStringToTable(" ")
        else:
            self.removeListToTable(self.__numberList)
            self.removeListToTable(self.__capitalizationlist)
            self.removeListToTable(self.__lowerCaseList)
            self.removeListToTable(self.__anthoerList)
            self.removeStringToTable(" ")

    @pyqtSlot()
    def onBtnAddClicked(self):
        """添加一个字典值"""

        # 弹出一个对话框，要求用户输入一个字典值
        (name, mark) = QInputDialog.getText(self, u"输入一个字符串", u"字符串：", QLineEdit.Normal, u"")

        # 判断该值是否已经在例表中，或者用户没有给予合法的输入值
        if not mark:
            return
        self.addStringToTable(name)

        # 将用户添加的值追加如字典列表
        self.addStringToTable(name)

    @pyqtSlot()
    def onBtnRemoveClicked(self):
        """删除一个字典值"""

        # 如果当前没有选中的项，不执行本函数
        if self.tableWidgetDict.currentRow() < 0:
            return

        # 删除选中项
        self.tableWidgetDict.removeRow(self.tableWidgetDict.currentRow())

    def addListToTable(self, list):
        """为字典列表添加当前传参进入的数据"""

        # 遍历列表中的每一个元素，依次添加到界面的字典列表中
        for string in list:
            self.addStringToTable(string)

    def addStringToTable(self, string):
        """添加传参进入的字符到界面的字典列表中"""

        # 查找该字符是否已经包含在界面列表中
        resltList = self.tableWidgetDict.findItems(string, Qt.MatchFlag(0))
        if len(resltList) <= 0:
            return

        # 将字典添加到界面中的字典列表中
        self.tableWidgetDict.setRowCount(self.tableWidgetDict.rowCount() + 1)
        self.tableWidgetDict.setItem(self.tableWidgetDict.rowCount() - 1, 0, QTableWidgetItem(string))

    def removeListToTable(self, list):
        """为字典列表删除当前传参进入的数据"""

        # 遍历列表中的每一个元素，依次添加到界面的字典列表中
        for string in list:
            self.removeStringToTable(string)

    def removeStringToTable(self, string):
        """删除传参进入的字符到界面的字典列表中"""

        # 查找该字符是否已经包含在界面列表中
        resltList = self.tableWidgetDict.findItems(string, Qt.MatchFlag(0))
        if len(resltList) <= 0:
            return

        # 将字典从界面中的字典列表中删除
        for item in resltList:
            self.tableWidgetDict.removeRow(item.row())

    def getMinAndMax(self):
        """获取设置的字典的最小值与最大值"""
        return self.spinBoxMin.value(), self.spinBoxMax.value()

    def getDict(self):
        """依据当前界面的设计，返回一个密码字段"""

        # 如果界面表为空，返回一个空表
        if 0 >= self.tableWidgetDict.rowCount():
            return []

        # 界面所有的数据，然后组装表返回
        else:
            dictList = ''
            for rowIndex in range(self.tableWidgetDict.rowCount()):
                dictList = dictList + self.tableWidgetDict.item(rowIndex, 0).text()

            return dictList

