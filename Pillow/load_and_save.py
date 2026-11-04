from PIL import Image

if __name__ == '__main__':
    with Image.open(".\\images\\squirrel.jpg") as img:
        print(img.size)
        img.save(".\\saved_images\\squirrel.png")

