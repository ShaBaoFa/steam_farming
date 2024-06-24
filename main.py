import win32gui
import win32api
import win32con
import psutil
import os
import time
import pyautogui
import pyperclip
import pygetwindow as gw


def kill_steam():
    """
    Kill the Steam application.
    """
    try:
        # Check if Steam is running
        if is_application_running('steam.exe'):
            print("Killing Steam...")
            # Kill the Steam application
            os.system("taskkill /f /im steam.exe")
        else:
            print("Steam is not running.")
    except Exception as e:
        print(f"Failed to kill Steam. Reason: {e}")


def kill_games(game):
    """
    Kill the Egg application.
    """
    try:
        # Check if Steam is running
        if is_application_running(f'{game}.exe'):
            print("Killing Egg...")
            # Kill the Steam application
            os.system(f"taskkill /f /im {game}.exe")
        else:
            print(f"{game} is not running.")
    except Exception as e:
        print(f"Failed to kill {game}. Reason: {e}")


def open_steam():
    """
    Open the Steam application.
    """
    try:
        # Check if Steam is already running
        while steam_exists():
            print("Steam is already running.")
            # 关闭steam
            kill_steam()
            # Wait for Steam to close
            print("Waiting for Steam to close...")
            time.sleep(5)
        # Open the Steam application
        print("Opening Steam...")
        win32api.ShellExecute(0, 'open', 'steam://', None, None, win32con.SW_SHOWNORMAL)
    except Exception as e:
        print(f"Failed to open Steam. Reason: {e}")


def delete_files_in_directory(directory):
    """
    Delete all files in the specified directory.
    """
    try:
        # Check if the directory exists
        if os.path.exists(directory) and os.path.isdir(directory):
            # List all files and directories in the given directory
            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)
                try:
                    # Check if it's a file and delete it
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        print(f"Deleted file: {file_path}")
                    # Optionally: if it's a directory, you can also remove it
                    # elif os.path.isdir(file_path):
                    #     shutil.rmtree(file_path)
                    #     print(f"Deleted directory: {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}. Reason: {e}")
        else:
            print(f"Directory {directory} does not exist or is not a directory.")
    except Exception as e:
        print(f"Error accessing the directory {directory}. Reason: {e}")


def is_application_running(app_name):
    """
    Check if there is any running application that matches the given name.
    """
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Check if the process name matches
            if proc.info['name'] and proc.info['name'].lower() == app_name.lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def steam_exists():
    return win32gui.FindWindow(None, 'Steam') != 0


def show_sda_window():
    # 根据窗口标题查找窗口
    hwnd = win32gui.FindWindow(None, 'Steam桌面验证器（海盗海汉化）')

    if hwnd:
        # 如果窗口被最小化，恢复它
        if win32gui.IsIconic(hwnd):
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

        # 将窗口带到前台
        win32gui.SetForegroundWindow(hwnd)
        print("Steam Desktop Authenticator window has been brought to the front.")
    else:
        print("Steam Desktop Authenticator window not found.")


def show_steam_window():
    # 根据窗口标题查找窗口
    hwnd = win32gui.FindWindow(None, 'Steam')

    if hwnd:
        # 如果窗口被最小化，恢复它
        if win32gui.IsIconic(hwnd):
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

        # 将窗口带到前台
        win32gui.SetForegroundWindow(hwnd)
        print("Steam window has been brought to the front.")
    else:
        print("Steam window not found.")


def show_games_window(game):
    # 根据窗口标题查找窗口
    hwnd = win32gui.FindWindow(None, game)

    if hwnd:
        # 如果窗口被最小化，恢复它
        if win32gui.IsIconic(hwnd):
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

        # 将窗口带到前台
        win32gui.SetForegroundWindow(hwnd)
        print(f"{game} window has been brought to the front.")
    else:
        print(f"{game} window not found.")


def show_sign_steam_window():
    # 根据窗口标题查找窗口
    hwnd = win32gui.FindWindow(None, 'Sign in to Steam')

    if hwnd:
        # 如果窗口被最小化，恢复它
        if win32gui.IsIconic(hwnd):
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

        # 将窗口带到前台
        win32gui.SetForegroundWindow(hwnd)
        print("Steam window has been brought to the front.")
    else:
        print("Steam window not found.")


def type_sda_code():
    """
    Type the Steam Guard code from the authenticator app.
    """
    # 显示sda桌面
    show_sda_window()
    x, y = find_pic('sda_code_search.png')
    pyautogui.click(x + 100, y, duration=0.25)
    # 清除当前对话框
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    # 确保焦点
    pyautogui.click(x + 100, y, duration=0.25)
    # 复制username
    pyperclip.copy(username)
    pyautogui.hotkey('ctrl', 'v')
    # 移动到账户名激活账户信息
    pyautogui.click(x, y - 210, duration=0.25)
    # 复制验证码
    x, y = find_pic('copy_sda_code.png')
    pyautogui.click(x, y, duration=0.25)
    # 显示steam登录窗口
    show_sign_steam_window()
    x, y = find_pic('sda_code_input.png')
    pyautogui.click(x, y, duration=0.25)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')


