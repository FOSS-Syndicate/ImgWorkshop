from PIL import Image



# to open the image
image = Image.open("base.jpg")
width, height = image.size
margin = 10

# image watermark
size = (100, 100)
watermark_image = Image.open("watermark.png")

# to keep the aspect ration in intact
watermark_image.thumbnail(size)

# add watermark
copied_image = image.copy()

# Position
x = x = width - 100 - margin
y = height - 100 - margin


# base image
copied_image.paste(watermark_image, (x, y), watermark_image)

copied_image.save('final.png')

# pasted the crop image onto the base image
plt.imshow(copied_image)