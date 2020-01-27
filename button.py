import pygame.font


class Button:
    def __init__(self, ai_settings, screen, msg):
        """Initialize button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Setting up button size and properties.
        self.width, self.height = 200, 50
        self.button_color = 0, 255, 0
        self.text_color = 255, 255, 255
        self.font = pygame.font.SysFont(None, 48)

        # Building rect-object for button and centering it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Message of the button is created only once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Makes 'msg' as a rectangular and centers the text in it"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Displaying an empty button and outputing the message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
