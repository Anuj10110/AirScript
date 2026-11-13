import cv2
import numpy as np

class DrawingCanvas:
    """Creates a canvas that remembers drawn strokes."""

    def __init__(self, width=1280, height=720):
        self.width = width
        self.height = height

        # Create a blank white canvas.
        self.canvas = np.ones(
            (height, width, 3),
            dtype=np.uint8
        ) * 255

    def draw_line(self, start_point, end_point, thickness=4):
        """Draw a line between two pixel coordinates."""
        cv2.line(
            self.canvas,
            start_point,
            end_point,
            (0, 0, 0),
            thickness
        )

    def get_canvas(self):
        """Return the current canvas image."""
        return self.canvas

    def clear(self):
        """Erase everything and create a blank canvas."""
        self.canvas[:] = 255
