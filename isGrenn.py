import pyautogui
from PIL import ImageGrab
import time

# Define the pixel coordinates you want to grab
x, y = 761, 271

# Introduce a 2-second delay
time.sleep(2)

# Capture a screenshot of the specified pixel
screenshot = ImageGrab.grab(bbox=(x, y, x + 1, y + 1))

# Get the color of the pixel
pixel_color = screenshot.getpixel((0, 0))

# Define a threshold for considering a pixel as green
green_threshold = 100

# Check if the pixel is approximately green
is_green = pixel_color[1] > green_threshold and pixel_color[0] < green_threshold and pixel_color[2] < green_threshold

# Print the RGB values and color classification
if is_green:
    print(f"Pixel Color at ({x}, {y}): RGB{pixel_color} (Approximately green)")
else:
    print(f"Pixel Color at ({x}, {y}): RGB{pixel_color} (Not green)")
