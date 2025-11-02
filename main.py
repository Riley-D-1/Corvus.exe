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
# Start the screen
# Try and except the load of assets 
screen = pygame.display.set_mode((160, 160), pygame.NOFRAME)
try:
    program_icon = pygame.image.load('assets/images/icon-1.png') # Load the Icon
    pygame.display.set_icon(program_icon) # Set Icon
    pygame.mixer.music.load('assets/music/Crow_caw_1.mp3')
    pygame.mixer.music.set_volume(0.5)
    music = True
except FileNotFoundError:
	print("File not found")
	music = False

pygame.display.set_caption("Corvus.exe")
running = True
clock = pygame.time.Clock()
# Class for core methods of window
class corvus:
    def __init__(self,x,y,speed):
        self.speed = speed
        self.position = pygame.Vector2(x,y)
        self.state = "idle"
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
    def drag(self,window):
        # Need to fix
        self.move()
        self.anim_state()
    def cursor_steal(self):
        # Fill this function with more infomation
        ctypes.windll.user32.SetCursorPos(self.position[0], self.position[1])
    def move(self,target_x,target_y):
        # Position using pygame vectors stored 2 values (x and y respectively)
        # By minusing or adding the speed to the value,
        # we can create smooth walking to a target destinations
        if target_x < self.position[0]:
            self.position[0] -= self.speed
        elif target_x > self.position[0]:
            self.position[0] += self.speed

        if target_y < self.position[1]:
            self.position[1] -= self.speed
        elif target_y > self.postion[1]:
            self.position[1] += self.speed 

# Control the desktop transperency effect
def transparency(on):
    hwnd = pygame.display.get_wm_info()["window"]
    if on == True:
        # Credit to https://github.com/munucrafts/PY-DesktopPet-Ducky for the info 
        #Make window layered
        ctypes.windll.user32.SetWindowLongW(hwnd, -20, ctypes.windll.user32.GetWindowLongW(hwnd, -20) | 0x80000)

        # Make the entire window transparent
        transparency_color = (0, 0, 0)
        color_key = (transparency_color[2] << 16) | (transparency_color[1] << 8) | transparency_color[0]
        ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, color_key, 0, 0x00000001)
    else:
        # AI HELPED wrote the below else statement as had no clue how to trigger the reverse
        # Remove layered style
        extended_style = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
        ctypes.windll.user32.SetWindowLongW(hwnd, -20, extended_style & ~0x80000)
        # Remove transparency
        ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, 255, 0x00000002)  # Set full opacity

def note_messsage():
    # Working and done!
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
            file.write("This isn't a glitch it's a message. The message is 'run while you still can'. ")
        elif rand_num == 10 :
            file.write("You installed me. You launched me. You invited me in. I never left.")
        else:
            file.write("Tick Tock, you are running out of time. I have got plenty...")

    file_path = "assets/message.txt"
    # Opens the file from where it is written.
    # Maybe too big?
    subprocess.Popen(['notepad.exe', file_path])

def audio(music):
    # Done, Simple but it works
    if music ==  True:
       pygame.mixer.music.play()

