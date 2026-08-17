# gen_mock_dataset.py
import os
import numpy as np
from PIL import Image

categories = ['A', 'B', 'C']
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue

for cat, color in zip(categories, colors):
    path = os.path.join('mock_dataset', cat)
    os.makedirs(path, exist_ok=True)
    for i in range(2):  # create 2 images per class
        img = Image.new('RGB', (64, 64), color=color)
        img.save(os.path.join(path, f'{cat.lower()}{i+1}.jpg'))

print("✅ Mock dataset created in 'mock_dataset/'")
