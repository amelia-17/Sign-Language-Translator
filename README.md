## Sign Language Translator

A Python-based Sign Language Translator that uses **Django, Machine Learning, and Computer Vision** to recognize sign-language gestures through webcam input.

## Features

* Real-time sign-language recognition using a webcam
* Machine learning model for gesture classification
* Django-based web application
* Model training script included
* Webcam inference support
* Simple and user-friendly interface
* Score/output display for recognized signs

## Technologies Used

* **Python**
* **Django**
* **TensorFlow / Keras**
* **OpenCV**
* **Pygame**
* **NumPy**
* **HTML / CSS**

## Project Structure

```text
Sign-Language-Translator/
│
├── model/
│   └── sign_language_model.h5
│
├── sign_language_translation/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── slt_app/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── train_model.py
├── webcam.py
├── manage.py
├── .gitignore
└── README.md
```

## How It Works

1. The webcam captures the user's hand gestures.
2. The captured input is processed using computer-vision techniques.
3. The processed input is passed to the trained machine-learning model.
4. The model predicts the corresponding sign.
5. The prediction is displayed through the application.

## Installation

Clone the repository:

```bash
git clone https://github.com/amelia-17/Sign-Language-Translator.git
cd Sign-Language-Translator
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

Start the Django development server:

```bash
python manage.py runserver
```

Then open the local development server in your browser.

For webcam-based prediction, run:

```bash
python webcam.py
```

## Model

The trained model is stored in:

```text
model/sign_language_model.h5
```

The project also includes `train_model.py` for training the machine-learning model.

## Future Improvements

* Support for a larger sign-language vocabulary
* Improved prediction accuracy
* Sentence-level sign translation
* Better handling of different lighting and backgrounds
* Improved user interface
* Deployment as an online application


## License

This project is created for educational and learning purposes.
