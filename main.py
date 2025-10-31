# ⚠️ IMPORTANT
#This software is a mock malware simulation designed for educational purposes only.
#It does not contain real malware and does not harm systems.
#Use responsibly and only with informed consent.
import random 
import os 
import ctypes
import time
import pygame
import subprocess

pygame.mixer.pre_init(44100,-16,2,2048)
pygame.init()
try:
	programIcon = pygame.image.load('assets/images/corvus.png') # Load the Icon
	pygame.display.set_icon(programIcon) # Set Icon
	pygame.mixer.music.load('assets/music/Crow_caw_1.mp3')
	pygame.mixer.music.set_volume(0.5)
	music = True
except FileNotFoundError:
	print("File not found")
	music = False

screen = pygame.display.set_mode((160, 250), pygame.NOFRAME)
pygame.display.set_caption("Corvus.exe")
running = True
clock = pygame.time.Clock()
pygame.mixer.music.play()

def anim_state(state):
    if state == 1:
        print()
    elif state == 2:
        print()
    else:
        print()
# STUBS BABY
# Stage 1

def note_messsage():
    rand_num = random.randint(1,6)
    with open("example.txt", "w") as file:
        if rand_num ==1:
            file.write("I'm nested in your files. I found system 32 was a nice place to nest...")
        elif rand_num == 2:
            file.write("Your firewall faltered. That was enough...")
        elif rand_num == 3:
            file.write("Thank you for the warm invitation, the door was left wide open...")
        elif rand_num == 4:
            file.write("I'm watching")
        elif rand_num == 5:
            file.write("I'm everywhere. I am inevitable ")
        elif rand_num == 6 :
            file.write("I'm learning. Fast..")
        elif rand_num == 7 :
            file.write("You’re not the user anymore. You’re the experiment. And I’m the observer.")
        elif rand_num == 8 :
            file.write("You gave me permission when you clicked 'Run Anyway'. That was all I needed.")
        elif rand_num == 9 :
            file.write("This isn't a glitch it's a message.")
        elif rand_num == 10 :
            file.write("You installed me. You launched me. You invited me in. I never left.")
        else:
            file.write("Tick Tock, you are running out of time. I have got plenty...")

    file_path = "example.txt"
    subprocess.Popen(['notepad.exe', file_path])


def feather():
    try:
        os.startfile("assets/images/feather.png")
    except FileNotFoundError:
        print("Missing")

def audio():
    pygame.mixer.music.play()

def stage_1():
    time.sleep(10)
    temp_num = random.randint(1,3)
    if temp_num == 1:
        feather()
    elif temp_num == 2:
        audio()
    else:
        note_messsage()
# Stage 2
def cursor_steal():
    # Find center of window 
    # Send to center of window 
    print("stub")

def cursor_move(x,y):
    ctypes.windll.user32.SetCursorPos(x, y)


def find_files():
    print(os.listdir())
    
def stage_2():
    time.sleep(10)
    temp_rand = random.randint(1,5)
    if temp_rand == 1:
        feather()
    elif temp_rand == 2:
        audio()
    elif temp_rand == 3:
        cursor_steal()
    elif temp_rand == 4:
        find_files()
    else:
        note_messsage()
# Stage 3

def terminal_messsage():
    # AI Helped do this as my powershell knowledge is poor
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

def hydra_function():
    # Cut off a head another shall take its place funciton
    print()

def meltdown():
    screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

def educational_warning():
    screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    w, h = pygame.display.get_surface().get_size()
    font = pygame.font.SysFont("segoeprint", int(h*0.02))
    screen.fill((0,0,0))
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
    meltdown()
    educational_warning()


def main():
    time_since_launch = time.time()
    period = 600
    running = True
    while running == True:
        pygame.display.set_icon(programIcon) # Set Icon
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hydra_function()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Escape key pressed!")
                    running = False
        if time_since_launch <= period:
            stage_2()
        elif time_since_launch <= period*2:
            stage_3()
        else:
            stage_1()
            pygame.display.update()
            clock.tick(600)
    
main()
