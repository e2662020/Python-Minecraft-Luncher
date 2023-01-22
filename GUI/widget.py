# This Python file uses the following encoding: utf-8
import sys
import os
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader

class Stats:

    def __init__(self):
        # 从文件中加载UI定义
        path = os.path.realpath(os.curdir)#获取当前目录的绝对路径
        print(path)
        self.ui = QUiLoader().load(path+'/form.ui')

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()



