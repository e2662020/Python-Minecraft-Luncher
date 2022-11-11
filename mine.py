# 定义我们将要是用到的命令用来操控这个
'''
Usage:
  python3 mine.py run <想要启动的我的世界版本号>
  python3 mine.py install <想要下载的我的世界版本号>
  python3 mine.py micr     #开发中功能
  python3 mine.py version
  python3 mine.py v
  python3 mine.py forge <forge版本>      #开发中功能
'''
#导库
from docopt import *
import minecraft_launcher_lib
import subprocess
import webbrowser
from typing import *
import IPython.display as ipd
import logging

logging.basicConfig(filename="logs/launcher.log",level = logging.INFO)

try:    
    # 逝世功能（看成百宝箱），功能作用：就是播放音乐
    # def a():
    #     ipd.Audio("1.wav")

    
    debug = False #开发人员请将False改为True已触发开发中的功能，如果您是正常使用请不要动。

    current_max = 0


    def set_status(status: str):
        print(status)


    def set_progress(progress: int):
        if current_max != 0:
            print(f"{progress}/{current_max}")


    def set_max(new_max: int):
        global current_max
        current_max = new_max


    minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()

    callback = {
        "setStatus": set_status,
        "setProgress": set_progress,
        "setMax": set_max
    }

    arguments = docopt(__doc__,options_first=True)
    #设置minecraft目录为自动读取的默认目录
    minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()

    #启动minecraft
    if arguments.get("run"):
        lib = arguments['<想要启动的我的世界版本号>'] #获取用户输入的版本号
        options = minecraft_launcher_lib.utils.generate_test_options() #验证minecraft的存在
        subprocess.run(minecraft_launcher_lib.command.get_minecraft_command(lib, minecraft_directory, options))#获取命令，运行命令，启动游戏
        logging.info("启动minecraft，请移步到latest.log")
    #下载minecraft
    elif arguments.get("install"):
        lib = arguments['<想要下载的我的世界版本号>']#获取用户输入的minecraft版本好
        print("正在下载Minecraft",lib)#打印信息，给予用户安慰（如用户看的，提醒你，安装时间大约为3-5分钟）
        minecraft_launcher_lib.install.install_minecraft_version(lib, minecraft_directory,callback=callback) #安装minecraft
        
        logging.info("下载Minecraft，请发来程序截图输出内容")

    # 微软登录，软件开发过程中，请勿使用
    elif arguments.get("micr"):
        if debug == False:
            print("此功能正在潜心研发当中")
        elif debug == True:  
            a = minecraft_launcher_lib.microsoft_account.get_login_url(client_id="0e9621ea-900a-436e-a8a5-92c5bd41d938",redirect_uri = "https://login.live.com/oauth20_desktop.srf")
            print(a)
            webbrowser.open(a)
            accd=input("登录好后，请把最后的链接复制到这里")
            c = str(minecraft_launcher_lib.microsoft_account.get_auth_code_from_url(url=accd))
            print("检测到您的id是",c)
            # print(minecraft_launcher_lib.microsoft_account.complete_login(client_id: , redirect_uri: str, auth_code: str, code_verifier: Optional[str]))
            # minecraft_directory.microsoft_account.complete_login(client_id="0e9621ea-900a-436e-a8a5-92c5bd41d938" , redirect_uri="https://login.live.com/oauth20_desktop.srf", auth_code="", code_verifier=Option([]))
    #获取版本号
    elif arguments.get("version") or arguments.get("v"):
        print("alpha 0.0.1")

    #初始化，下载最新版本的我的世界
    elif arguments.get("init"):
        lib = latest_release = minecraft_launcher_lib.utils.get_latest_version()["release"]
        minecraft_launcher_lib.install.install_minecraft_version(lib, minecraft_directory)

    #安装forge，功能潜心研发之中
    elif arguments.get("forge"):
        if debug == False:
            print("此功能正在潜心研发当中")
        elif debug == True:    
            lib = arguments['<forge版本>']
            version = minecraft_launcher_lib.forge.find_forge_version(lib)
            if version is None:
                print("没找到对应的Forge版本")
                exit()
            print("正在下载Forge",version)

            minecraft_launcher_lib.forge.install_forge_version(version, minecraft_directory)

except:
    import traceback
    e = traceback.format_exc()
    print("程序又出错了，请将/logs文件夹的所有文件和mc的日志（"+minecraft_directory+"/logs/）打包发给他人给予分析（或者发给我：e2662020@outlook.com）（顺便说一下，我要上学，回复慢）")
    logging.error("错误,Python输出:\n%s---------------",e)
