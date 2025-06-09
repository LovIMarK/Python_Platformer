from Utils.settings import *
from Core.objects import Object


class Button(Object):
    """
    Represents a UI button element, including handling hover and click logic, 
    as well as generating level selection buttons dynamically.
    """
    BUTTONS = []

    def __init__(self, x, y, width, height, name=None):
        """
        Initialize a button with given position, size, and sprite name.
        """
        super().__init__(x, y, width, height, "button")
        self.button = load_sprite_sheet_cached("Menu", "Buttons", width, height)
        self.image = self.button[name][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.onButton = False

    def OnButton(self, pos):
        """
        Update onButton state based on whether a given position is hovering over the button.
        """
        self.onButton = self.rect.collidepoint(pos)

    def Clicked(self, pos=None):
        """
        Check if the button has been clicked.
        Args:
            pos (tuple or None): Position of the click. If None, returns hover status.

        Returns:
            bool: True if clicked or hovered, False otherwise.
        """
        if pos is not None:
            return self.rect.collidepoint(pos)
        return self.onButton

    def buttonLevel(self, levels):
        """
        Generate level buttons for the menu up to a given unlocked level.
        Args:
            levels (int): The highest unlocked level.
        """
        self.BUTTONS.clear()
        posX = 0
        posY = 0
        for i in range(1, 51):
            string_number = "{:02d}".format(i)
            if i > levels:
                string_number += "1"  # Grayed-out or locked version
            buttonLevel = LevelButton(WIDTH / 3 + posX, 0 + posY, 19, 17, string_number)
            self.BUTTONS.append(buttonLevel)
            posX += buttonLevel.image.get_width()
            if i % 10 == 0:
                posY += buttonLevel.image.get_height()
                posX = 0

    def ChangeButton(self, playerLevel):
        """
        Update the visual state of a level button to mark it as newly unlocked.
        Args:
            playerLevel (int): The player's new unlocked level.
        """
        changedButton = self.BUTTONS[playerLevel - 1]
        string_number = "{:02d}".format(playerLevel)
        newButton = LevelButton(changedButton.rect.x, changedButton.rect.y, changedButton.width, changedButton.height, string_number)
        newButton.name = string_number
        self.BUTTONS[playerLevel - 1] = newButton

    def DrawMenu(self, win):
        """
        Draw all level buttons to the screen.
        Args:
            win (pygame.Surface): The surface to draw the buttons on.
        """
        for obj in self.BUTTONS:
            win.blit(obj.image, (obj.rect.x, obj.rect.y))
        pygame.display.update()


class LevelButton(Object):
    """
    A specialized button used for selecting a specific level in the menu.
    """

    def __init__(self, x, y, width, height, name):
        """
        Initialize the level button with its sprite and collision mask.
        """
        super().__init__(x, y, width, height, name)
        self.level = load_sprite_sheets("Menu", "Levels", width, height)
        self.image = self.level[name][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.onButton = False

    def OnButton(self, pos):
        """
        Check if a position is hovering over this button.
        """
        self.onButton = self.rect.collidepoint(pos)

    def Clicked(self, pos=None):
        """
        Check if this level button was clicked.
        Args:
            pos (tuple or None): Position of the click. If None, returns hover status.

        Returns:
            bool: True if clicked or hovered, False otherwise.
        """
        if pos is not None:
            return self.rect.collidepoint(pos)
        return self.onButton
