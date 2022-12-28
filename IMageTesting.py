import PIL.Image
# So a guide that works! https://stackoverflow.com/questions/10748822/img-image-openfp-attributeerror-class-image-has-no-attribute-open

fp = open("Weyland.png","rb")
img = PIL.Image.open(fp)
img.show()