def find_pic(pic_name, times=5):
    """
    Find the specified image on the screen.
    """
    # 定义图像文件路径
    pic_path = os.path.join(os.path.dirname(__file__), 'pic', pic_name)
    # 匹配pic/login.png
    # Wait for the login button to appear
    for i in range(times):
        # Check if the login button is visible
        try:
            # Locate the login button on the screen
            pic = pyautogui.locateCenterOnScreen(pic_path, confidence=0.8)
            if pic:
                print(f"{pic_name} found")
                return pic
            else:
                print(f"{pic_name} not found")
                time.sleep(1)
        except pyautogui.ImageNotFoundException:
            time.sleep(1)
    return None


def start_games():
    games = ['Egg', 'Cats', 'Banana']

    for game in games:
        # 进入游戏库
        show_steam_window()
        x, y = find_pic('steam_lib.png', 1000)
        # 点击游戏库
        pyautogui.click(x, y, duration=0.25)
        # 搜索游戏
        x, y = find_pic('search_games.png')
        pyautogui.click(x, y, duration=0.25)
        # 清除当前对话框
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('delete')
        # 输入游戏名
        pyperclip.copy(game)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.click(x, y + 55, duration=0.25)
        # 开始游戏
        x, y = find_pic('start_game.png')
        pyautogui.click(x, y, duration=0.25)
        # 第一次登录需要确认
        if game == 'Banana':
            if find_pic('accept.png'):
                x, y = find_pic('accept.png')
                pyautogui.click(x, y, duration=0.25)
            if find_pic('play_anyway.png', 10):
                x, y = find_pic('play_anyway.png')
                pyautogui.click(x, y, duration=0.25)
        # 等待游戏启动
        while not is_application_running(f'{game}.exe'):
            time.sleep(1)
        show_games_window(game)
        # 判断游戏窗口是否存在
        while not gw.getWindowsWithTitle(game):
            time.sleep(1)
        # 最大化游戏窗口
        win = gw.getWindowsWithTitle(game)[0]
        win.maximize()
        if game == 'Egg':
            if find_pic('egg.png'):
                x, y = find_pic('egg.png')
                pyautogui.moveTo(x, y, duration=0.25)
            else:
                # 找到鸡蛋设置
                x, y = find_pic('egg_setting.png', 1000)
                pyautogui.click(x, y, duration=0.25)
                time.sleep(1)
                # 选择装备
                x, y = find_pic('egg_equip.png', 1000)
                pyautogui.click(x, y, duration=0.25)
                time.sleep(1)
                # 关闭鸡蛋设置
                x, y = find_pic('egg_setting_close.png', 1000)
                pyautogui.click(x, y, duration=0.25)
                time.sleep(1)
        # 获取屏幕大小 移动到屏幕中心
        width, height = pyautogui.size()
        pyautogui.moveTo(width / 2, height / 2, duration=0.25)
        # 等待一下
        time.sleep(1)
        # 左键连点100次
        pyautogui.click(clicks=100, interval=0.1)
        # 关闭游戏
        kill_games(game)


# 读取配置文件
# Read the configuration file
# 修改为每3小时运行一次
# Run every 3 hours

def login_steam():
    # 打开steam
    while True:
        open_steam()
        # 如果不为空，说明已经打开
        if find_pic('login.png'):
            break
    print("Steam opened successfully")

    # 匹配pic/login.png
    # Wait for the login button to appear
    find_pic('login.png')

    # 输入账号密码
    # Simulate typing the username
    print("Typing username and password...")
    # 使用剪贴板复制账号并粘贴
    pyperclip.copy(username)
    pyautogui.hotkey('ctrl', 'v')
    print(f"Pasted username: {username}")
    # 模拟 Tab 键切换到密码输入框
    pyautogui.press('tab')
    time.sleep(0.9)  # 等待一会儿，以确保焦点切换

    # 使用剪贴板复制密码并粘贴
    pyperclip.copy(password)
    pyautogui.hotkey('ctrl', 'v')
    print(f"Pasted password: {password}")

    # 可选：按回车键以提交表单
    pyautogui.press('enter')

    show_sign_steam_window()
    if not find_pic('sda.png', 15):
        kill_steam()
        print(f'{username} login failed')

        return False

    type_sda_code()
    return True


while True:
    accounts = []
    config_file = 'config.txt'
    if os.path.exists(config_file):
        """
        username----password
        username----password
        username----password
        """
        with open(config_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                username, password = line.strip().split('----')
                print(f"Account: {username}, Password: {password}")
                accounts.append((username, password))
    while accounts:
        for username, password in accounts:
            # Delete files in the directory
            directory_path = r"C:\Program Files (x86)\Steam\config"
            print(f"Deleting files in the directory: {directory_path}")
            delete_files_in_directory(directory_path)
            print("Deletion complete")
            if not login_steam():
                continue
            print("Login successful")

            while not steam_exists():
                time.sleep(1)
            start_games()
            accounts.remove((username, password))
        if not accounts:
            print("All accounts have been processed. Waiting for 3 hours...")
            time.sleep(10800)
