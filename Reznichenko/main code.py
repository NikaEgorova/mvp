from pygame import *

window_width = 700
window_height = 500
display.set_caption('labirint lol')
background = transform.scale(image.load("bg.jpg"), (window_width, window_height))
window = display.set_mode((window_width, window_height))

mixer.init()
mixer.music.load('maingame.mp3')
mixer.music.play(-1)


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed

    def update(self):
        if player.rect.x <= window_width - 80 and player.x_speed > 0 or player.rect.x >= 0 and player.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, walls, False)
        if self.x_speed > 0:
            for platforms in platforms_touched:
                self.rect.right = min(self.rect.right, platforms.rect.left)
        elif self.x_speed < 0:
            for platforms in platforms_touched:
                self.rect.left = max(self.rect.left, platforms.rect.right)

        if player.rect.y <= window_height - 80 and player.y_speed > 0 or player.rect.y >= 0 and player.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, walls, False)
        if self.y_speed > 0:
            for platforms in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, platforms.rect.top)
        elif self.y_speed < 0:
            for platforms in platforms_touched:
                self.rect.top = max(self.rect.top, platforms.rect.bottom)
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.right - 25, self.rect.centery - 16, 15, 20, 15)
        bullets.add(bullet)

class Enemy(GameSprite):
    side = 'left'
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self,player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    def update(self):
        if self.rect.x <= 450:
            self.side = 'right'
        if self.rect.x >= window_width - 80:
            self.side = 'left'

        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > window_width + 10:
            self.kill()

class Enemy1(GameSprite):
    side = 'left'

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

    def update(self):
        if self.rect.x <= 0:
            self.side = 'right'
        if self.rect.x >= window_width - 380:
            self.side = 'left'

        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy2(GameSprite):
    side = 'left'

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

    def update(self):
        if self.rect.x <= 100:
            self.side = 'right'
        if self.rect.x >= window_width - 380:
            self.side = 'left'

        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


button1= GameSprite('key.png', 340, 300, 40, 40)

wall1 = GameSprite('wall.png', 400, 100, 50, 400)
wall2 = GameSprite('wall2.png', 200, 250, 200, 40)
wall3 = GameSprite('wall2.png', 550, 300, 150, 40)
wall4 = GameSprite('wall.png', 200, 250, 40, 150)
wall5 = GameSprite('wall2.png', 550, 100, 150, 40)
wall6 = GameSprite('wall.png', 200, 0, 40, 100)
walltofinish = GameSprite('door.png', 450, 280, 100, 70)#

walls = sprite.Group()
bullets = sprite.Group()
walls.add(wall1)
walls.add(wall2)
walls.add(wall3)
walls.add((wall4))
walls.add(wall5)
walls.add(wall6)

player = Player('hero.png', 5, window_height -80, 80, 80, 0, 0)
monster = Enemy('enemy.png', 450, 200, 80, 80, 3)
monstr = Enemy1('enemy.png', 50, 170, 80, 80, 3)
monstryk = Enemy2('enemy.png', 250, 410, 80, 80,3)
finish = GameSprite('end.png', 550, window_height -80, 80, 80)

monsters = sprite.Group()
monsters.add(monster)
monsters.add(monstr)
monsters.add(monstryk)

victoryline=sprite.Group()
victoryline.add(button1)
victoryline.add(walltofinish)
win = False
run = True
while run:
    time.delay(17)

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_w:
                player.y_speed = -5
            elif e.key == K_s:
                player.y_speed = 5
            elif e.key == K_a:
                player.x_speed = -5
            elif e.key == K_d:
                player.x_speed = 5
            elif e.key == K_SPACE:
                player.fire()
        elif e.type == KEYUP:
            if e.key == K_w:
                player.y_speed = 0
            elif e.key == K_s:
                player.y_speed = 0
            elif e.key == K_a:
                player.x_speed = 0
            elif e.key == K_d:
                player.x_speed = 0
    if not win:
        window.blit(background, (0,0))
        bullets.draw(window)
        monsters.draw(window)
        bullets.update()
        victoryline.draw(window)
        player.reset()
        player.update()
        finish.reset()
        walls.draw(window)

        sprite.groupcollide(monsters, bullets, True, True)
        monsters.update()
        monsters.draw(window)
        sprite.groupcollide(bullets, walls, True, False)
        sprite.spritecollide(player, victoryline, True)

        if sprite.spritecollide(player, monsters, False):
            mixer.music.stop()
            mixer.Sound('over.wav').play()
            win = True
            img = image.load('lose.png')
            window.blit(transform.scale(img, (window_width, window_height)), (0,0))

        if sprite.collide_rect(player, finish):
            mixer.music.stop()
            mixer.Sound('win.wav').play()
            win = True
            img = image.load('win.png')
            window.blit(transform.scale(img, (window_width, window_height)), (0,0))

        display.update()