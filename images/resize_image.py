from PIL import Image

# Open the BMP image file
image = Image.open("C:/Users/jacop/OneDrive/Desktop/Learning python/python crash course/alien_invasion_game/images/raindrop.bmp")

# Set the new size (width, height) - adjust as needed
new_size = (20, 40)

# Resize the image
resized_image = image.resize(new_size)

# Save the resized image
resized_image.save("C:/Users/jacop/OneDrive/Desktop/Learning python/python crash course/alien_invasion_game/images/raindrop_resized.bmp")

# Optionally, show the resized image
resized_image.show()
print("Resized done!")