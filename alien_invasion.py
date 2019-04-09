#!/usr/bin/env python
# Author:Wang Xueming
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象、设置等
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        # 监听事件
        gf.check_events(ai_settings, screen, ship, bullets)
        # 移动飞船
        ship.update()
        # 更新子弹位置
        bullets.update() # 调用update() ，编组将自动调用组中的每一个update()，即每颗子弹调用bullet.update()
        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
