# importing the requests library
import requests
import pygame
from pygame.locals import *
from PIL import Image

# api-endpoint
number = input("what number???: ")
URL = "https://pokeapi.co/api/v2/pokemon/"
URL = URL+number
r = requests.get(url = URL)
data = r.json()

name = (data["species"]["name"])
print(name)

image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{number}.png"
image_data = requests.get(image_url).content
with open("image.jpg", "wb") as handler:
    handler.write(image_data)




pygame.init()
screen = pygame.display.set_mode((600, 700))
imp = pygame.image.load("/home/maeve/VSCode/image.jpg")
pygame.display.set_caption("show text")
# imp.open("image.jpg").convert("RGB").save("new.jpg")


white = (255, 255, 255)
black = (0, 0 , 0)
font = pygame.font.Font("pokemon.ttf", 100)
text = font.render(name, True, white)
width = text.get_rect().width
screen.blit(text,(300-(width/2), 600))


Image.open("image.jpg").convert("RGB").save("image.jpg")
image = Image.open("image.jpg")
new_image = image.resize((600, 600))
new_image.save("scaled.jpg")
imp = pygame.image.load("/home/maeve/VSCode/scaled.jpg").convert()
 
# paint screen one time
screen.blit(imp, (0, 0))


pygame.display.flip()
status = True
while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
 
pygame.quit()




