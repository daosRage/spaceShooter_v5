import pygame
import os

pygame.init()
#словник з розмірами вікна
setting_win = {
    "WIDTH": 900,
    "HEIGHT": 600,
    "FPS": 60
}
setting_hero = {
    "WIDTH": 130,
    "HEIGHT": 95
}
setting_bot = {
    "WIDTH": 80,
    "HEIGHT": 110
}
setting_boss = {
    "WIDTH": 400,
    "HEIGHT": 200
}


#bot_list = list()
bullet_list_bot_boss = list()

abs_path = os.path.abspath(__file__ + "/..") + "\\image"

hero_image_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "hero_fly_1.png")), (setting_hero["WIDTH"], setting_hero["HEIGHT"])),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "hero_fly_2.png")), (setting_hero["WIDTH"], setting_hero["HEIGHT"]))
]

bot_image_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "bot_1_1.png")), (setting_bot["WIDTH"],setting_bot["HEIGHT"])),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "bot_1_2.png")), (setting_bot["WIDTH"],setting_bot["HEIGHT"]))
]
boss_image_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "bot_1_1.png")), (setting_boss["WIDTH"],setting_boss["HEIGHT"])),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "bot_1_2.png")), (setting_boss["WIDTH"],setting_boss["HEIGHT"]))
]
background_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "bg.png")), (setting_win["WIDTH"],setting_win["HEIGHT"]))

hp_width, hp_height = 32, 32
hp_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "hp1.jpg")), (hp_width, hp_height)),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "hp2.jpg")), (hp_width, hp_height)),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "hp3.jpg")), (hp_width, hp_height)),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "hp4.jpg")), (hp_width, hp_height)),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "hp5.jpg")), (hp_width, hp_height)),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "hp6.jpg")), (hp_width, hp_height)),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "hp7.jpg")), (hp_width, hp_height)),
]