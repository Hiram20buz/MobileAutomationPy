import pyautogui

# Define the coordinates of the region you want to capture (left, top, width, height)
region = (100, 100, 800, 600)

# Take a screenshot of the specified region
screenshot = pyautogui.screenshot(region=region)

# Save the screenshot to a file
screenshot.save("region_screenshot.png")
print("Screenshot of the specified region saved as 'region_screenshot.png'")
