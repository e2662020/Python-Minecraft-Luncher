'''
Usage:
  mine run <想要启动的我的世界版本号>
  mine install <想要下载的我的世界版本号>
  mine micr
  mine version
  mine v
  mine forge <forge版本> 
  mine gui
  mine help
  mine
  mine update
  mine setdir <目录>
'''
# 导库
from docopt import *
import minecraft_launcher_lib
import subprocess
import webbrowser
from typing import *
import IPython.display as ipd
import logging
import os
import requests

logging.basicConfig(filename="logs/launcher.log", level=logging.INFO)
logging.info("以下为CMD程序提供的日志")

# 设置启动地址
try:
    with open("./data/directory.pmldatafile", "r", encoding="UTF-16BE") as rf:
        minecraft_directory = rf.read()
except:
    minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
logging.info("成功加载MC路径")

try:
    minecraft_release_lib = []
    for i in minecraft_launcher_lib.utils.get_available_versions(minecraft_directory):
        minecraft_release_lib.append(i["id"])
except requests.exceptions.ConnectionError:
    minecraft_release_lib = ["网络错误"]
    logging.error("无法顺利连接网络,请检查代理服务器,调制解调器以及Internet是否连接")
    
try:
    current_max = 0


    def set_status(status: str):
        print(status)


    def set_progress(progress: int):
        if current_max != 0:
            print(f"{progress}/{current_max}")


    def set_max(new_max: int):
        global current_max
        current_max = new_max
        
    callback = {
        "setStatus": set_status,
        "setProgress": set_progress,
        "setMax": set_max
    }

    debug = True

    arguments = docopt(__doc__, options_first=True)
    # 设置minecraft目录为自动读取的默认目录
    # Set the minecraft directory to the default directory automatically read
    minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()

    # 启动minecraft
    # Run minecraft
    if arguments.get("run"):
        pass
        # 获取用户输入的版本号
        # Get the version number entered by the user
        lib = arguments['<想要启动的我的世界版本号>']
        options = minecraft_launcher_lib.utils.generate_test_options()  # 验证minecraft的存在 Verify the existence of minecraft
        subprocess.run(minecraft_launcher_lib.command.get_minecraft_command(lib, minecraft_directory,
                                                                            options))  # 获取命令,运行命令,启动游戏 Get the command, run the command, and start the game
        logging.info("启动minecraft,请移步到latest.log")
    # 下载minecraft
    # Download minecraft
    elif arguments.get("install"):
        lib = arguments[
            '<想要下载的我的世界版本号>']  # 获取用户输入的minecraft版本好 Get the minecraft version number entered by the user
        print("正在下载Minecraft",
              lib)  # 打印信息,给予用户安慰(如用户看的,提醒你,安装时间大约为3-5分钟) Print information to give users comfort (users see it, remind you that the installation time is about 3-5 minutes)
        minecraft_launcher_lib.install.install_minecraft_version(lib, minecraft_directory,
                                                                 callback=callback)  # 安装minecraft Install minecraft
        logging.info("下载Minecraft,请发来程序截图输出内容")

    # 微软登录,软件开发过程中,请勿使用
    # Microsoft login, please do not use during software development
    # 微软登录

    elif arguments.get("micr"):
        if debug == False:
            print("此功能正在潜心研发当中")
        elif debug == True:
            loginWebsite = minecraft_launcher_lib.microsoft_account.get_login_url(client_id="0e9621ea-900a-436e-a8a5-92c5bd41d938", redirect_uri="https://login.live.com/oauth20_desktop.srf")
            webbrowser.open(loginWebsite)
            accd = input("登录好后,请把最后的链接复制到这里")
            c = str(minecraft_launcher_lib.microsoft_account.get_auth_code_from_url(url=accd))
            print("检测到您的登录id是", c)
            minecraft_launcher_lib.microsoft_account.complete_login(client_id="0e9621ea-900a-436e-a8a5-92c5bd41d938", redirect_uri="https://login.live.com/oauth20_desktop.srf", auth_code=str(c))
            # print(minecraft_launcher_lib.microsoft_account.complete_login(client_id: , redirect_uri: str, auth_code: str, code_verifier: Optional[str]))
            # minecraft_directory.microsoft_account.complete_login(client_id="0e9621ea-900a-436e-a8a5-92c5bd41d938" , redirect_uri="https://login.live.com/oauth20_desktop.srf", auth_code="", code_verifier=Option([]))
    # 获取版本号
    elif arguments.get("version") or arguments.get("v"):
        print("alpha 0.01")

    # 初始化,下载最新版本的我的世界
    elif arguments.get("init"):
        lib = latest_release = minecraft_launcher_lib.utils.get_latest_version()["release"]
        minecraft_launcher_lib.install.install_minecraft_version(lib, minecraft_directory)

    # 安装forge,功能潜心研发之中
    elif arguments.get("forge"):
        if debug == True:
            print("此功能正在潜心研发当中")
        elif debug == True:
            lib = arguments['<forge版本>']
            version = minecraft_launcher_lib.forge.find_forge_version(lib)
            if version is None:
                print("没找到对应的Forge版本")
                exit()
            print("正在下载Forge", version)

            minecraft_launcher_lib.forge.install_forge_version(version, minecraft_directory)
    elif arguments.get("gui"):
        os.system("python3 ./QtGUI/mainwindow.py")
    elif arguments.get("help"):
        print("""Usage:
  python3 mine.py run <想要启动的我的世界版本号> #启动我的世界
  python3 mine.py install <想要下载的我的世界版本号> #下载我的世界
  python3 mine.py micr #微软登录
  python3 mine.py version #查询版本
  python3 mine.py setdir '<这里输入目录，别忘了带单引号>' #设置minecraft的安装目录
  python3 mine.py gui #启动GUI界面""")
    elif arguments.get("update"):
        webbrowser.open("http://github.com/e2662020/Python-Minecraft-Luncher/releases/")

    # 设置minecraft的安装目录
    # Set the installation directory of minecraft
    elif arguments.get("setdir"):
        minecraft_directory = arguments["<目录>"]
        with open("./data/directory.pmldatafile", "w", encoding="UTF-16BE") as f:
            f.write(minecraft_directory)
        logging.info("MC目录已成功写入文件")
        print("成功更改MC地址为", minecraft_directory)

except:
    import traceback

    e = traceback.format_exc()
    if debug == False:
        print(
            "程序又出错了,请将/logs文件夹的所有文件和mc的日志(" + minecraft_directory + "/logs/)打包发给他人给予分析(或者发给我:e2662020@outlook.com)(顺便说一下,我要上学,回复慢)")
    elif debug == True:
        print(e)
    logging.error("错误,Python输出:\n%s---------------", e)