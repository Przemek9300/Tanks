import pygame

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
           
pygame.init()
#screen = pygame.display.set_mode((480,320))
menu_fonts = pygame.font.Font(None, 40) #tworzenie nowej czcionki z pliku
                                        #(plik, rozmiar)
