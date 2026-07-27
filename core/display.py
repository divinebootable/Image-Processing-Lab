# core.display.py

import cv2

class Display:
    @staticmethod
    def show_image(window_name: str, image):
        """
        Display an image in a window.

        Parameters
        ----------
        window_name : str
            The name of the window.
        image : numpy.ndarray
            The image to display.
        """
        # also fit the image to the screen size
        screen_res = 1280, 720
        scale_width = screen_res[0] / image.shape[1]
        scale_height = screen_res[1] / image.shape[0]
        scale = min(scale_width, scale_height)
        window_width = int(image.shape[1] * scale)
        window_height = int(image.shape[0] * scale)
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(window_name, window_width, window_height)
        cv2.imshow(window_name, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    
    @staticmethod
    def close():
        """
        Close all OpenCV windows.
        """
        cv2.waitKey(0)
        cv2.destroyAllWindows()