from PIL import Image
import webcolors

def get_color_name(rgb):
    try:
        return webcolors.rgb_to_name(rgb)
    except ValueError:
        return f"rgb({rgb[0]}, {rgb[1]}, {rgb[2]})"

def color_rectangle(rgb):
    r, g, b = rgb
    return f"\033[48;2;{r};{g};{b}m   \033[0m"


img = Image.open("21_million_orange_pixels.png")

img = img.convert("RGB")

color_counts = img.getcolors(maxcolors=img.width * img.height)

total_pixels = sum(count for count, _ in color_counts)
color_summary = {color: count for count, color in color_counts}

sorted_color_summary = sorted(color_summary.items(), key=lambda item: item[1], reverse=True)

total_unique_colors = len(color_summary)

print(f"Total number of pixels: {total_pixels}")
print(f"Total unique colors: {total_unique_colors}")
print("Color breakdown:")

for color, count in sorted_color_summary:
    color_name = get_color_name(color)
    rectangle = color_rectangle(color)
    print(f"{rectangle} Color {color_name} : {count} pixels")


# pip install pillow webcolors
# python main.py