"""
main.py

Entry point of the Digital Image Processing Laboratory.
"""

from pathlib import Path

from core.image_loader import ImageLoader
from core.display import Display
from core.image_info import ImageInfo


def main():

    # ----------------------------------------------------
    # Locate the image
    # ----------------------------------------------------
    image_path = (
        Path(__file__).resolve().parent
        / "images"
        / "original"
        / "chest_x-rayB.png"
    )

    print("=" * 60)
    print(" DIGITAL IMAGE PROCESSING LAB ")
    print("=" * 60)

    print(f"Loading image:\n{image_path}\n")

    # ----------------------------------------------------
    # Load image
    # ----------------------------------------------------
    image = ImageLoader.load_image(image_path)

    # ----------------------------------------------------
    # Basic information
    # ----------------------------------------------------
    image_info = ImageInfo.get_image_info(image)
    print("Basic Information:")
    for key, value in image_info.items():
        print(f"  {key.capitalize()}: {value}")

    #----------------------------------------------------
    # get image name
    #----------------------------------------------------
    image_name = image_path.name
    
    #----------------------------------------------------
    # Display image
    #----------------------------------------------------
    Display.show_image(image_name, image)


if __name__ == "__main__":
    main()