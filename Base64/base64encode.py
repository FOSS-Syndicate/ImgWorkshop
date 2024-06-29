from PIL import Image

# Open the image file
with open("base.jpg", "rb") as f:
    image = Image.open(f)

import base64
# Convert the image to base64 format
with open("base.jpg", "rb") as f:
    encoded_image = base64.b64encode(f.read())
