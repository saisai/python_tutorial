import Image, ImageFilter

im = Image.open('/Users/Laozhikun/Pictures/leaf.bmp')
w,h = im.size

# im.thumbnail((w/2,h/2))
# im.save("/Users/Laozhikun/Pictures/leaf2.bmp")

im = im.filter(ImageFilter.BLUR)
im.save("/Users/Laozhikun/Pictures/leaf2.bmp")