def pygame_screen_message(message,text_colour,screen_colour,sleep_time,clear):
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    w, h = pygame.display.get_surface().get_size()
    screen.fill(screen_colour)
    font = pygame.font.SysFont("consolas", 48)
    text = font.render(message, True, text_colour)
    text_rect = text.get_rect(center=(w//2, h//2))
    screen.blit(text,text_rect)
    pygame.display.flip()
    time.sleep(sleep_time)
    if clear == True:
        screen.fill((0,0,0))
        pygame.display.flip()
        time.sleep(sleep_time)


def find_files():
    # Done 
    files = os.listdir(os.path.expanduser("~/Downloads"))
    rand_file = random.choice(files)
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    w, h = pygame.display.get_surface().get_size()
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont("consolas", 48)
    text = font.render(f"Anything intreasting in {rand_file}?", True, (255, 0, 0))
    text_rect_idk = text.get_rect(center=(w//2, h//2))
    screen.blit(text,text_rect_idk)
    pygame.display.flip()
    time.sleep(2)
    
def meme():
    # Done I belive
    cwd = os.getcwd()
    # To ensure it works across diffrent directives
    meme_list = os.listdir(f"{cwd}/assets/images/memes/")
    meme = random.choice(meme_list)
    os.startfile(f"{cwd}/assets/images/memes/{meme}")

def chaos(the_one):
    time.sleep(10)
    temp_rand = random.randint(1,5)
    if temp_rand == 1:
        meme()
    elif temp_rand == 2:
        audio(music)
    elif temp_rand == 3:
        the_one.cursor_steal()
    elif temp_rand == 4:
        find_files()
    else:
        note_messsage()

# Stage 3
# All preset sequence to scare
def terminal_messsage():
    # AI Helped do this as my powershell knowledge is poor
    # Launch a separate terminal window with a custom title
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
        'timeout /t 3 >nul "',
        #'exit"',
        shell=True
    )


def educational_warning():
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    w, h = pygame.display.get_surface().get_size()
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont("segoeprint", 20)
    content= ["...   Lucky this was an educational mock malware.", 
    " Corvus.exe is an educational example of how much control an exe can have.",
    "It is a nightmare. This was created for the theme spooky on hackclub siege and its spooky alright...",
    "I'm a pretty average coder but it takes 3 lines to nuke window's critical files",
    "You want even more spooky?",
    "Every day, 560,000 new pieces of malware are detected, adding to the over 1 billion malware programs already in circulation.",
    "Not scared yet?",
    "With this program I could have started stealing your files all while your keyboard and mouse are disabled",
    "Imagine what an experienced hacker could do!",
    "Please take this as an important reminder about the importance of cybersecurity.",
    "Credits:",
    "Creator : Riley-D-1 ",
    "Art : Riley-D-1 ",
    "Crow calls :  https://www.youtube.com/watch?v=XZrh-zK1nJ0 - Free Sounds Library",
    "Code : Riley-D-1  ",
    "See the repoistry on my github with the name Corvus.exe ",
    "Thank you! And keep safe out there!"
    ]

    for item in content:
        pygame.event.get()
        text = font.render(item, True, (255,255,255))
        text_rect_2 = text.get_rect(center=(w//2, h//2))
        screen.blit(text,text_rect_2)
        pygame.display.flip()
        pygame.time.delay(3000)
        screen.fill((0,0,0))
        pygame.display.flip()

            
def meltdown():
    # Inspo - https://dev.to/chrisgreening/simulating-simple-crt-and-glitch-effects-in-pygame-1mf1
    w,h = pygame.display.get_surface().get_size()
    
    


def final_countdown():
    meltdown()
    # Everything below is working and timed to a T
    terminal_messsage()
    time.sleep(4) 
    pygame.event.get() 
    time.sleep(4)
    pygame.event.get()  
    time.sleep(4)
    pygame.event.get()
    print("ting")
    transparency(False)
    pygame_screen_message("SYSTEM FAILURE: CAUSED BY CORVUS.EXE",(255,0,0),(0,0,0),3,True)
    educational_warning()

def main():
    # Caculate time since launch to trigger diffrent stages. 
    time_since_launch = time.time()
    period = 600
    # Time period before starting next stage. Stage 2 takes 1*period and the 3rd stage is double
    the_one = corvus(1,1,1)
    running = True
    transparency(True)
    while running == True:
        #Keep Window on Top
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
        # swapped < to > for testing.
        #if time.time() - time_since_launch >= period:
            final_countdown()
            print("Done")
            time.sleep(1)
            running = False
        #else:
        #    chaos(the_one)
main()
# Self note (Command for exe)
# Worlds longest pyinstaller statement lol 
#pyinstaller main.py --onefile --noconsole --add-data "assets/*;assets" --icon=assets/images/icon.ico
# Have to use an older version to build for some reason? 3.11.8 