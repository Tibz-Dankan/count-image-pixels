#  using PIL (pillow) library
from PIL import Image

# Open the image
img = Image.open("21_million_orange_pixels.png")

# Count the number of pixels
num_pixels = img.width * img.height

print(f"Total number of pixels: {num_pixels}")


