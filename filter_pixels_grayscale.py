from PIL import Image

colors = []

def generate_colors():
    global colors
    r = 0
    g = 0
    b = 0

    for ri in range(5):
        if ri > 0:
            r = 64*ri - 1
        else:
            r = 0

        for gi in range(5):
            if gi > 0:
                g = 64*gi - 1
            else:
                g = 0

            for bi in range(5):
                if bi > 0:
                    b = 64*bi - 1
                else:
                    b = 0
                    
                colors.append([r, g, b])

def import_image():
    filename = input("Image file name:")

    if not "." in filename:
        try:
            image = Image.open(filename + ".png")
            filename = filename + ".png"
        except:
            try:
                image = Image.open(filename + ".jpg")
                filename = filename + ".jpg"
            except:
                print("Can not access file. Please check file name and file extension!")
                quit()
    else:
        image = Image.open(filename)
        
    pixels = image.load()

    filename = filename.split(".")

    if len(filename) == 2:
        filetitle = filename[0]
        fileextension = "." + filename[1]

    else:
        filetitle = filename[0]
        for i in range(1, len(filename)-1):
            filetitle += "." + filename[i]
        fileextension = "." + filename[-1]

    return image, pixels, filetitle, fileextension

def main():
    global colors
    image, pixels, filetitle, fileextension = import_image()

    print("\nApplying brightness filter to " + filetitle + fileextension + "\n")

    channel_num = len(pixels[0,0])

    
    filter_val_default = 100
    filter_val_inp = input("Filter brightness (" + str(filter_val_default) + " if left blank):")
    

    if not filter_val_inp:
        filter_val = filter_val_default
    else:
        filter_val = int(filter_val_inp)

    def filter_brightness(filter_val, r, g, b, a=None):

        bright = (r + g + b)/3

        if bright > filter_val:
            bright = int(bright)
            if a==None:
                return bright, bright, bright
            else:
                return bright, bright, bright, a

        else:
            if a==None:
                return 0, 0, 0
            else:
                return 0, 0, 0, a

    # user comforting variable
    # very important
    i = 0
    i_full = image.size[0] * image.size[1]

    # R, G, B channels
    if channel_num == 3:
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                i += 1
                r, g, b = pixels[x, y][0], pixels[x, y][1], pixels[x, y][2]
                r, g, b = filter_brightness(filter_val, r, g, b)
                pixels[x, y] = (r, g, b)

                i += 1
                if i % 50000 == 0 and i > 0:
                    print("Still working...", i/i_full*100/2, "%")
                
        
    # R, G, B, Alpha channels
    elif channel_num == 4:
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                r, g, b, a = pixels[x, y][0], pixels[x, y][1], pixels[x, y][2], pixels[x, y][3]
                r, g, b, a = filter_brightness(filter_val, r, g, b, a)
                pixels[x, y] = (r, g, b, a)

                i += 1
                if i % 50000 == 0 and i > 0:
                    print("Still working...", i/i_full*100/2, "%")

    image.save(filetitle + "_filterBrightnessGrayscale" + fileextension)

generate_colors()
main()
