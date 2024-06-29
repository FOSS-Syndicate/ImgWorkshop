import subprocess

def select_choice():

    while True:
        print("1. Swatch Generation")
        print("2. Watermarker")
        print("3. Base64 Encoder")
        user_input = input("Choose and operation: ")

        if user_input == "1":
            print("Swatcher/")  # To Link Script
            subprocess.call("./swatcher.py", shell=True)
        elif user_input == "2":
            print("Watermarker/") # To Link Script
            break
        elif user_input == "3":
            print("Base64 Encoder/") # To Link Script
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
