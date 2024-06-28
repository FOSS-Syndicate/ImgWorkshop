def read_file():
    with open("./colors.txt","r") as file:
        for line in file:
            params = line.split(":")
            name, color = params[0], params[1]
            print(name, "FFF" ,color)
            create_image(name, color)


def main():
    read_file()


if __name__ == "__main__":
    main()