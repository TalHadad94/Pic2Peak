# Not usable for now...

from PIL import Image

print("Tal: You are in the Image_Handle.py file")

def Open_Image(imagePath): # Send path to open image
        print("You are in the Open_Image method")
        file = imagePath
        with Image.open(file) as img:
            img.load()

        type(img)

        isinstance(img, Image.Image)

        img.show()