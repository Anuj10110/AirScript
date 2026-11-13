import cv2

from airscript.camera import Camera
from airscript.hand_tracker import HandTracker
from airscript.stroke import Stroke
from airscript.drawing_canvas import DrawingCanvas
from airscript.digit_predictor import DigitPredictor


def main():
    camera = Camera()
    tracker = HandTracker()
    canvas = DrawingCanvas(width=1280, height=720)
    predictor = DigitPredictor()

    current_stroke = None
    prediction_text = "Prediction: None"

    try:
        print("AirScript is running!")
        print("Raise your index finger to draw.")
        print("Make a fist to stop drawing.")
        print("Press P to recognize the digit.")
        print("Press C to clear the canvas.")
        print("Press Q to quit.")

        while True:
            # 1. Capture webcam frame.
            frame = camera.read_frame()

            # 2. Detect fingertip and drawing gesture.
            result = tracker.get_fingertip(frame)

            if result is not None:
                x_normalized, y_normalized, drawing = result

                height, width, _ = frame.shape

                x = int(x_normalized * width)
                y = int(y_normalized * height)

                cv2.circle(frame, (x, y), 8, (0, 255, 0), -1)

                if drawing:
                    if current_stroke is None:
                        current_stroke = Stroke()

                    points = current_stroke.get_points()

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

                    current_stroke.add_point(
                        x_normalized,
                        y_normalized
                    )

                    status = "DRAWING"

                else:
                    current_stroke = None
                    status = "NOT DRAWING"

            else:
                current_stroke = None
                status = "NO HAND DETECTED"

            # 3. Display gesture status.
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

            # 4. Display prediction.
            cv2.putText(
                frame,
                prediction_text,
                (20, 85),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 0, 0),
                2,
            )

            # 5. Display windows.
            cv2.imshow("AirScript - Camera", frame)
            cv2.imshow(
                "AirScript - Drawing Canvas",
                canvas.get_canvas()
            )

            # 6. Keyboard controls.
            key = cv2.waitKey(1) & 0xFF

            if key == ord("p"):
                digit, confidence = predictor.predict(
                    canvas.get_canvas()
                )

                if digit is not None:
                    prediction_text = (
                        f"Prediction: {digit} "
                        f"({confidence:.2f}%)"
                    )

                    print("\nRecognized digit:", digit)
                    print(f"Confidence: {confidence:.2f}%")
                else:
                    prediction_text = "Prediction: Empty canvas"
                    print("Nothing to recognize!")

            elif key == ord("c"):
                canvas.clear()
                current_stroke = None
                prediction_text = "Prediction: None"
                print("Canvas cleared!")

            elif key == ord("q"):
                break

    finally:
        tracker.close()
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
