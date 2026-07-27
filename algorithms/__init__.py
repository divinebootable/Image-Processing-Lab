# core/image_loader.py

from pathlib import Path
import cv2
import numpy as np

class ImageLoader:
    
    @staticmethod
    def load_image(image_path: Path):
        """
        Load an image from disk.

        Parameters
        ----------
        image_path : str or Path

        Returns
        -------
        numpy.ndarray
        """
        
        image_path = Path(image_path)
        if not image_path.exists():
            raise FileNotFoundError(
                f"Image not found:\n{image_path}"
            )
        
        image = cv2.imread(str(image_path))
        
        if image is None:
            raise ValueError(
                "OpenCV could not read the image."
            )
        
        return image
