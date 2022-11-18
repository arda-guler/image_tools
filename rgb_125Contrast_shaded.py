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

    print("\nApplying 125 contrast to " + filetitle + fileextension + "\n")

    channel_num = len(pixels[0,0])

    def contrastify(r, g, b, a=None):

        selected_color = None
        lowest_dist = None
        
        for color in colors:
            current_dist = (color[0] - r)**2 + (color[1] - g)**2 + (color[2] - b)**2

            if not lowest_dist or current_dist < lowest_dist:
                selected_color = color
                lowest_dist = current_dist

        if a==None:
            return selected_color[0], selected_color[1], selected_color[2]
        else:
            return selected_color[0], selected_color[1], selected_color[2], a

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
                r, g, b = contrastify(r, g, b)
                pixels[x, y] = (r, g, b)

                i += 1
                if i % 50000 == 0 and i > 0:
                    print("Still working...", i/i_full*100/2, "%")
                
        
    # R, G, B, Alpha channels
    elif channel_num == 4:
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                r, g, b, a = pixels[x, y][0], pixels[x, y][1], pixels[x, y][2], pixels[x, y][3]
                r, g, b, a = contrastify(r, g, b, a)
                pixels[x, y] = (r, g, b, a)

                i += 1
                if i % 50000 == 0 and i > 0:
                    print("Still working...", i/i_full*100/2, "%")

    image.save(filetitle + "_125Contrast" + fileextension)

generate_colors()
main()
