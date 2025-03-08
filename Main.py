import pygame
import sys
import time
#from Packager import QUITE


def Main():
    pygame.init()                                   #初始化pygame
    size = width,height = 1500,1200                 #设置窗口大小
    color = (0,0,0)                                 #设置背景颜色 黑色
    image = pygame.image.load("./Image//1.jpg")     #加载图片
    imagerect = image.get_rect()                    #图片显示的矩形区域
    speed = [5,5]                                   #X轴和Y轴的移动距离
    screen = pygame.display.set_mode(size)          #显示窗口
    
    i = -1
    while True:                                     #窗口持久化
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:           #关闭窗口退出
                sys.exit()

        imagerect = imagerect.move(speed)           #控制图片移动速度
        #碰壁反弹
        if imagerect.left < 0 or imagerect.right > width:
            speed[0] = speed[1]*i
        if imagerect.top < 0 or imagerect.bottom > height:
            speed[1] = speed[1]*i
        #
        screen.fill(color)                          #填充颜色
        screen.blit(image,imagerect)                #图片加载到窗口上
        pygame.display.flip()                       #更新全部显示
        time.sleep(0.1)                             
    pygame.quit()

        #QUITE.Quite()                              #关闭窗口退出





if __name__ == "__main__":
    Main()