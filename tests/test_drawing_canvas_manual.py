
import cv2

from airscript.drawing_canvas import DrawingCanvas


# Create a blank canvas.
canvas = DrawingCanvas(width=800, height=600)

# Draw two connected lines.
canvas.draw_line((100, 100), (300, 100))
canvas.draw_line((300, 100), (300, 300))

# Display the canvas.
cv2.imshow("AirScript - Canvas Test", canvas.get_canvas())

print("Canvas test running!")
print("Press C to clear the canvas.")
print("Press Q to quit.")

while True:
    key = cv2.waitKey(1) & 0xFF

    if key == ord("c"):
        canvas.clear()
        cv2.imshow("AirScript - Canvas Test", canvas.get_canvas())
        print("Canvas cleared!")

    elif key == ord("q"):
        break

cv2.destroyAllWindows()
