
import cv2

from airscript.camera import Camera
from airscript.hand_tracker import HandTracker


camera = Camera()
tracker = HandTracker()

try:
    print("Show one hand to the camera. Press Q to quit.")

    while True:
        frame = camera.read_frame()
        fingertip = tracker.get_fingertip(frame)

        if fingertip is not None:
            x_normalized, y_normalized = fingertip
            height, width, _ = frame.shape

            x = int(x_normalized * width)
            y = int(y_normalized * height)

            # Draw a circle at the fingertip position on the frame.
            cv2.circle(frame, (x, y), 10, (0, 255, 255), -1)
            print(f"Fingertip: x={x}, y={y}", end="\r")

        cv2.imshow("AirScript - Tracker Test", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    tracker.close()
    camera.release()
    cv2.destroyAllWindows()
