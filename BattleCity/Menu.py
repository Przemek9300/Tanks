import pygame
from Game import Game
from Construction import Construction

class Menu:

     hover_text = False

     def __init__(self, text, position):
          self.text = text
          self.position = position
          self.set_rect()

     def set_render(self):
          self.render = menu_fonts.render(self.text, True, self.hover_menu())
          #rysowanie tekstu na powierzchni (tekst, wygladzanie, tlo)

     def hover_menu(self):
          if self.hover_text:
               return (255, 255, 255)
          else:
               return (255, 255, 0)

     def draw(self):
          self.set_render()
          screen.blit(self.render, self.rect)

     def set_rect(self):
          self.set_render() #rysuje tekst
          self.rect = self.render.get_rect() #tworzy prostokat na
                                             #obszarze ktorego bedzie tekst
          self.rect.topleft = self.position  #ustawienie pozycji tekstu

if __name__ == "__main__":
     pygame.init()
     sound = pygame.mixer.Sound("music/SoundMenu.wav")
     sound2 = pygame.mixer.Sound("music/MusicMenu.wav")
     screen = pygame.display.set_mode((1100,700), pygame.FULLSCREEN) #480x320

     menu_fonts = pygame.font.Font(None, 60) #tworzenie nowej czcionki z pliku
                                        #(plik, rozmiar)
     #menu_words = [Menu("NEW GAME", (160,105)),
              #Menu("CREDITS", (176, 155)),
              #Menu("OPTIONS", (173, 205)),
              #Menu("QUIT GAME",(158, 255))]

     menu_words = [Menu("NEW GAME", (440, 455)),
              Menu("DRAW MAP", (440, 505)),
              Menu("QUIT GAME",(438, 555))]

     background = pygame.image.load("img/background.jpg")
     game = Game()
     lvl = Construction()
     sound2.play(-1)
     while True:
          pygame.mouse.set_visible(True)
          pygame.event.pump()  #obsluga dzialan wewnetrznych

          (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
          screen.blit(background, (0,0)) #wypelnienie
          for option in menu_words:
               if option.rect.collidepoint(pygame.mouse.get_pos()):   #sprawdza czy kursor znajduje
                                                                      #sie wewnatrz prostokata
                    option.hover_text = True
                    mouse_position = pygame.mouse.get_pos() #pozycja myszki to krotka (x, y)
                    #print(mouse_position)
                    if 440 < mouse_position[0] < 676 and 455 < mouse_position[1] < 488:
                         if pressed1==1:
                              print("NEW GAME")
                              sound.play()
                              sound2.stop()
                              game.blocks.remove(game.blocks)
                              game.run()

                    if 440 < mouse_position[0] < 678 and 505 < mouse_position[1] < 538:
                         if pressed1==1:
                              print("DRAW MAP")
                              sound.play()
                              sound2.stop()
                              game.blocks.remove(game.blocks)
                              lvl.run()

                    if 438 < mouse_position[0] < 676 and 558 < mouse_position[1] < 588:   # +-----------------------+
                         if pressed1==1:                                                  # | to jest dla QUIT GAME |
                              print("QUIT GAME")
                              sound.play()
                              exit()
               else:
                    option.hover_text = False
               option.draw()
          pygame.display.update()