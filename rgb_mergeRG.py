from PIL import Image

def import_image():
    filename = input("Image file name:")

    try:
        image1 = Image.open(filename + "_redFiltered.png")
        image2 = Image.open(filename + "_greenFiltered.png")
        filename = filename + ".png"
    except:
        try:
            image1 = Image.open(filename + "_redFiltered.jpg")
            image2 = Image.open(filename + "_greenFiltered.jpg")
            filename = filename + ".jpg"
        except:
            print("Can not access file. Please check file name and file extension!")
            quit()
        
    pixels1 = image1.load()
    pixels2 = image2.load()

    filename = filename.split(".")

    if len(filename) == 2:
        filetitle = filename[0]
        fileextension = "." + filename[1]

    else:
        filetitle = filename[0]
        for i in range(1, len(filename)-1):
            filetitle += "." + filename[i]
        fileextension = "." + filename[-1]

    return image1, image2, pixels1, pixels2, filetitle, fileextension

def main():
    image1, image2, pixels1, pixels2, filetitle, fileextension = import_image()

    print("\nRG merging " + filetitle + fileextension + "\n")

    channel_num = len(pixels1[0,0])

    def filter_red(r, g, b, a=None):

        if not a:
            return r, 0, 0
        else:
            return r, 0, 0, a

    def filter_green(r, g, b, a=None):

        if not a:
            return 0, g, 0
        else:
            return 0, g, 0, a

    def filter_blue(r, g, b, a=None):

        if not a:
            return 0, 0, b
        else:
            return 0, 0, b, a

    # user comforting variable
    # very important
    i = 0

    # R, G, B channels
    if channel_num == 3:
        for y in range(image1.size[1]):
            for x in range(image1.size[0]):
                i += 1
                r, g, b = pixels1[x, y][0], pixels2[x, y][1], 0
                pixels1[x, y] = (r, g, b)

                i += 1
                if i % 5000000 == 0 and i > 0:
                    print("Still working...")
                
        
    # R, G, B, Alpha channels
    elif channel_num == 4:
        for y in range(image1.size[1]):
            for x in range(image1.size[0]):
                r, g, b, a = pixels1[x, y][0], pixels2[x, y][1], 0, pixels1[x, y][3] + pixels2[x, y][3] + 0
                pixels1[x, y] = (r, g, b, a)

                i += 1
                if i % 5000000 == 0 and i > 0:
                    print("Still working...")

    image1.save(filetitle + "_rgFilterMerged" + fileextension)

main()
