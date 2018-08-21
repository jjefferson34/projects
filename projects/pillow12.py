from PIL import Image

image = Image.open("axolotl.jpeg")
imdata = image.getdata()
imagelist = list(imdata)
newimagelist=[]
#print(list(imdata))
for pixel in imagelist:
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    intensity = (r + b + g)
    #print(intensity)
    if intensity < 182:
        newimagelist.append((0, 51, 76))
    if 182 < intensity <= 364:
        newimagelist.append((217, 26, 33))
    if 364 < intensity <= 546:
        newimagelist.append((112, 150, 158))
    if intensity > 546:
        newimagelist.append((252, 227, 166))

image.putdata(newimagelist)
image.show()
