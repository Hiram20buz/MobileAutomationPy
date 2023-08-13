import pyautogui
from PIL import ImageGrab
import time

def display_mouse_position_with_color(interval=1):
    try:
        while True:
            # Get the current mouse position
            x, y = pyautogui.position()
            
            # Capture a screenshot of the pixel at the current position
            screenshot = ImageGrab.grab(bbox=(x, y, x + 1, y + 1))
            
            # Get the color of the pixel
            pixel_color = screenshot.getpixel((0, 0))
            
            # Display the mouse position and pixel color
            print(f"Mouse Position - X: {x}, Y: {y} | Pixel Color: RGB{pixel_color}")
            
            # Pause for the specified interval
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nMouse position display stopped.")

# Call the function to start displaying the mouse position and pixel color
display_mouse_position_with_color()
