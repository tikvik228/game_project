import pygame
from load_image import load_image


width, height = 800, 600
screen = pygame.display.set_mode((width, height))
menu_background = load_image("temporary_menu_background.png")


class levelOneButton(pygame.sprite.Sprite):

    def __init__(self, *group):
        super().__init__(*group)
        self.image_default = load_image("level1_button.png")
        self.image_pointed = load_image("level1_button_pointed.png")
        self.image = self.image_default
        self.rect = self.image.get_rect()
        self.rect.x = 418
        self.rect.y = 368

    def update(self, *args):
        if args and self.rect.collidepoint(args[0]):
            self.image = self.image_pointed
        else:
            self.image = self.image_default


class levelTwoButton(pygame.sprite.Sprite):

    def __init__(self, *group):
        super().__init__(*group)
        self.image_default = load_image("level2_button.png")
        self.image_pointed = load_image("level2_button_pointed.png")
        self.image = self.image_default
        self.rect = self.image.get_rect()
        self.rect.x = 568
        self.rect.y = 368

    def update(self, *args):
        if args and self.rect.collidepoint(args[0]):
            self.image = self.image_pointed
        else:
            self.image = self.image_default



def main():
    pygame.init()
    pygame.display.set_caption("названия нет")
    screen.fill("black")
    menu_sprites = pygame.sprite.Group()
    one = levelOneButton(menu_sprites)
    two = levelTwoButton(menu_sprites)
    level1_passed = False

    running = True
    fps = 60
    clock = pygame.time.Clock()
    while running:
        screen.blit(menu_background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and one.rect.collidepoint(event.pos):
                if not level1():
                    running = False
                level1_passed = True
            if event.type == pygame.MOUSEBUTTONDOWN and two.rect.collidepoint(event.pos) and level1_passed:
                if not level2():
                    running = False
        menu_sprites.draw(screen)
        menu_sprites.update(pygame.mouse.get_pos())
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


def level1():
    level1_sprites = pygame.sprite.Group() # пока пустая группа

    running = True
    fps = 60
    clock = pygame.time.Clock()
    while running:
        screen.fill("black")
        end_level1 = pygame.draw.rect(screen, "red", (300, 200, 200, 100))  # заглушка
        font = pygame.font.Font(None, 23)
        text_surface = font.render("Выйти из первого уровня", True, "white")
        screen.blit(text_surface, (305, 240))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN and end_level1.collidepoint(event.pos):
                running = False
        level1_sprites.draw(screen)
        level1_sprites.update()
        clock.tick(fps)
        pygame.display.flip()
    return True

def level2():
    level2_sprites = pygame.sprite.Group()  # пока пустая группа

    running = True
    fps = 60
    clock = pygame.time.Clock()
    while running:
        screen.fill("black")
        end_level1 = pygame.draw.rect(screen, "red", (300, 200, 200, 100)) #
        font = pygame.font.Font(None, 23)
        text_surface = font.render("Выйти из второго уровня", True, "white")
        screen.blit(text_surface, (305, 240))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN and end_level1.collidepoint(event.pos):
                running = False
        level2_sprites.draw(screen)
        level2_sprites.update()
        clock.tick(fps)
        pygame.display.flip()
    return True


if __name__ == '__main__':
    main()