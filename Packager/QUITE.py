import pygame
import sys


def Quite():
    for event in pygame.event.get():    
            if event.type == pygame.QUIT:    #关闭窗口退出
                sys.exit()