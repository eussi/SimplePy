#!/usr/bin/env python
# Author:Wang Xueming
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象、设置等
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_setting, screen)

    # 开始游戏的主循环
    while True:
        # 监听事件
        gf.check_events(ship)
        # 移动飞船
        ship.update()
        # 更新屏幕
        gf.update_screen(ai_setting, screen, ship)


run_game()
