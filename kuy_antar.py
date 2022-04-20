from matplotlib import image
import pygame

# init pygame
pygame.init()

# mengatur ukuran layar
screen = pygame.display.set_mode((600, 600))

# set caption
pygame.display.set_caption("Kuy Antar")
# set logo
pygame.display.set_icon(pygame.image.load("logo.png"))

# menambahkan kurir
def kurir(x, y):
    image = pygame.image.load('kurir1.png')
    screen.blit(image, (x, y))

x = 100
y = 300

x_point = 0
y_point = 0 

# menambakan destinasi
def destinasi(x, y):
    image = pygame.image.load('destinasi.png')
    screen.blit(image, (x, y))





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT or event.key == ord('a'):
            x_point -= 1
          if event.key == pygame.K_RIGHT or event.key == ord('d'):
            x_point += 1
          if event.key == pygame.K_UP or event.key == ord('w'):
            y_point -= 1
          if event.key == pygame.K_DOWN or event.key == ord('s'):
            y_point += 1

        if event.type == pygame.KEYUP:
          if event.key == pygame.K_LEFT or event.key == ord('a'):
            x_point = 0
          if event.key == pygame.K_RIGHT or event.key == ord('d'):
            x_point = 0
          if event.key == pygame.K_UP or event.key == ord('w'):
            y_point = 0
          if event.key == pygame.K_DOWN or event.key == ord('s'):
            y_point = 0


    # membuat batasan layar agar kurir tidak keluar dari layar
    if x <= 0:
        x = 0
    elif x >= 500:
        x = 500
    if y <= 0:
        y = 0
    elif y >= 500:
        y = 500

    
    screen.fill((255,255,255))
        
    x += x_point
    y += y_point

    # menampilkann gambar
    
    destinasi(50, 50)
    destinasi(450, 50)
    destinasi(450, 450)
    destinasi(50, 450)

    
    kurir(x, y)
    pygame.display.update()

pygame.quit()


