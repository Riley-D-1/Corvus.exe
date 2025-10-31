# ⚠️ IMPORTANT
#This software is a mock malware simulation designed for educational purposes only.
#It does not contain real malware and does not harm systems.
#Use responsibly and only with informed consent.
import random 
import os 
import time
import pygame
import subprocess

pygame.mixer.pre_init(44100,-16,2,2048)
pygame.init()
try:
	#programIcon = pygame.image.load('assets/images/Icon.png') # Load the Icon
	#pygame.display.set_icon(programIcon) # Set Icon
	pygame.mixer.music.load('assets/music/Crow_caw_1.mp3')
	pygame.mixer.music.set_volume(0.5)
	music = True
except FileNotFoundError:
	print("File not found")
	music = False

screen = pygame.display.set_mode((250, 250), pygame.NOFRAME)
pygame.display.set_caption("Corvus.exe")
running = True
clock = pygame.time.Clock()
pygame.mixer.music.play()

# STUBS BABY
# Stage 1
def note_messsage():
    rand_num = random.randint(1,6)
    with open("example.txt", "w") as file:
        if rand_num ==1:
            file.write("This is the first line.")
        elif rand_num == 2:
            file.write("This is the second line.")
        elif rand_num == 3:
            file.write("This is the first line.")
        elif rand_num == 4:
            file.write("This is the first line.")
        elif rand_num == 5:
            file.write("This is the first line.")
        else:
            file.write("This is the first line.")

    file_path = "example.txt"
    subprocess.Popen(['notepad.exe', file_path])
def stage_up():
    print("Stub")
def feather():
    if os.path.exists(image_path):
        os.startfile(image_path)

def audio():
    pygame.mixer.music.play()

# Stage 2
def cursor_steal():
    pygame.event.pump()
    time.sleep(1)
    time.sleep(1)
    
# Stage 3

def terminal_messsage():
    # AI Helped as my powershell knowledge is poor
    subprocess.Popen(
        'start cmd /c "'
        'echo [Corvus.exe] Injecting payload... && '
        'timeout /t 2 >nul && '
        'echo [Corvus.exe] Disabling firewall... && '
        'timeout /t 2 >nul && '
        'echo [Corvus.exe] System integrity compromised... && '
        'timeout /t 1 >nul && '
        'echo. && '
        'echo \x1b[91m[Corvus.exe] HAHAHAH MINE \x1b[0m && '
        'timeout /t 3 >nul && '
        'exit"',
        shell=True
    )

def glitch_screen():
    print()
    # Glitch screen with pygame overlays

def meltdown():
    print()

def educational_warning():
    content= ["...   Lucky this was an educational mock malware.", 
    " Corvus.exe is an educational example of how much control an exe can have."
    "It is a nightmare. This was created for the theme spooky on hackclub siege and its spooky alright...",
    "I'm a pretty average coder but it takes 3 lines to delete system 32 ruining your windows altogether",
    "Linux is even easier requiring just 1 line to nuke its crucial files.",
    "You want even more spooky?",
    "Every day, 560,000 new pieces of malware are detected, adding to the over 1 billion malware programs already in circulation.",
    "Not scared yet?"
    "With this program I could have started stealing your files all while your keyboard and mouse are disabled",
    "Imagine what an experienced hacker could do!",
    "Please take this as an important reminder about the importance of cybersecurity.",
    "                                                                                 ",
    "Credits:",
    "Creator : Riley-D-1 ",
    "See the repoistry on my github with the name Corvus.exe "
    ]
    for item in content:
        for char in item:
            print()
            #print(char)

def stage_3():
    terminal_messsage()
    glitch_screen()
    meltdown()

cursor_steal() 
#educational_warning()
#note_messsage()
#terminal_messsage()
while running == True:
    pygame.display.update()
    pygame.mouse.set_pos((400, 300))
    clock.tick(600)

