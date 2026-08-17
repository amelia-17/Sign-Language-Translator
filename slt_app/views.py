from django.shortcuts import render
from django.http import JsonResponse, StreamingHttpResponse
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the model and class names once
model = load_model('model/sign_language_model.h5')
class_names = ['A', 'B', 'C']  # Replace with your full class list

# View: Home page
def index(request):
    return render(request, 'index.html')  # ✅ This assumes templates/index.html is correctly placed

# Webcam video stream generator
def gen_frames():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # ✅ Use DSHOW on Windows to avoid MSMF errors

    try:
        while True:
            success, frame = cap.read()
            if not success:
                print("❌ Failed to grab frame")
                break

            # Preprocess for model
            roi = cv2.resize(frame, (64, 64))
            roi = roi.astype('float32') / 255.0
            roi = np.expand_dims(roi, axis=0)

            # Predict
            prediction = model.predict(roi)
            result = class_names[np.argmax(prediction)]

            # Annotate frame
            cv2.putText(frame, f'Prediction: {result}', (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Encode for streaming
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Yield frame to stream
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    except GeneratorExit:
        print("🔌 Client disconnected — stopping webcam stream")

    finally:
        print("📷 Releasing webcam")
        cap.release()
        cv2.destroyAllWindows()  # ✅ Moved inside finally

# View: Video stream
def video_feed(request):
    return StreamingHttpResponse(gen_frames(),
        content_type='multipart/x-mixed-replace; boundary=frame')

# Optional: Prediction endpoint (if using AJAX)
def get_sign(request):
    from webcam import get_prediction  # ✅ Make sure webcam.py has this function
    result = get_prediction()
    return JsonResponse({'prediction': result})
