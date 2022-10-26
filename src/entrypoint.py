#!/usr/bin/env python3

"""
entrypoint.py - Main entry point for game
"""

import os
import pygame
from pygame.locals import *
from gamedirector import *

import resources
import game


# Start
def main(mainpath):
    # Initialise pygame
    pygame.init()
    pygame.mixer.init()
    pygame.mouse.set_visible(False)

    # start up director
    framerate = 30
    screen_res = (850, 480)
    window_title = "Waverider"
    direct = GameDirector(window_title, screen_res, framerate)

    # Load resources
    resources.init(mainpath, screen_res)

    # Load game scenes
    titlescreen = game.TitleScreen(direct, screen_res)
    direct.addscene('titlescreen', titlescreen)
    maingame = game.MainGame(direct, screen_res)
    direct.addscene('maingame', maingame)

    # start up director
    direct.change_scene('titlescreen', [])
    # dir.change_scene('maingame', [])
    direct.loop()

    # exiting, record framerate
    # print maingame.avgframerate
    # fp = open(os.path.join(mainpath,'framerate.txt'),"w")
    # fp.write("%f\n"%(maingame.avgframerate))
    # fp.close()
