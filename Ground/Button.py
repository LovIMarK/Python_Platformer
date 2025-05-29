from Utils.settings import *
from Core.Objects import Object

class Button(Object):
    BUTTONS = []

    def __init__(self, x, y, width, height, name=None):
        super().__init__(x, y, width, height, "button")
        self.button = load_sprite_sheet_cached("Menu", "Buttons", width, height)
        self.image = self.button[name][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.onButton = False

    def OnButton(self, pos):
        self.onButton = self.rect.collidepoint(pos)

    def Clicked(self, pos=None):
        if pos is not None:
            return self.rect.collidepoint(pos)
        return self.onButton

    def buttonLevel(self, levels):
        self.BUTTONS.clear()
        posX = 0
        posY = 0
        for i in range(1, 51):
            string_number = "{:02d}".format(i)
            if i > levels:
                string_number += "1"
            buttonLevel = LevelButton(WIDTH/3+posX, 0+posY, 19, 17, string_number)
            self.BUTTONS.append(buttonLevel)
            posX += buttonLevel.image.get_width()
            if i % 10 == 0:
                posY += buttonLevel.image.get_height()
                posX = 0

    def ChangeButton(self, playerLevel):
        changedButton = self.BUTTONS[playerLevel-1]
        string_number = "{:02d}".format(playerLevel)
        newButton = LevelButton(changedButton.rect.x, changedButton.rect.y, changedButton.width, changedButton.height, string_number)
        newButton.name = string_number
        self.BUTTONS[playerLevel-1] = newButton

    def DrawMenu(self, win):
        for obj in self.BUTTONS:
            win.blit(obj.image, (obj.rect.x, obj.rect.y))
        pygame.display.update()

class LevelButton(Object):
    def __init__(self, x, y, width, height, name):
        super().__init__(x, y, width, height, name)
        self.level = load_sprite_sheets("Menu", "Levels", width, height)
        self.image = self.level[name][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.onButton = False

    def OnButton(self, pos):
        self.onButton = self.rect.collidepoint(pos)

    def Clicked(self, pos=None):
        if pos is not None:
            return self.rect.collidepoint(pos)
        return self.onButton
