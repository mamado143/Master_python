from PIL import Image

# open the image
myImage = Image.open("/Users/Mido/Pictures/IMG_3097.jpg")
# Show The Image
myImage.show()

# my crop Image
myBox = (0, 0, 400, 400)
croppedImage = myImage.crop(myBox)

# Show The Image
myImage.show()