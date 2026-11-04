from PIL import Image

def scale_by_factor(im, factor):
    return im.resize((round(im.width * factor), round(im.height * factor)))

if __name__ == '__main__':
    with Image.open(".\\images\\squirrel.jpg") as img:
        rotated_img = img.rotate(45,expand=True)
        scaled_img = scale_by_factor(img, 0.5)
        rotated_img.save(".\\saved_images\\rotated squirrel.jpg")
        scaled_img.save(".\\saved_images\\scaled squirrel.jpg")