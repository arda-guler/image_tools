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

    channel_num = len(pixels[0,0])

    def separate_shaded(r, g, b, a = None):
        # check alpha
        if a and a > 127:
            alpha = 255
        else:
            alpha = 0

        brightness = (r + g + b)/(255*3)

        # check if one color is greater than others
        if r > g and r > b:
            return int(255 * brightness), 0, 0, alpha

        elif g > r and g > b:
            return 0, int(255 * brightness), 0, alpha

        elif b > r and b > g:
            return 0, 0, int(255 * brightness), alpha

        # check if two largest colors have equal value
        elif r == g and r > b:
            return int(255 * brightness), int(255 * brightness), 0, alpha

        elif r == b and r > g:
            return int(255 * brightness), 0, int(255 * brightness), alpha

        elif g == b and g > r:
            return 0, int(255 * brightness), int(255 * brightness), alpha

        # check if all colors have equal value (black, gray or white pixel)
        elif r == g and g == b:
            return int(255 * brightness), int(255 * brightness), int(255 * brightness), alpha

    # user comforting variable
    # very important
    i = 0

    print("\nApplying shaded RGB separation to " + filetitle + fileextension + "\n")
    
    # R, G, B channels
    if channel_num == 3:
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                r, g, b = pixels[x, y][0], pixels[x, y][1], pixels[x, y][2]
                r, g, b, a = separate_shaded(r, g, b)
                pixels[x, y] = (r, g, b)

                i += 1
                if i % 5000000 == 0 and i > 0:
                    print("Still working...")
        
    # R, G, B, Alpha channels
    elif channel_num == 4:
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                r, g, b, a = pixels[x, y][0], pixels[x, y][1], pixels[x, y][2], pixels[x, y][3]
                r, g, b, a = separate_shaded(r, g, b, a)
                pixels[x, y] = (r, g, b, a)

                i += 1
                if i % 5000000 == 0 and i > 0:
                    print("Still working...")

    image.save(filetitle + "_RGBseparate_shaded" + fileextension)

main()
