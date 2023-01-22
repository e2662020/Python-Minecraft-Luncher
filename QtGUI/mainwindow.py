# This Python file uses the following encoding: utf-8
import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader
from docopt import *
import minecraft_launcher_lib
import subprocess
import webbrowser
from typing import *
import IPython.display as ipd
import logging
import time

# 收集电脑里面安装的minecraft的版本号
minecraft_install_lib = []
logging.basicConfig(filename="logs/launcher.log", level=logging.INFO)
minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
for i in minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory):
    minecraft_install_lib.append(i["id"])
print(minecraft_install_lib)

#定义现在发行的版本号
minecraft_release_lib = []
for i in minecraft_launcher_lib.utils.get_available_versions(minecraft_directory):
    minecraft_release_lib.append(i["id"])
print(minecraft_release_lib)

current_max = 0


def set_status(status: str):
    print(status)


def set_progress(progress: int):
    if current_max != 0:
        print(f"{progress}/{current_max}")


def set_max(new_max: int):
    global current_max
    current_max = new_max
    
# 定义返回安装进度的函数
callback = {
    "setStatus": set_status,
    "setProgress": set_progress,
    "setMax": set_max
}

class Stats:
    def __init__(self):
        # 从文件中加载UI定义
        path = os.path.realpath(os.curdir)#获取当前目录的绝对路径
        print(path)
        self.ui = QUiLoader().load(path+'/run.ui')
        # 初始化
        self.ui.label_5.setText("安装进度")
        self.ui.comboBox_2.addItems(minecraft_release_lib)
        self.ui.comboBox.addItems(minecraft_install_lib)
        # 连接信号
        self.ui.pushButton_3.clicked.connect(self.RunMinecraft)
        self.ui.pushButton.clicked.connect(self.InstallMinecraft)

    def RunMinecraft(self):
        
        # 获取用户输入的版本号
        # Get the version number entered by the user
        lib = self.ui.comboBox.currentText()
        # self.ui.comboBox.
        options = minecraft_launcher_lib.utils.generate_test_options()  # 验证minecraft的存在 Verify the existence of minecraft
        subprocess.run(minecraft_launcher_lib.command.get_minecraft_command(lib, minecraft_directory,options))  # 获取命令，运行命令，启动游戏 Get the command, run the command, and start the game
        logging.info("启动minecraft，请移步到latest.log")
        quit()

    def InstallMinecraft(self):
        lib = self.ui.comboBox_2.currentText()
        self.ui.label_5.setText("正在下载")
        self.ui.label_5.repaint()
        logging.info("下载Minecraft")
        minecraft_launcher_lib.install.install_minecraft_version(lib, minecraft_directory,callback=callback)  # 安装minecraft Install minecraft
        self.ui.label_5.setText("下载完成")
        self.ui.label_5.repaint()
    
app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()



