from PIL import Image

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
    image, pixels, filetitle, fileextension = import_image()

    print("\nRedifying " + filetitle + fileextension + "\n")

    channel_num = len(pixels[0,0])

    def greenify(r, g, b, a=None):
        
        bright = int((r + g + b)/3)

        if not a:
            return bright, 0, 0
        else:
            return bright, 0, 0, a

    # user comforting variable
    # very important
    i = 0

    # R, G, B channels
    if channel_num == 3:
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                i += 1
                r, g, b = pixels[x, y][0], pixels[x, y][1], pixels[x, y][2]
                r, g, b = greenify(r, g, b)
                pixels[x, y] = (r, g, b)

                i += 1
                if i % 5000000 == 0 and i > 0:
                    print("Still working...")
                
        
    # R, G, B, Alpha channels
    elif channel_num == 4:
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                r, g, b, a = pixels[x, y][0], pixels[x, y][1], pixels[x, y][2], pixels[x, y][3]
                r, g, b, a = greenify(r, g, b, a)
                pixels[x, y] = (r, g, b, a)

                i += 1
                if i % 5000000 == 0 and i > 0:
                    print("Still working...")

    image.save(filetitle + "_redified" + fileextension)

main()
