import pygame
pygame.init()
info = pygame.display.Info()
import pygame
import pandas as pd
from teams import a,b

TEAM1 = a
TEAM2 = b

SLOW_ATTACK = 3
MEDIUM_ATTACK = 2
FAST_ATTACK = 1

SLOW_SPEED = 1
MEDIUM_SPEED = 3
FAST_SPEED = 5
TOP_SPEED = 6

FPS = 10

FULL_WIDTH = info.current_w
EXTRA_HEIGHT  = info.current_h
FULL_HEIGHT = int(FULL_WIDTH*9/16)


ARENA_HEIGHT = int(422/540*FULL_HEIGHT)
ARENA_WIDTH = ARENA_HEIGHT//2

AIR_HEIGHT = ARENA_HEIGHT * 0.03


MIDDLE_WIDTH = FULL_WIDTH*54//196
MIDDLE_HEIGHT = FULL_HEIGHT

CARD_PLATE_WIDTH = FULL_WIDTH*12//196
CARD_PLATE_HEIGHT = FULL_HEIGHT*832//1080

GAME_START_TIME = 3*FPS # 3 sec
GAME_TOTAL_TIME = 1800 # 3 min
GAME_END_TIME = GAME_START_TIME + GAME_TOTAL_TIME

FRAMES = 6
SIGNAL_LENGTH = 200

CENTERS = pd.read_csv("data/image_centers/troops_center.csv",index_col="troop")
