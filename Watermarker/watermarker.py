from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# to open the image
image = Image.open("base.jpg")
width, height = image.size
margin = 10

# this open the photo viewer
# image.show()
#lt.imshow(image)

# image watermark
size = (100, 100)
watermark_image = Image.open("watermark.png")

