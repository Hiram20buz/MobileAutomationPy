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

# Print the RGB values of the pixel color
print(f"Pixel Color at ({x}, {y}): RGB{pixel_color}")
