from PIL import Image
im = Image.open("test.jpg")
k=max(im.getcolors(im.size[0]*im.size[1]))
