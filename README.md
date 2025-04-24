# AI-Application
# Emotion Predictor API

This project provides a simple API for emotion analysis in English text. It utilizes the `j-hartmann/emotion-english-distilroberta-base` model from the Hugging Face `transformers` library to identify the predominant emotion in a given sentence.

## Features

* **`/predict` Endpoint:** Accepts POST requests with text in JSON format and returns a JSON array containing the detected emotion and its confidence score.
* **Unit Tests:** Includes unit tests to verify the correct identification of joy, sadness, and a neutral state (although the latter is currently tested for 'joy' in the code).
* **Static Code Analysis:** The source code has passed static analysis with `flake8` without any errors or warnings, ensuring a clean and compliant coding style.

## Technologies Used

* **Python:** Primary programming language.
* **Flask:** Micro web framework for building the API.
* **Transformers:** Hugging Face library for using pre-trained Natural Language Processing models.
* **unittest:** Standard Python framework for writing and running unit tests.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <YOUR_REPOSITORY_URL>
    cd <YOUR_REPOSITORY_NAME>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You might need to create a `requirements.txt` file containing the dependencies. Include at least `Flask` and `transformers`)*

## Running the Application

1.  **Run the Flask application:**
    ```bash
    python app.py
    ```
    The API will be available at `http://0.0.0.0:5000/`.

2.  **Run the unit tests:**
    ```bash
    python test_emotion_predictor.py
    ```

## API Usage

You can send a POST request to the `/predict` endpoint with a JSON body containing the key `text`.

**Example Request (with `curl`):**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": "This is a fantastic day!"}' [http://0.0.0.0:5000/predict](http://0.0.0.0:5000/predict)