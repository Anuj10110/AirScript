
import cv2
import numpy as np

from airscript.digit_predictor import DigitPredictor

# Load trained model
predictor = DigitPredictor()

# Create a white test canvas
canvas = np.ones((720, 1280, 3), dtype=np.uint8) * 255

# Draw digit 7 in black
cv2.putText(
    canvas,
    "7",
    (450, 500),
    cv2.FONT_HERSHEY_SIMPLEX,
    10,
    (0, 0, 0),
    25
)

# Predict
digit, confidence = predictor.predict(canvas)

print("\nPredicted digit:", digit)
print(f"Confidence: {confidence:.2f}%")

# Display test image
cv2.imshow("Digit Test", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
