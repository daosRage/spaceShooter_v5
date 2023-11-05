from data import *

boss_event = pygame.USEREVENT
pygame.time.set_timer(boss_event, 2000)

class Background():
    def __init__(self):
        self.y = 0
        self.y1 = - setting_win["HEIGHT"]
        self.image = background_image
        self.speed = 0.5
    
    def update(self, window):
        self.y += self.speed
        self.y1 += self.speed
        window.blit(self.image, (0, self.y))
        window.blit(self.image, (0, self.y1))
        if self.y > setting_win["HEIGHT"]:
            self.y = -setting_win["HEIGHT"]
        if self.y1 > setting_win["HEIGHT"]:
            self.y1 = -setting_win["HEIGHT"]


#загальний(батькивський) клас для героя та ботів
class Sprite(pygame.Rect):
    def __init__(self, x, y, width, height, image= None, speed= 5, hp= None):
        super().__init__(x, y, width, height)
        self.IMAGE_LIST = image
        self.IMAGE = self.IMAGE_LIST[0]
        self.IMAGE_COUNT = 0
        self.SPEED = speed
        self.HP = hp

    def move_image(self):
        self.IMAGE_COUNT += 1
        if self.IMAGE_COUNT == len(self.IMAGE_LIST) * 10 - 1:
            self.IMAGE_COUNT = 0
        if self.IMAGE_COUNT % 10 == 0:
            self.IMAGE = self.IMAGE_LIST[self.IMAGE_COUNT // 10]

    
class Hero(Sprite):
    def __init__(self, x, y, width, height, image= None, speed= 5, hp= 5):
        super().__init__(x, y, width, height, image, speed, hp)
        self.MOVE = {"LEFT": False, "RIGHT": False}
        self.BULLET_LIST = list()
        self.BOT_LIST = list()
        self.SCORE = 0
        self.LVL = 1
    
    def move(self, window):
        if self.MOVE["LEFT"] == True and self.x > 0:
            self.x -= self.SPEED
        if self.MOVE["RIGHT"] == True and self.x + self.width < setting_win["WIDTH"]:
            self.x += self.SPEED
        window.blit(self.IMAGE, (self.x, self.y))
        self.move_image()

class Bot(Sprite):
    def __init__(self, x, y, width, height, image= None, speed= 1, hp= 1, body_damage= 1):
        super().__init__(x, y, width, height, image, speed, hp)
        self.SHOT = 0
        self.BODY_DAMAGE = body_damage

    def move(self, window, hero):
        self.y += self.SPEED
        window.blit(self.IMAGE, (self.x, self.y))
        self.move_image()

        self.SHOT += 1
        if self.SHOT % (setting_win["FPS"] * 2) == 0:
            bullet_list_bot_boss.append(Bullet(self.centerx, self.bottom, 10, 20))

        if self.colliderect(hero):
            hero.HP -= self.BODY_DAMAGE
            hero.BOT_LIST.remove(self)
            return 0

class Boss(Sprite):
    bullet_pattern = [[()], 1]
    def __init__(self, x, y, width, height, image= None, speed= 1, hp= 10):
        super().__init__(x, y, width, height, image, speed, hp)
        self.ANIMATION = False
        self.LIVE = False

    def move(self, window, hero):
        if self.y < 50:
            self.y += abs(self.SPEED)
        self.x += self.SPEED
        if self.x <= 0 or self.right > setting_win["WIDTH"]:
            self.SPEED *= -1
        window.blit(self.IMAGE, self)
        self.move_image()
        if self.ANIMATION:
            self.leave(hero)
            self.LIVE = False
    def leave(self, hero):
        self.y -= abs(self.SPEED) * 2
        if self.bottom < 0:
            self.y = - self.height
            self.x = setting_win["WIDTH"] // 2 - self.width // 2
            self.ANIMATION = False
            self.HP = 10 + hero.LVL * 5
            hero.LVL += 1

class Bullet(pygame.Rect):
    def __init__(self, x, y, width, height, image= None, speed= 3):
        super().__init__(x, y, width, height)
        self.IMAGE = image
        self.SPEED = speed
    def move_hero(self, window, hero, boss):
        self.y -= self.SPEED
        index = self.collidelist(hero.BOT_LIST)
        if index != -1:
            hero.BOT_LIST[index].HP -= 1
            hero.BULLET_LIST.remove(self)
            if hero.BOT_LIST[index].HP == 0:
                hero.BOT_LIST.pop(index)
                hero.SCORE += 1
            return 0
        if self.y < 0:
            hero.BULLET_LIST.remove(self)
            return 0
        if hero.SCORE >= 5 * hero.LVL:
            if self.colliderect(boss):
                hero.BULLET_LIST.remove(self)
                boss.HP -= 1
                if boss.HP == 0:
                    boss.ANIMATION = True
                    
                    hero.SCORE += 1
                return 0
        pygame.draw.rect(window, (255, 20, 30), self)
        return 0
    
    def move_bot_boss(self, window, hero):
        self.y += self.SPEED
        if self.colliderect(hero):
            hero.HP -= 1
            bullet_list_bot_boss.remove(self)
            return 0
        if self.bottom > setting_win["HEIGHT"]:
            bullet_list_bot_boss.remove(self)
            return 0
        pygame.draw.rect(window, (20,20,200), self)
        