from PIL import Image, ImageEnhance

def enhance_image_sharpness(image_path, output_path, sharpness_factor=2.0):
    """
    Enhance the sharpness of an image.
    :param image_path: Path to the input image file.
    :param output_path: Path to save the enhanced image.
    :param sharpness_factor: Factor by which the image is sharpened. Default is 2.0.
    """
    # Open an image file
    with Image.open(image_path) as img:
        # Initialize the Sharpness enhancer
        enhancer = ImageEnhance.Sharpness(img)
        
        # Apply the sharpness filter
        img_enhanced = enhancer.enhance(sharpness_factor)
        
        # Save the enhanced image
        img_enhanced.save(output_path)
        print(f"Enhanced image saved as {output_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python increase_sharpness.py <path_to_image> <output_path> <sharpness_factor>")
        sys.exit(1)

    image_path = sys.argv[1]
    output_path = sys.argv[2]
    sharpness_factor = float(sys.argv[3])

    enhance_image_sharpness(image_path, output_path, sharpness_factor)
