import noise
from random import randint
from PIL import Image
from settings import *


shape = (WINDOW_WIDTH, WINDOW_HEIGHT)

scale = 400.0
octaves = 1 #2
lacunarity = 2.0 #2.0
persistence = 0.2 #0.5



def t(value):
    if value > 0.2:
        return (127,127,127)
    else:
        return (17, 139, 86)

def creerMap():
    seed = int(randint(0, 1000))
    print(seed)
    image_filepath = "noise.png"

    image = Image.new("RGB", shape)
    for x in range(shape[0]):
        for y in range(shape[1]):
            value = noise.pnoise2(x/scale,
                                y/scale,
                                octaves=octaves,
                                lacunarity=lacunarity,
                                repeatx = shape[0],
                                repeaty = shape[1],
                                base = seed)
            image.putpixel((x,y), t(value))

    #image.show()
    image.save(image_filepath)

