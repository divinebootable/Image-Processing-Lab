# core.image_info.py
import cv2

class ImageInfo:
    @staticmethod
    def get_image_info(image):
        """
        Get basic information about an image.

        Parameters
        ----------
        image : numpy.ndarray
            The image to analyze.

        Returns
        -------
        dict
            A dictionary containing the shape, data type, and value range of the image.
        """
        if image is None:
            raise ValueError("Image is None. Please provide a valid image.")

        info = {
            "shape": image.shape,
            "dtype": image.dtype,
            "min": image.min(),
            "max": image.max()
        }
        
        return info

