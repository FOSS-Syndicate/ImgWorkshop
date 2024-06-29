import swatcher

print(r"  ___               __        __         _        _                 ")
print(r" |_ _|_ __ ___   __\\ \      / /__  _ __| | _____| |__   ___  _ __  ")
print(r"  | || '_ ` _ \ / _`\\ \ /\ / / _ \| '__| |/ / __| '_ \ / _ \| '_ \ ")
print(r"  | || | | | | | (_| \\ V  V / (_) | |  |   <\__ \ | | | (_) | |_) |")
print(r" |___|_| |_| |_|\__, |\\_/\_/ \___/|_|  |_|\_\___/_| |_|\___/| .__/ ")
print(r"                |___/                                        |_|    ") 


print("1. Swatch Generation")
print("2. Watermarker")
print("3. Base64 Encoder")
user_input = input("Choose and operation: ")

if user_input == 1:
    # Swatch function
elif user_input == 2:
    # Watermark function
elif user_input == 3:
    # base64 function
else:
    print("Invalid arguement! Please choose a valid argument")