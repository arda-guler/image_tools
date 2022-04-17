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

    print("\nApplying alternative RGB contrast to " + filetitle + fileextension + "\n")

    channel_num = len(pixels[0,0])

    def contrastify(r, g, b, a=None):
        
        bright = 255

        dist_red = ((255-r)**2 + g**2 + b**2)**(0.5)
        dist_green = (r**2 + (255-g)**2 + b**2)**(0.5)
        dist_blue = (r**2 + g**2 + (255-b)**2)**(0.5)
        dist_magenta = ((255-r)**2 + g**2 + (255-b)**2)**(0.5)
        dist_yellow = ((255-r)**2 + (255-g)**2 + b**2)**(0.5)
        dist_cyan = (r**2 + (255-g)**2 + (255-b)**2)**(0.5)
        dist_white = ((255-r)**2 + (255-g)**2 + (255-b)**2)**(0.5)

        dists = [dist_red, dist_green, dist_blue, dist_magenta, dist_yellow, dist_cyan, dist_white]

        if dist_red == min(dists):
            r = bright
            g = 0
            b = 0
        elif dist_green == min(dists):
            r = 0
            g = bright
            b = 0
        elif dist_blue == min(dists):
            r = 0
            g = 0
            b = bright
        elif dist_magenta == min(dists):
            r = bright
            g = 0
            b = bright
        elif dist_yellow == min(dists):
            r = bright
            g = bright
            b = 0
        elif dist_cyan == min(dists):
            r = 0
            g = bright
            b = bright
        elif dist_white == min(dists):
            r = bright
            g = bright
            b = bright

        if not a:
            return r, g, b
        else:
            return r, g, b, a

    # user comforting variable
    # very important
    i = 0

    # R, G, B channels
    if channel_num == 3:
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                i += 1
                r, g, b = pixels[x, y][0], pixels[x, y][1], pixels[x, y][2]
                r, g, b = contrastify(r, g, b)
                pixels[x, y] = (r, g, b)

                i += 1
                if i % 5000000 == 0 and i > 0:
                    print("Still working...")
                
        
    # R, G, B, Alpha channels
    elif channel_num == 4:
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                r, g, b, a = pixels[x, y][0], pixels[x, y][1], pixels[x, y][2], pixels[x, y][3]
                r, g, b, a = contrastify(r, g, b, a)
                pixels[x, y] = (r, g, b, a)

                i += 1
                if i % 5000000 == 0 and i > 0:
                    print("Still working...")

    image.save(filetitle + "_richContrast" + fileextension)

main()
