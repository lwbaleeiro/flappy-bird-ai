import pygame
import os

class Bird:
    IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]
    MAX_ROTATION = 25
    ROTATION_VELOCITY = 20
    ANIMATION_TIME = 5
    MAX_DISPLACEMENT = 16
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.velocity = 0
        self.height = self.y
        self.img_count = 0
        self.image = self.IMGS[0]

    def jump(self):
        self.velocity = -10.5
        self.tick_count = 0
        self.height = self.y

    def check_ground_collision(self, base):
        if self.y + self.image.get_height() >= base.y:
            return True
        return False

    def move(self):
        self.tick_count += 1

        displacement = self.velocity * self.tick_count + 1.5 * self.tick_count ** 2
        if displacement >= self.MAX_DISPLACEMENT:
            displacement = self.MAX_DISPLACEMENT
        if displacement < 0:
            displacement -= 2

        self.y += displacement

        if displacement < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROTATION_VELOCITY

    def draw(self, window):
        self.img_count += 1

        if self.img_count < self.ANIMATION_TIME:
            self.image = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME * 2:
            self.image = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME * 3:
            self.image = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME * 4:
            self.image = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME * 4 + 1:
            self.image = self.IMGS[0]
            self.img_count = 0
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME * 2

        rotated_image = pygame.transform.rotate(self.image, self.tilt)
        obj_rect = rotated_image.get_rect(center=self.image.get_rect(topleft = (self.x, self.y)).center)
        window.blit(rotated_image, obj_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.image)