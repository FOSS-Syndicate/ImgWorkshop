from PIL import Image

def encode_bas64(filename):
    # Open the image file
    with open(filname, "rb") as f:
        image = Image.open(f)

    import base64
    # Convert the image to base64 format
    with open("base.jpg", "rb") as f:
        encoded_image = base64.b64encode(f.read())

    # Save the encoded image to a file
    with open("image.txt", "w") as f:
        f.write(encoded_image.decode("utf-8"))