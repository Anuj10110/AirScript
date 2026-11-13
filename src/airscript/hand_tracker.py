import time

import cv2
import mediapipe as mp

class HandTracker:
    """Detects hands and returns the index fingertip position."""

    def __init__(self, model_path="models/hand_landmarker.task"):
        self.model_path = model_path

        options = mp.tasks.vision.HandLandmarkerOptions(
            base_options=mp.tasks.BaseOptions(
                model_asset_path=self.model_path
            ),
            running_mode=mp.tasks.vision.RunningMode.VIDEO,
            num_hands=1,
        )

        self.landmarker = (
            mp.tasks.vision.HandLandmarker.create_from_options(options)
        )

        self.start_time = time.monotonic()

    
    def get_fingertip(self, frame):
        """Return the index fingertip's normalized (x, y), or None."""

        # OpenCV uses BGR; MediaPipe expects RGB.
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Wrap the NumPy image in a MediaPipe Image object.
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame,
        )

        # VIDEO mode requires increasing timestamps in milliseconds.
        timestamp_ms = int(
            (time.monotonic() - self.start_time) * 1000
        )

        result = self.landmarker.detect_for_video(
            mp_image, timestamp_ms
        )

        if not result.hand_landmarks:
            return None

        # Get the landmarks for the detected hand.
        landmarks = result.hand_landmarks[0]

        # Get the index fingertip coordinates.
        tip = landmarks[8]
        x, y = tip.x, tip.y

        # Check whether each finger is raised.
        index_up = landmarks[8].y < landmarks[6].y
        middle_up = landmarks[12].y < landmarks[10].y
        ring_up = landmarks[16].y < landmarks[14].y
        pinky_up = landmarks[20].y < landmarks[18].y

        # Draw only when the index finger is up
        # and the other three fingers are down.
        drawing = (
            index_up
            and not middle_up
            and not ring_up
            and not pinky_up
        )

        return x, y, drawing


    def close(self):
        """Release MediaPipe's hand-tracking resources."""
        self.landmarker.close()
