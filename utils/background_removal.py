from rembg import remove
from PIL import Image

def remove_bg(image_file):
    image = Image.open(image_file).convert("RGBA")
    return remove(image)
