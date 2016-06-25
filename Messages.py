from pygame import *

class Message():
    
    def __init__(self, text, screen):
        self.text = text
        self.screen = screen
        self.font = font.Font(None, 30)
        
    def displayMessage(self):
        
        wait = True
        while wait:
            for evnt in  event.get():
                if evnt.type == MOUSEBUTTONDOWN:
                    wait = False
                    
            draw.rect(self.screen, (200,0,0), (490, 190, 520, 320))
            draw.rect(self.screen, (0,0,0), (500, 200, 500, 300))
            mess = self.font.render(self.text, True, (200,0,0), (0,0,0))
            messRect = mess.get_rect()
            messRect.centerx = 750 
            messRect.centery = 350
            self.screen.blit(mess, messRect)
            display.flip()
            
class NonValidTarget(Message):
    
    def __init__(self, screen):
        Message.__init__(self, "You must Attack a Valid Target", screen)
        
class WrongTurn(Message):
    
    def __init__(self, screen):
        Message.__init__(self, "You can't atack your own minion", screen)