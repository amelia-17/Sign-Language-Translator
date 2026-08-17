# train_model.py

import tensorflow as tf 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Model architecture
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(64,64,3)),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(3, activation='softmax')  # 3 classes: A, B, C
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Data loading
datagen = ImageDataGenerator(rescale=1./255)
train = datagen.flow_from_directory(
    'A:\Sign_Translation\sign_language_translation\mock_dataset\mock_dataset',
    target_size=(64, 64),        # or your expected input size
    batch_size=32,
    class_mode='categorical'     # ✅ Make sure this is categorical!
)


# Train the model
model.fit(train, epochs=5)

# Save the model
os.makedirs("model", exist_ok=True)
model.save('model/sign_language_model.h5')

print("Class indices:", train.class_indices)

print("✅ Model trained and saved to 'model/sign_language_model.h5'")



