from PIL import Image

# Open the BMP image file
image = Image.open("C:/Users/jacop/OneDrive/Desktop/Learning python/python crash course/Part 2 Alien invasion game/images/star.bmp")

# Set the new size (width, height) - adjust as needed
new_size = (40, 40)

# Resize the image
resized_image = image.resize(new_size)

# Save the resized image
resized_image.save("C:/Users/jacop/OneDrive/Desktop/Learning python/python crash course/Part 2 Alien invasion game/images/star_resized.bmp")

# Optionally, show the resized image
resized_image.show()
print("Resized done!")