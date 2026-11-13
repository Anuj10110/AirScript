import cv2

class Camera:
    """Manages webcam access for AirScript."""

    def __init__(self, camera_index=0):
        # Create a connection to the webcam.
        self.capture = cv2.VideoCapture(camera_index)

        # Check whether the webcam opened successfully.
        if not self.capture.isOpened():
            self.capture.release()
            raise RuntimeError(
                "Could not open webcam. Check camera permissions."
            )

    def read_frame(self):
        """Return the next webcam frame."""
        success, frame = self.capture.read()

        if not success:
            raise RuntimeError("Could not read a webcam frame.")

        # Mirror the image so it behaves like a selfie preview.
        return cv2.flip(frame, 1)

    def release(self):
        """Release the webcam when we finish."""
        self.capture.release()
