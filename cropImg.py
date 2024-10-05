import os
from PIL import Image

# Define paths
input_folder = "Dataset\\Neutral"
output_folder = "Dataset\\NeutralCropped"
target_size = (224, 224)  # Set desired square size (e.g., 224x224)

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to center crop image to square
def crop_center(image):
    width, height = image.size
    new_size = min(width, height)
    left = (width - new_size) / 2
    top = (height - new_size) / 2
    right = (width + new_size) / 2
    bottom = (height + new_size) / 2
    return image.crop((left, top, right, bottom))

# Process each image in the folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        image_path = os.path.join(input_folder, filename)
        
        # Open the image
        img = Image.open(image_path)
        
        # Crop the image to the center square
        cropped_img = crop_center(img)
        
        # Resize the cropped image to the target size (e.g., 224x224)
        resized_img = cropped_img.resize(target_size)
        
        # Save the processed image in the output folder
        output_path = os.path.join(output_folder, f'resized_{filename}')
        resized_img.save(output_path)

print(f"Images have been cropped and resized to {target_size[0]}x{target_size[1]}.")
