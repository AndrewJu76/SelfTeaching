from PIL import Image,ImageDraw,ImageFont

def add_text(im,text,topleft,size,color):
    font = ImageFont.truetype('arial.ttf',size)
    draw = ImageDraw.Draw(im)
    # draw.text(topleft,text,font=font,fill=color)
    draw.multiline_text(topleft, text, font=font, fill=color)
    return im


if __name__ == '__main__':
    with Image.open("./images/racecar.jpg") as im:
        im = add_text(im,"Hello world!\nIt's good to see you.",(100,100),200,(255,255,255))
        im.save(".\\saved_images\\racecar with text.jpg")

