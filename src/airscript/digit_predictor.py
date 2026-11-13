import cv2
import numpy as np
import torch

from airscript.digit_model import DigitCNN


class DigitPredictor:
    """Predicts handwritten digits from AirScript canvas."""

    def __init__(self, model_path="models/digit_cnn.pth"):

        if torch.backends.mps.is_available():
            self.device = torch.device("mps")
        elif torch.cuda.is_available():
            self.device = torch.device("cuda")
        else:
            self.device = torch.device("cpu")

        self.model = DigitCNN().to(self.device)

        state_dict = torch.load(
            model_path,
            map_location=self.device,
            weights_only=True
        )

        self.model.load_state_dict(state_dict)
        self.model.eval()

        print("Digit predictor loaded on:", self.device)

    def preprocess(self, canvas):
        """Convert AirScript drawing into MNIST-style input."""

        gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)

        _, binary = cv2.threshold(
            gray, 200, 255, cv2.THRESH_BINARY_INV
        )

        coords = cv2.findNonZero(binary)

        if coords is None:
            return None

        x, y, w, h = cv2.boundingRect(coords)
        digit = binary[y:y+h, x:x+w]

        scale = 20.0 / max(w, h)

        new_w = max(1, int(w * scale))
        new_h = max(1, int(h * scale))

        resized = cv2.resize(
            digit,
            (new_w, new_h),
            interpolation=cv2.INTER_AREA
        )

        image = np.zeros((28, 28), dtype=np.uint8)

        x_offset = (28 - new_w) // 2
        y_offset = (28 - new_h) // 2

        image[
            y_offset:y_offset + new_h,
            x_offset:x_offset + new_w
        ] = resized

        kernel = np.ones((2, 2), np.uint8)
        image = cv2.dilate(image, kernel, iterations=1)

        moments = cv2.moments(image)

        if moments["m00"] > 0:
            cx = int(moments["m10"] / moments["m00"])
            cy = int(moments["m01"] / moments["m00"])

            shift_x = 14 - cx
            shift_y = 14 - cy

            matrix = np.float32([
                [1, 0, shift_x],
                [0, 1, shift_y]
            ])

            image = cv2.warpAffine(
                image,
                matrix,
                (28, 28),
                borderValue=0
            )

        image = image.astype(np.float32) / 255.0
        image = (image - 0.1307) / 0.3081

        tensor = torch.from_numpy(image).unsqueeze(0).unsqueeze(0)

        return tensor.to(self.device)

    def predict(self, canvas):

        tensor = self.preprocess(canvas)

        if tensor is None:
            return None, 0.0

        with torch.no_grad():
            outputs = self.model(tensor)
            probabilities = torch.softmax(outputs, dim=1)

            confidence, prediction = probabilities.max(dim=1)

        return prediction.item(), confidence.item() * 100
