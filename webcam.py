# webcam.py
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load trained model
model = load_model('model/sign_language_model.h5')

# Assuming you trained on A, B, C only
class_names = ['A', 'B', 'C']

# Start video capture
cap = cv2.VideoCapture(0)

window_name = "Sign Language Translator"
cv2.namedWindow(window_name)

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    cv2.imshow(window_name, frame)

    # Break if 'q' is pressed or window is closed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Check if the window was closed manually
    if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
