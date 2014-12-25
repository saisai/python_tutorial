# -*- coding:utf-8 -*-
import Image,ImageFont,ImageFilter,ImageDraw
import random

# random char
def rndChar():
	return chr(random.randint(65,90))

def rndColor():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4
height = 60

image = Image.new('RGB', (width, height), (255, 255, 255))

font = ImageFont.truetype('/Users/Laozhikun/Library/Fonts/UbuntuMono-R.ttf', 36)

draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('/Users/Laozhikun/Pictures/checkcode.jpg', 'jpeg');