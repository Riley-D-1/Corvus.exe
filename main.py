# ⚠️ IMPORTANT
#This software is a mock malware simulation designed for educational purposes only.
#It does not contain real malware and does not harm systems.
#Use responsibly and only with informed consent.
import random 
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
note_messsage()
while running == True:
    pygame.display.update()
    clock.tick(600)

