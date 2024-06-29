from PIL import Image


def read_file(filename):
    with open(filename,"r") as file:
        for line in file:
            params = line.split(":")
            name, color = params[0], params[1]
            print(name, "FFF" ,color)
            create_image(name, color)


def create_image(name, color):
    im = Image.new("RGB", (50,50), color)
    im.save(f"./swatch-output/{name}.png")


def swatcher():
    filename = input("Enter the location of the file containing all the color codes: ")
    read_file(filename)


def encode_bas64():
    filename = input("Enter the path to the image to be converted to Base64: ")
    # Open the image file
    with open(filename, "rb") as f:
        image = Image.open(f)

    import base64
    # Convert the image to base64 format
    with open("base.jpg", "rb") as f:
        encoded_image = base64.b64encode(f.read())

    # Save the encoded image to a file
    with open(f"./base64-output/{filename}.txt", "w") as f:
        f.write(encoded_image.decode("utf-8"))
    print("Saved the output .txt in the bas64-out directory")


def select_choice():
    while True:
        print("1. Swatch Generation")
        print("2. Watermarker")
        print("3. Base64 Encoder")
        user_input = input("Choose and operation: ")

        if user_input == "1":
            print("Swatcher/")  # To Link Script
            swatcher()
            break
        elif user_input == "2":
            print("Watermarker/") # To Link Script
            break
        elif user_input == "3":
            print("Base64 Encoder/") # To Link Script
            encode_bas64()
            break
        elif user_input == "q":
            print("Bye Bye!!") # To Link Script
            quit()
        else:
            print("Invalid arguement! Please choose a valid argument")


def main():
    print(r"  ___               __        __         _        _                 ")
    print(r" |_ _|_ __ ___   __\\ \      / /__  _ __| | _____| |__   ___  _ __  ")
    print(r"  | || '_ ` _ \ / _`\\ \ /\ / / _ \| '__| |/ / __| '_ \ / _ \| '_ \ ")
    print(r"  | || | | | | | (_| \\ V  V / (_) | |  |   <\__ \ | | | (_) | |_) |")
    print(r" |___|_| |_| |_|\__, |\\_/\_/ \___/|_|  |_|\_\___/_| |_|\___/| .__/ ")
    print(r"                |___/                                        |_|    ") 

    select_choice()

if __name__ == "__main__":
    main()
