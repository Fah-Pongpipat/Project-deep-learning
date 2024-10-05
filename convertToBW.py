import os
from PIL import Image, ImageOps

# Define input and output folders
input_folder = 'Dataset\HappyCropped'
output_folder = 'Dataset\HappyCroppedBW'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each image in the folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        image_path = os.path.join(input_folder, filename)
        
        # Open the image
        img = Image.open(image_path)
        
        # Convert to grayscale (black and white)
        bw_img = ImageOps.grayscale(img)
        
        # Save the black and white image to the output folder
        output_path = os.path.join(output_folder, f'bw_{filename}')
        bw_img.save(output_path)

print("All images have been converted to black and white.")
