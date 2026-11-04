from PIL import Image,ImageDraw

def add_cross_to(im,color):
    draw = ImageDraw.Draw(im)
    draw.line((0,0)+im.size,fill=color,width=5)
    draw.line((0, im.size[1],im.size[0],0), fill=color,width=10)
    return im

def add_rectangle_to(im,topleft,rightleft,color):
    draw = ImageDraw.Draw(im)
    draw.rectangle((topleft,rightleft), fill=color)
    # draw.rectangle((topleft,(topleft[0]+size,topleft[1]+size)), fill=color)
    return im

def add_ellipse_to(im,topleft,rightleft,color):
    draw = ImageDraw.Draw(im)
    draw.ellipse((topleft,rightleft), fill=color)
    return im

if __name__ == '__main__':
    with Image.open(".\\images\\racecar.jpg") as img:
        im = add_cross_to(img,(255,0,0))
        im = add_rectangle_to(im,(50,50),(1000,1000),(0,0,255))
        im = add_ellipse_to(im,(1500,1500),(1800,1800),(255,0,0))
        img.save(".\\saved_images\\racecar with cross.jpg")