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
import win32gui
import win32con
import getpass

# Music Innit about sound quality and whatnot
pygame.mixer.pre_init(44100,-16,2,2048)
# Starting other core parts of pygame
pygame.init()
pygame.font.init() 
# Try and except the load of assets 
try:
	program_icon = pygame.image.load('assets/images/icon.png') # Load the Icon
	pygame.display.set_icon(program_icon) # Set Icon
	pygame.mixer.music.load('assets/music/Crow_caw_1.mp3')
	pygame.mixer.music.set_volume(0.5)
	music = True

except FileNotFoundError:
	print("File not found")
	music = False

screen = pygame.display.set_mode((160, 160), pygame.NOFRAME)
# Credit to https://github.com/munucrafts/PY-DesktopPet-Ducky for the info 
#Make window layered
hwnd = pygame.display.get_wm_info()["window"]
ctypes.windll.user32.SetWindowLongW(hwnd, -20, ctypes.windll.user32.GetWindowLongW(hwnd, -20) | 0x80000)

# Make the entire window transparent
transparency_color = (0, 0, 0)
color_key = (transparency_color[2] << 16) | (transparency_color[1] << 8) | transparency_color[0]
ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, color_key, 0, 0x00000001)

pygame.display.set_caption("Corvus.exe")
running = True
clock = pygame.time.Clock()
pygame.mixer.music.play()

# Class for core methods of window
class corvus:
    def __init__(self):
        self.x_pos = 1
        self.y_pos = 1
        self.state = "idle"
    def move(self,x,y):
        self.x_pos += x
        self.y_pos += y
    def anim_state(self,state):
        if state == "idle":
            background = pygame.image.load("assets/images/corvus.png").convert()
            screen.blit(background, (0, 0))
            pygame.display.flip()
        elif state == "grab":
            background = pygame.image.load("assets/images/corvus.png").convert()
            screen.blit(background, (0, 0))
            pygame.display.flip()
        elif state == "walk_1":
            background = pygame.image.load("assets/images/corvus.png").convert()
            screen.blit(background, (0, 0))
            pygame.display.flip()
        elif state == "walk_2":
            background = pygame.image.load("assets/images/corvus.png").convert()
            screen.blit(background, (0, 0))
            pygame.display.flip()
        else:
            print("error")
        self.state = state
    def drag(self):
        print(self.state)
    def cursor_steal(self):
        ctypes.windll.user32.SetCursorPos(self.x_pos, self.y_pos)

# STUBS BABY
# Stage 1

def note_messsage():
    # Used as a random num selector
    rand_num = random.randint(1,11)
    with open("assets/message.txt", "w") as file:
        if rand_num ==1:
            file.write("I'm nested in your files. I found system 32 was a nice place to nest...")
        elif rand_num == 2:
            file.write("Your firewall faltered. That was enough...")
        elif rand_num == 3:
            file.write(f"Thank you for {getpass.getuser()} the warm invitation, the door was left wide open...")
        elif rand_num == 4:
            file.write(f"Hey {getpass.getuser()}, I'm watching")
        elif rand_num == 5:
            file.write("I'm everywhere. I am inevitable ")
        elif rand_num == 6 :
            file.write("I'm learning. Fast..")
        elif rand_num == 7 :
            file.write("You're not the user anymore. You're the experiment. And I'm the observer.")
        elif rand_num == 8 :
            file.write("You gave me permission when you clicked 'Run Anyway'. That was all I needed.")
        elif rand_num == 9 :
            file.write("This isn't a glitch it's a message. The message is run")
        elif rand_num == 10 :
            file.write("You installed me. You launched me. You invited me in. I never left.")
        else:
            file.write("Tick Tock, you are running out of time. I have got plenty...")

    file_path = "assets/message.txt"
    # Opens the file from where it is written.
    # Maybe too big?
    subprocess.Popen(['notepad.exe', file_path])

def audio():
    pygame.mixer.music.play()

def find_files():
    # Need to fill out
    files = os.listdir(os.path.expanduser("~/Downloads"))
    rand_file = random.choice(files)
    print(f"Anything intreasting in {rand_file}?")

def meme():
    meme_list = os.listdir("assets/images/memes")
    meme = random.choice(meme_list)
    os.startfile(meme)
    print(meme)

def chaos(the_one):
    time.sleep(10)
    temp_rand = random.randint(1,5)
    if temp_rand == 1:
        # Removed due to problems
        #feather()
        meme()
    elif temp_rand == 2:
        audio()
    elif temp_rand == 3:
        the_one.cursor_steal()
    elif temp_rand == 4:
        find_files()
    else:
        note_messsage()

# Stage 3
# All preset sequence to scare those involved.
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


def meltdown():
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    w, h = pygame.display.get_surface().get_size()
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont("consolas", 48)
    text = font.render("SYSTEM FAILURE: CAUSED BY CORVUS.EXE", True, (255, 0, 0))
    screen.blit(text,(100,100))
    pygame.display.flip()
    time.sleep(3)

def educational_warning():
    screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
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
            font.render(char)

            #print(char)

def final_countdown(the_one):
    terminal_messsage()
    meltdown()
    educational_warning()


def main():
    # Caculate time since launch to trigger diffrent stages. 
    time_since_launch = time.time()
    period = 600
    # Time period before starting next stage. Stage 2 takes 1*period and the 3rd stage is double
    the_one = corvus()
    running = True
    while running == True:
        #Keep Window on Top
        #win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, w//2, h*2, 0, 0, win32con.SWP_NOSIZE)
        pygame.display.set_icon(program_icon) # Set Icon
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("NOPE")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Make 
                    pygame.quit()
                    print("Escape key pressed!")
                    running = False
        if time_since_launch <= period:
            final_countdown(the_one)
            running = False
        else:
            chaos(the_one)
meltdown()
# Self note (Command for exe)
#pyinstaller main.py --onefile --noconsole --add-data "assets/*:assets"
