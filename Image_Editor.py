from PIL import Image, ImageEnhance, ImageFilter
import os

path = (r"C:/Users/Christopher Turner/Pictures/Saved Pictures")
pathOut = (r"C:/Users/Christopher Turner/Pictures/EditedPhotos") 

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(90)

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'{pathOut}/{clean_name}_edited.jpg')

#python 3 image Editor.py 