#!/usr/bin/env python
# Author:Wang Xueming
import pygame

from p1_settings import Settings
from p1_ship import Ship
import p1_game_functions as gf
from pygame.sprite import Group
from p1_game_stats import GameStats
from p1_button import Button
from p1_scoreboard import Scoreboard


def run_game():
    # 初始化游戏并创建一个屏幕对象、设置等
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建记分牌
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen, True)

    # 创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监听事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            # 移动飞船
            ship.update()
            # 更新子弹
            gf.update_bullets(ai_settings, screen, stats, sb, ship, bullets, aliens)
            # 移动外星人
            gf.update_aliens(ai_settings, screen, stats, sb, ship, bullets, aliens)

        # 更新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
