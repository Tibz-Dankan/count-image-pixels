# Image Pixel Counter

This script counts the total number of pixels in an image using the `PIL` (Pillow) library.

## Prerequisites

Ensure you have Python installed (version 3.x recommended). You can download Python from [python.org](https://www.python.org/).

## Installation

1. Clone this repository or download `main.py`.
2. Install the required dependencies using pip:
   ```sh
   pip install pillow
   ```

## Usage

1. Place your image (`21_million_orange_pixels.png`) in the same directory as `main.py`.
2. Run the script using the following command:
   ```sh
   python main.py
   ```
3. The total number of pixels will be displayed in the terminal.

## Notes

- Ensure that the image file `21_million_orange_pixels.png` exists in the same directory as `main.py`.
- You can modify the script to work with other image files by changing the filename in `Image.open()`.
