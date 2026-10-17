
import cv2

from airscript.camera import Camera
from airscript.hand_tracker import HandTracker
from airscript.stroke import Stroke
from airscript.drawing_canvas import DrawingCanvas


def main():
    camera = Camera()
    tracker = HandTracker()
    canvas = DrawingCanvas(width=1280, height=720)

    # Stores the stroke currently being drawn.
    current_stroke = None

    try:
        print("AirScript is running!")
        print("Raise your index finger to draw.")
        print("Make a fist to stop drawing.")
        print("Press C to clear the canvas.")
        print("Press Q to quit.")

        while True:
            # 1. Capture the webcam frame.
            frame = camera.read_frame()

            # 2. Detect the fingertip and drawing gesture.
            result = tracker.get_fingertip(frame)

            if result is not None:
                x_normalized, y_normalized, drawing = result

                height, width, _ = frame.shape

                # Convert normalized coordinates to camera pixels.
                x = int(x_normalized * width)
                y = int(y_normalized * height)

                # Show the fingertip on the webcam feed.
                cv2.circle(frame, (x, y), 8, (0, 255, 0), -1)

                if drawing:
                    # Start a new stroke when drawing begins.
                    if current_stroke is None:
                        current_stroke = Stroke()

                    points = current_stroke.get_points()

                    # Connect the previous point to the current point.
                    if points:
                        previous_x, previous_y = points[-1]

                        start_point = (
                            min(int(previous_x * canvas.width),
                                canvas.width - 1),
                            min(int(previous_y * canvas.height),
                                canvas.height - 1),
                        )

                        end_point = (
                            min(int(x_normalized * canvas.width),
                                canvas.width - 1),
                            min(int(y_normalized * canvas.height),
                                canvas.height - 1),
                        )

                        canvas.draw_line(start_point, end_point)

                    # Save the current normalized position.
                    current_stroke.add_point(
                        x_normalized,
                        y_normalized,
                    )

                    status = "DRAWING"

                else:
                    # End the current stroke.
                    current_stroke = None
                    status = "NOT DRAWING"

            else:
                # Don't connect separate movements across missing frames.
                current_stroke = None
                status = "NO HAND DETECTED"

            # Display the current gesture status on the camera.
            cv2.putText(
                frame,
                status,
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0) if status == "DRAWING"
                else (0, 0, 255),
                2,
            )

            # 3. Show the camera and persistent drawing canvas.
            cv2.imshow("AirScript - Camera", frame)
            cv2.imshow("AirScript - Drawing Canvas", canvas.get_canvas())

            # 4. Handle keyboard controls.
            key = cv2.waitKey(1) & 0xFF

            if key == ord("c"):
                canvas.clear()
                current_stroke = None
                print("Canvas cleared!")

            elif key == ord("q"):
                break

    finally:
        tracker.close()
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
