# coding=utf8

import sys
from PyQt5.QtWidgets import QApplication
from MainWindow.MainWindowMgr import MainWindowMgr


def main():
    # 创建事件
    app = QApplication(sys.argv)

    # 创建ui
    ui = MainWindowMgr()

    # 显示ui界面
    ui.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
