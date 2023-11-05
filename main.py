from funcion import *
from random import randint

window = pygame.display.set_mode((setting_win["WIDTH"], setting_win["HEIGHT"]))
pygame.display.set_caption("КОСМІЧНИЙ ШУТЕР")

def run():
    game = True
    start_time = 0
    end_time = 0
    menu = False
    boss_live = False

    hero = Hero(setting_win["WIDTH"] // 2 - setting_hero["WIDTH"] // 2,
                setting_win["HEIGHT"] - setting_hero["HEIGHT"] - 10,
                setting_hero["WIDTH"],
                setting_hero["HEIGHT"],
                image= hero_image_list)
    boss = Boss(setting_win["WIDTH"] // 2 - setting_boss["WIDTH"] // 2,
                - setting_boss["HEIGHT"],
                setting_boss["WIDTH"],
                setting_boss["HEIGHT"],
                image= boss_image_list)
    bg = Background()
    clock = pygame.time.Clock()     #створення об'єкту часу
    font_win_lose = pygame.font.Font(None, 50)
    rect_start = pygame.Rect(350, 225, 200, 60)
    rect_end = pygame.Rect(350, 325, 200, 60)

    while game:
        events = pygame.event.get()
        #window.fill((0,0,0))
        bg.update(window)

        try:
            window.blit(hp_list[6 - hero.HP], (5, 5))
        except:
            hero.HP = 0
        window.blit(font_win_lose.render(f"{hero.SCORE}", True, (255,255,255)), (setting_win["WIDTH"] - 50, 5))
 
        #HERO
        hero.move(window)
        for bullet in hero.BULLET_LIST:
            bullet.move_hero(window, hero, boss)
        
        if hero.HP <= 0:
            menu = True

        #BOT
        end_time = pygame.time.get_ticks()
        if end_time - start_time > 2000 and hero.SCORE < hero.LVL * 5:
            hero.BOT_LIST.append(Bot(randint(0, setting_win["WIDTH"] - setting_bot["WIDTH"]),
                                - setting_bot["HEIGHT"],
                                setting_bot["WIDTH"],
                                setting_bot["HEIGHT"],
                                image= bot_image_list,
                                hp= 1))
            start_time = end_time
        
        for bot in hero.BOT_LIST:
            bot.move(window, hero)

        for bullet in bullet_list_bot_boss:
            bullet.move_bot_boss(window, hero)

        #BOSS
        if hero.SCORE >= hero.LVL * 5:
            hero.BOT_LIST = list()
            boss.LIVE = True
            boss.move(window, hero)
      
        if menu == True:
            pygame.draw.rect(window, (120, 120, 120), rect_start)
            pygame.draw.rect(window, (120, 120, 120), rect_end)
            start_render = font_win_lose.render("START", True, (255,255,255))
            end_render = font_win_lose.render("END", True, (255,255,255))
            window.blit(start_render, (350 + 45, 225 + 13))
            window.blit(end_render, (350 + 65, 325 + 13))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if rect_start.collidepoint(x, y):
                        hero.HP = 5
                        hero.BOT_LIST = list()
                        while len(bullet_list_bot_boss) > 0:
                            bullet_list_bot_boss.pop(0)
                        hero.x = setting_win["WIDTH"] // 2 - setting_hero["WIDTH"] // 2
                        hero.SCORE = 0
                        menu = False
                    if rect_end.collidepoint(x, y):
                        game = False

        for event in events:
            if event.type == boss_event and boss.LIVE:
                bullet_list_bot_boss.append(Bullet(boss.centerx + 40, boss.bottom, 10, 20))
                bullet_list_bot_boss.append(Bullet(boss.centerx - 50, boss.bottom, 10, 20))
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    hero.MOVE["LEFT"] = True
                if event.key == pygame.K_d:
                    hero.MOVE["RIGHT"] = True
                if event.key == pygame.K_SPACE:
                    hero.BULLET_LIST.append(Bullet(hero.x + 50, hero.y, 10, 20))

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    hero.MOVE["LEFT"] = False
                if event.key == pygame.K_d:
                    hero.MOVE["RIGHT"] = False

        clock.tick(setting_win["FPS"])
        pygame.display.flip()

run()