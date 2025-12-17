import os
import pyautogui

def open_chrome():
    os.system("start chrome")
    return "Tôi đã mở Chrome"

def shutdown():
    os.system("shutdown /s /t 5")
    return "Máy sẽ tắt sau 5 giây"

def open_vscode():
    os.system("code")
    return "Tôi đã mở Visual Studio Code"
