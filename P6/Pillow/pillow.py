from PIL import Image

im_name = "flower.jpg"
with Image.open(im_name) as img:
    img.load()

rotated_im = img.rotate(45)

rotated_im.show()

