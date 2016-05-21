# Draw class

import Image

img = Image.new('RGB', (255,255), "black")
pixels = img.load()
 
for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        pixels[i,j] = (i, j, 100) # set the colour accordingly
 
def draw():
	img.show()

def set_pixel(self, x, y, colour):
	pixels[x, y] = (x, y, colour)