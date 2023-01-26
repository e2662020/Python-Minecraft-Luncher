import logging
#设置日志
logging.basicConfig(filename="./logs/launcher.log", level=logging.INFO)
debug = True
logging.info("以下为GUI程序所提供日志")
try:    
    # 请使用utf-8编码打开
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
    import time
    import requests

    #设置启动地址
    try:
        with open("./data/directory.pmldatafile","r",encoding="UTF-16BE") as rf:
            minecraft_directory = rf.read()
    except:
        minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
    logging.info("成功加载MC路径")
    
    # 收集电脑里面安装的minecraft的版本号
    minecraft_install_lib = []
    for i in minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory):
        minecraft_install_lib.append(i["id"])

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

    try:
        minecraft_release_lib = []
        for i in minecraft_launcher_lib.utils.get_available_versions(minecraft_directory):
            minecraft_release_lib.append(i["id"])
    except requests.exceptions.ConnectionError:
        minecraft_release_lib = ["网络错误"]
        logging.error("无法顺利连接网络,请检查代理服务器,调制解调器以及Internet是否连接")

    class Stats:
        def __init__(self):
            # 从文件中加载UI定义
            path = os.path.realpath(os.curdir)#获取当前目录的绝对路径
            print(path)
            self.ui = QUiLoader().load(path+'/QtGUI/run.ui')
            # 初始化
            self.ui.label_5.setText("安装进度")
            self.ui.comboBox_2.addItems(minecraft_release_lib)
            self.ui.comboBox.addItems(minecraft_install_lib)
            self.ui.lineEdit.setText(minecraft_directory)
            # 错误展示
            if minecraft_release_lib == ["网络错误"]:
                self.ui.pushButton.setText("无法下载")
                self.ui.label_6.setText("请检查代理服务器,调制解调器以及Internet是否连接后重新启动该软件")
            # 连接信号
            self.ui.pushButton_3.clicked.connect(self.RunMinecraft)
            self.ui.pushButton.clicked.connect(self.InstallMinecraft)
            self.ui.pushButton_2.clicked.connect(self.setDirectory)
            self.ui.pushButton_4.clicked.connect(self.installForge)

        def RunMinecraft(self):
            # 获取用户输入的版本号
            # Get the version number entered by the user
            lib = self.ui.comboBox.currentText()
            # self.ui.comboBox.
            options = minecraft_launcher_lib.utils.generate_test_options()  # 验证minecraft的存在 Verify the existence of minecraft
            subprocess.run(minecraft_launcher_lib.command.get_minecraft_command(lib, minecraft_directory,options))  # 获取命令,运行命令,启动游戏 Get the command, run the command, and start the game
            logging.info("启动minecraft,请移步到latest.log")

        def InstallMinecraft(self):
            #定义现在发行的版本号
            lib = self.ui.comboBox_2.currentText()
            self.ui.label_5.setText("正在下载")
            self.ui.label_5.repaint()
            logging.info("下载Minecraft")
            minecraft_launcher_lib.install.install_minecraft_version(lib, minecraft_directory,callback=callback)  # 安装minecraft Install minecraft
            self.ui.label_5.setText("下载完成")
            logging.info("下载完成")
            self.ui.label_5.repaint()

        def setDirectory(self):
            minecraft_directory = self.ui.lineEdit.text()
            with open("./data/directory.pmldatafile","w", encoding="UTF-16BE") as f:
                f.write(minecraft_directory)
            logging.info("MC目录已成功写入文件")
            self.ui.pushButton_2.setText("成功更改")
        
        def installForge(self):
            modVersion = self.ui.lineEdit_2.text()
            forge_version = minecraft_launcher_lib.forge.find_forge_version(modVersion)
            if forge_version is None:
                self.ui.label_3.setText("没有这个版本")
            else:
                minecraft_launcher_lib.forge.install_forge_version(forge_version, minecraft_directory)
        def installFabric(self):
            modVersion = self.ui.lineEdit_2.text()
            minecraft_launcher_lib.fabric.install_fabric(modVersion, minecraft_directoy)

    app = QApplication([])
    stats = Stats()
    stats.ui.show()
    app.exec_()
except:
    import traceback

    e = traceback.format_exc()
    if debug == False:
        print(
            "程序又出错了,请将/logs文件夹的所有文件和mc的日志(" + minecraft_directory + "/logs/)打包发给他人给予分析(或者发给我:e2662020@outlook.com)(顺便说一下,我要上学,回复慢)")
    elif debug == True:
        print(e)
    logging.error("错误,Python输出:\n%s---------------", e)