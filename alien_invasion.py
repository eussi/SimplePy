#!/usr/bin/env python
# Author:Wang Xueming
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
    # 初始化游戏并创建一个屏幕对象、设置等
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监听事件
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            # 移动飞船
            ship.update()
            # 更新子弹
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
            # 移动外星人
            gf.update_aliens(ai_settings, stats, screen, aliens, ship, bullets)

        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
