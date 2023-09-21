from PIL import Image, ImageOps
import sys
import os

def main():
    # Check the number of command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        # Define supported image formats
        valid_formats = [".jpg", ".jpeg", ".png"]

        # Split input and output file paths into name and extension
        input_parts = os.path.splitext(sys.argv[1])
        output_parts = os.path.splitext(sys.argv[2])

        # Check if the output format is valid
        if output_parts[1].lower() not in valid_formats:
            sys.exit("Invalid output format")

        # Check if input and output have different extensions
        if input_parts[1].lower() != output_parts[1].lower():
            sys.exit("Input and output have different extensions")

        # Call the function to edit the photo
        edit_photo(sys.argv[1], sys.argv[2])

def edit_photo(input_path, output_path):
    try:
        # Load the shirt image
        shirt = Image.open("shirt.png")

        # Open the input image
        with Image.open(input_path) as input_image:
            # Crop and resize the input image to match the shirt's size
            input_cropped = ImageOps.fit(input_image, shirt.size)

            # Paste the shirt on the input image using the shirt as a mask
            input_cropped.paste(shirt, mask=shirt)

            # Save the edited image
            input_cropped.save(output_path)
    except FileNotFoundError:
        sys.exit("Input image does not exist")

if __name__ == "__main__":
    main()
